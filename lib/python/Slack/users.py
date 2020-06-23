# -*- coding: utf-8 -*-
# import module snippets
import io
import sys
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Users(Base):
    """
    @namespace  Slack.users
    @class      Users
    @brief      Slackユーザー操作用クラス
    """

    class Profile(Base):
        """
        @namespace  Slack.users
        @class      Profile
        @brief      ユーザープロファイル操作用クラス
        """
        path = {
            "get": "users.profile.get",
            "set": "users.profile.set"
        }

        def get(
            self,
            include_labels: bool = False,
            user: str = None,
        ):
            query = get_arguments(locals())
            path = self.path[sys._getframe().f_code.co_name]
            return self.http_request(method="get", path=path, query=query)

        @formation
        def set(
            self,
            name: str = None,
            profile: dict = None,
            user: str = None,
            value: str = None,
            payload: dict = None,
        ):
            path = self.path[sys._getframe().f_code.co_name]
            return self.http_request(method="post", path=path, payload=payload)

    path = {
        "conversations": "users.conversations",
        "delete_photo": "users.deletePhoto",
        "get_presence": "users.getPresence",
        "identity": "users.identity",
        "list": "users.list",
        "info": "users.info",
        "lookup_by_email": "users.lookupByEmail",
        "set_archive": "users.setArchive",
        "set_photo": "users.setPhoto",
        "set_presence": "users.setPresence"
    }
    __profile = None

    def __init__(
        self,
        token: str = None,
        client: object = None,
    ):
        super(Users, self).__init__(token, client)

    def conversations(
        self,
        cursor: str = None,
        exclude_archived: bool = False,
        limit: int = 100,
        types: str = "public_channel",
        user: str = None
    ):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    def delete_photo(self):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path)

    def get_presence(self, user: str):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    def info(
        self,
        user: str,
        include_locale: bool = False,
    ):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    def identity(self):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path)

    def list(
        self,
        cursor: str = None,
        include_locale: bool = False,
        limit: int = 0,
    ):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    def lookup_by_email(self, email: str):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    def set_archive(self):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path)

    @formation
    def set_photo(
        self,
        image: io.BytesIO,
        content_type: str = "image/png",
        crop_w: int = None,
        crop_x: int = None,
        crop_y: int = None,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        headers = {"Content-Type": "multipart/form-data"}
        files = {
            "file": {
                "name": "photo.{}".format(content_type.replace("image/", "")),
                "content": image
            }
        }
        return self.http_request(
            method="post", path=path,
            headers=headers, payload=payload, files=files
        )

    @formation
    def set_presence(
        self,
        presence: str,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @property
    def profile(self):
        if self.__profile is None:
            self.__profile = self.__class__.Profile(client=self)
        return self.__profile
