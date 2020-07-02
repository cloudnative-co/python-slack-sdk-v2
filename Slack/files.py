# -*- coding: utf-8 -*-
# import module snippets
import sys
import io
from typing import Union
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Files(Base):
    """
    @namespace  Slack.files
    @class      Files
    @brief      Slackファイル操作用
    """

    class Comments(Base):
        """
        @namespace  Slack.files
        @class      Comments
        @brief      Slackファイルコメント操作用
        """
        path = {
            "delete": "files.comments.delete",
        }

        @formation
        def delete(self, file: str, id: str, payload: dict = None):
            path = self.path[sys._getframe().f_code.co_name]
            return self.http_request(method="post", path=path, payload=payload)

    class Remote(Base):
        """
        @namespace  Slack.files
        @class      Remote
        @brief      Slackリモートファイル操作用
        """
        path = {
            "add": "files.remote.add",
            "info": "files.remote.info",
            "list": "files.remote.list",
            "remove": "files.remote.remove",
            "share": "files.remote.share",
            "upload": "files.remote.upload"
        }

        def add(
            self,
            external_id: str,
            external_url: str,
            title: str,
            filetype: str = None,
            indexable_file_contents: str = None,
            preview_image: io.BytesIO = None
        ):
            query = get_arguments(locals())
            path = self.path[sys._getframe().f_code.co_name]
            return self.http_request(method="get", path=path, query=query)

        def info(self, external_id: str = None, file: str = None):
            query = get_arguments(locals())
            path = self.path[sys._getframe().f_code.co_name]
            return self.http_request(method="get", path=path, query=query)

        def list(
            self, channel: str = None, cursor: str = None, limit: int = None,
            ts_from: int = 0, ts_to: Union[str, int] = "now"
        ):
            query = get_arguments(locals())
            path = self.path[sys._getframe().f_code.co_name]
            return self.http_request(method="get", path=path, query=query)

        def remove(self, external_id: str = None, file: str = None):
            query = get_arguments(locals())
            path = self.path[sys._getframe().f_code.co_name]
            return self.http_request(method="get", path=path, query=query)

        def share(
            self, channels: str, external_id: str = None, file: str = None
        ):
            query = get_arguments(locals())
            path = self.path[sys._getframe().f_code.co_name]
            return self.http_request(method="get", path=path, query=query)

        def upload(
            self,
            external_id: str = None,
            external_url: str = None,
            file: io.BytesIO = None,
            filetype: str = None,
            indexable_file_contents: str = None,
            preview_image: io.BytesIO = None,
            title: str = None
        ):
            query = get_arguments(locals())
            path = self.path[sys._getframe().f_code.co_name]
            headers = {"Content-Type": "multipart/form-data"}
            files = {
                "file": {
                    "name": filename,
                    "content": file
                }
            }
            return self.http_request(
                method="post", path=path, headers=headers, files=files
            )

    path = {
        "delete": "files.delete",
        "info": "files.info",
        "list": "files.list",
        "revoke_public_url": "files.revokePublicURL",
        "shared_public_url": "files.sharedPublicURL",
        "upload": "files.upload"
    }

    __comments: Comments = None
    __remote: Remote = None

    @formation
    def delete(self, file: str, payload: dict = None):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    def info(
        self, file: str,
        conut: int = 100, cursor: str = None, limit: int = 0, page: int = 1
    ):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    def list(
        self, channel: str = None, conut: int = 100, page: int = 1,
        show_files_hidden_by_limit: bool = None, ts_from: int = 0,
        types: str = "all", user: str = None
    ):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    @formation
    def revoke_public_url(self, file: str, payload: dict = None):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @formation
    def shared_public_url(self, file: str, payload: dict = None):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @formation
    def upload(
        self,
        channels: Union[str, list] = None,
        content: str = None,
        file: io.BytesIO = None,
        filename: str = None,
        filetype: str = None,
        initial_comment: str = None,
        thread_ts: float = None,
        title: str = None,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        headers = {"Content-Type": "multipart/form-data"}
        files = {
            "file": {
                "name": filename,
                "content": file
            }
        }
        return self.http_request(
            method="post", path=path,
            headers=headers, payload=payload, files=files
        )

    @property
    def comments(self):
        if self.__comments is None:
            self.__comments = self.__class__.Comments(client=self)
        return self.__comments

    @property
    def remote(self):
        if self.__remote is None:
            self.__remote = self.__class__.Remote(client=self)
        return self.__remote
