# -*- coding: utf-8 -*-
# import module snippets
import json
import urllib.request
import io
import sys
import os
import mimetypes
import urllib.request
import urllib.parse
import http.cookiejar
from .exception import APIException


class Base(object):
    __client: urllib.request.OpenerDirector = None
    __cookie: http.cookiejar.CookieJar = None
    __lasturl: str = None
    __header: dict = dict()
    token: str = None
    schema = "https"
    host = "slack.com/api"

    def __init__(
        self,
        token: str = None,
        client: object = None,
    ):
        if client is not None:
            self.token = client.token
            self.__client = client.__client
            self.__header = client.__header
            self.__cookie = client.__cookie
        else:
            self.token = token
            self.__cookie = http.cookiejar.CookieJar()
            self.__client = urllib.request.build_opener(
                urllib.request.HTTPCookieProcessor(self.__cookie)
            )
            urllib.request.install_opener(self.__client)
            ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "\
                 "AppleWebKit/537.36 (KHTML, like Gecko) "\
                 "Chrome/70.0.3538.102 Safari/537.36 Edge/18.18362"
            self.__header = {
                "Accepted-Content-Type": "application/x-www-form-urlencoded",
                "Accept-Language": "ja",
                "Cache-Control": "max-age=0",
                "Connection": "Keep-Alive",
                "User-Agent": ua
            }

    def encode_multipart(
        self, payload: dict = None, files: dict = None, charset="utf-8"
    ):
        boundary = '----------lImIt_of_THE_fwIle_eW_$'
        bf = io.BytesIO()
        if payload is not None:
            for key, value in payload.items():
                bf.write(('--%s\r\n' % boundary).encode(charset))
                bf.write((
                    'Content-Disposition: form-data; name="%s"' % key
                ).encode(charset))
                bf.write(b'\r\n\r\n')
                if isinstance(value, dict):
                    value = json.dumps(value)
                elif isinstance(value, str):
                    value = value.encode(charset)
                elif isinstance(value, list):
                    value = json.dumps(value)
                    value = value.encode(charset)
                try:
                    bf.write(value)
                except Exception as e:
                    raise e
                bf.write(b'\r\n')
        if files is not None:
            cdisp = 'Content-Disposition: form-data; ' \
                    'name="%s"; filename="%s"\r\n'
            for key, value in files.items():
                filename = value["name"]
                bf.write(('--%s\r\n' % boundary).encode(charset))
                bf.write((cdisp % (key, filename)).encode(charset))
                typ = mimetypes.guess_type(filename)[0]
                typ = typ or 'application/octet-stream'
                bf.write(("Content-Type: {}\r\n".format(typ)).encode(charset))
                content = value["content"]
                if hasattr(content, "read"):
                    content = content.read()
                bf.write(b'\r\n')
                bf.write(content)
                bf.write(b'\r\n')
        bf.write(('--' + boundary + '--\r\n\r\n').encode(charset))
        bf = bf.getvalue()
        content_type = 'multipart/form-data; boundary=%s' % boundary
        return content_type, bf

    def http_request(
        self,
        method: str, path: str = None, headers: dict = {},
        query: dict = None, payload: dict = None, url: str = None,
        files: dict = None, is_read: bool = True, with_header: bool = False,
        charset: str = "utf-8"
    ):
        if url is None:
            url = "{}://{}/{}".format(self.schema, self.host, path)
        if query is None:
            query = dict()
        if "?" in url:
            q = url.split("?")
            if query is None:
                query = dict()
            for q1 in q[1].split("&"):
                q1 = q1.split("=")
                query[q1[0]] = q1[1]
        if method == "get":
            query["token"] = self.token
        elif method == "post":
            headers["Authorization"] = "Bearer {}".format(self.token)
        if len(query) > 0:
            url = "{}?{}".format(url, urllib.parse.urlencode(query))

        args = {
            "url": url,
            "method": method.upper()
        }
        ctype = headers.get('Content-Type', None)
        if ctype == "multipart/form-data":
            ctype, payload = self.encode_multipart(payload, files, charset)
            headers["Content-Type"] = ctype
            args["data"] = payload
        elif ctype == "application/octet-stream":
            args["data"] = payload
        elif payload is not None:
            try:
                payload = json.dumps(payload).encode('utf-8')
                headers["Content-Type"] = "application/json; charset=UTF-8"
            except TypeError as e:
                try:
                    payload = urllib.parse.urlencode(payload).encode()
                except Exception as e:
                    pass
            args["data"] = payload
        else:
            payload = b""
        args["headers"] = dict(self.__header, **headers)
        req = urllib.request.Request(**args)
        try:
            with self.__client.open(req) as res:
                head = dict(res.info())
                if is_read:
                    body = res.read()
                    try:
                        body = body.decode("utf-8")
                    except UnicodeDecodeError:
                        if with_header:
                            return body, head
                        return body
                    try:
                        body = json.loads(body)
                        if with_header:
                            return body, head
                        return body
                    except Exception as e:
                        if with_header:
                            return body, head
                        return body
                return res
        except urllib.error.HTTPError as e:
            raise APIException(e)
