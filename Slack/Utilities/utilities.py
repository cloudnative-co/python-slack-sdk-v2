import json
import datetime
import inspect
from .maps import Maps


def get_arguments(args: dict, keys: list = None, ignores: list = None):
    def snake_to_kebab(key):
        ret = []
        for key in key.split("_"):
            ret.append(key.capitalize())
        return "-".join(ret)

    ret = {}
    for ky in args:
        if ky == "self":
            continue
        if keys is not None:
            if ky not in keys:
                continue
        if ignores is not None:
            if ky in ignores:
                continue
        if args[ky] is None:
            continue
        if args[ky] is not None:
            if isinstance(args[ky], datetime.datetime):
                ret[ky] = args[ky].timestamp()
            elif isinstance(args[ky], list):
                ret[ky] = ",".join(args[ky])
            else:
                ret[ky] = args[ky]
    return ret


def parse_values(value):
    if value is None:
        value = "null"
    elif isinstance(value, bool):
        value = "true" if value else "false"
    elif isinstance(value, str):
        value = value.replace("\n", "\\n")
        value = value.replace("\r", "\\r")
        value = value.replace("\t", "\\t")
        value = value.replace("\u3000", " ")
        value = '"{}"'.format(value)
    elif isinstance(value, datetime.datetime):
        value = value.timestamp()
        value = '"{}"'.format(value)
    elif isinstance(value, dict):
        value = json.dumps(value)
    elif isinstance(value, list):
        if len(value) == 1:
            value = parse_values(value[0])
        else:
            try:
                value = json.dumps(value)
            except TypeError as e:
                value = "null"
    return value


def formation(f):
    def remove_none(params: dict):
        result = {}
        for k in params:
            v = params.get(k, None)
            if v is None:
                continue
            if isinstance(v, dict):
                v = remove_none(v)
                if v is None:
                    continue
            if isinstance(v, list):
                tmp_lst = []
                for v1 in v:
                    if isinstance(v1, dict):
                        v1 = remove_none(v1)
                        if v1 is None:
                            continue
                    tmp_lst.append(v1)
                if len(tmp_lst) == 0:
                    continue
                v = tmp_lst
            if isinstance(v, str):
                v = v.replace("\\r", "")
                v = v.replace("\\t", "\t")
                v = v.replace("\\n", "\n")
            result[k] = v
        if len(result) == 0:
            return None
        return result

    def wrapper(*args, **kwargs):
        if "payload" in kwargs:
            return f(*args, **kwargs)
        m = inspect.getmembers(f)
        a, member = m[0]
        lst_args = list(member.keys())
        _kwargs = {}
        for arg_name in lst_args:
            arg_value = "null"
            if arg_name in kwargs:
                arg_value = kwargs.get(arg_name)
                arg_value = parse_values(arg_value)
            _kwargs[arg_name] = arg_value
        method_name = f.__qualname__
        maps = Maps[method_name]
        str_params = maps.format(**_kwargs)
        payload = json.loads(str_params)
        payload = remove_none(payload)
        kwargs["payload"] = payload
        return f(*args, **kwargs)
    return wrapper

def signing_secret(
    signing_secret: str,
    request_timestamp: str,
    signature: str,
    body,
    debug: bool = False
):
    if abs(time.time() - int(request_timestamp)) > 60 * 5:
        if not debug:
            raise Exception("Timestamp Invalid")

    message = "v0:{}:{}".format(request_timestamp, body)
    message_bytes = bytes(message, 'UTF-8')
    request_hash = 'v0=' + hmac.new(
        str.encode(signing_secret),
        message_bytes,
        hashlib.sha256
    ).hexdigest()

    result = False
    if hasattr(hmac, "compare_digest"):
        if (sys.version_info[0] == 2):
            result = hmac.compare_digest(bytes(request_hash), bytes(signature))
        else:
            result = hmac.compare_digest(request_hash, signature)
    else:
        if len(request_hash) != len(signature):
            raise Exception("Signature invalid")
        result = 0
        if isinstance(request_hash, bytes) and isinstance(signature, bytes):
            for x, y in zip(request_hash, signature):
                result |= x ^ y
        else:
            for x, y in zip(request_hash, signature):
                result |= ord(x) ^ ord(y)
        result = result == 0

    if not result:
        raise Exception("Signature invalid")
    return result
