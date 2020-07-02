# -*- coding: utf-8 -*-
# import module snippets
import io
import sys
from typing import Union
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class UserGroups(Base):
    """
    @namespace  Slack.usergroups
    @class      UserGroups
    @brief      Slackユーザーグループ操作用
    """
    class Users(Base):
        """
        @namespace  Slack.usergroups
        @class      Users
        @brief      Slackユーザーグループのメンバー操作用
        """
        path = {
            "list": "usergroups.users.list",
            "update": "usergroups.users.update"
        }

        def list(self, usergroup: str, include_disabled: bool = False):
            query = get_arguments(locals())
            path = self.path[sys._getframe().f_code.co_name]
            return self.http_request(method="get", path=path, query=query)

        @formation
        def update(
            self, usergroup: str = None, users: Union[list, str] = None,
            include_count: bool = None, payload: dict = None
        ):
            path = self.path[sys._getframe().f_code.co_name]
            return self.http_request(method="post", path=path, payload=payload)

    path = {
        "create": "usergroups.create",
        "disable": "usergroups.disable",
        "enable": "usergroups.enable",
        "list": "usergroups.list",
        "update": "usergroups.update"
    }

    __users: Users = None

    @formation
    def create(
        self, name: str = None, channels: Union[list, str] = None,
        description: str = None, handle: str = None,
        include_count: bool = None, payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @formation
    def disable(
        self, usergroup: str, include_count: bool = None, payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @formation
    def enable(
        self, usergroup: str, include_count: bool = None, payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    def list(
        self,
        include_count: bool = False,
        include_disabled: bool = False,
        include_users: bool = False,
    ):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    @formation
    def update(
        self, usergroup: str = None, channels: Union[list, str] = None,
        description: str = None, handle: str = None,
        include_count: bool = None, name: str = None, payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @property
    def users(self):
        if self.__users is None:
            self.__users = self.__class__.Users(client=self)
        return self.__users
