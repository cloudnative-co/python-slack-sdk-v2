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
    print(value)
    if value is None:
        value = "null"
    elif isinstance(value, bool):
        value = "true" if value else "false"
    elif isinstance(value, str):
        value = '"{}"'.format(value)
    elif isinstance(value, datetime.datetime):
        value = value.timestamp()
        value = '"{}"'.format(value)
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
        print(str_params)
        payload = json.loads(str_params)
        payload = remove_none(payload)
        kwargs["payload"] = payload
        return f(*args, **kwargs)
    return wrapper
