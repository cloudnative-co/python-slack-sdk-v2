# -*- coding: utf-8 -*-
# import module snippets
import sys
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Apps(Base):
    """
    @namespace  Slack.apps
    @class      Apps
    @brief      Slackアプリケーション情報取得クラス
    """

    class Permissions(Base):
        """
        @namespace  Slack.apps
        @class      Apps.Permissions
        @brief      Slackアプリケーション権限情報取得クラス
        """

        class Resources(Base):
            """
            @namespace  Slack.apps
            @class      Apps.Permisions.Resources
            @brief      Slackアプリケーション権限のリソース情報取得クラス
            """
            path = {
                "list": "apps.permissions.resources.list"
            }

            def list(self, cursor: str = None, limit: int = None):
                query = get_arguments(locals())
                path = self.path[sys._getframe().f_code.co_name]
                return self.http_request(method="get", path=path, query=query)

        class Scopes(Base):
            """
            @namespace  Slack.apps
            @class      Apps.Permissions.Scopes
            @brief      Slackアプリケーション権限のスコープ情報取得クラス
            """
            path = {
                "list": "apps.permissions.scopes.list"
            }

            def list(self, cursor: str = None, limit: int = None):
                query = get_arguments(locals())
                path = self.path[sys._getframe().f_code.co_name]
                return self.http_request(method="get", path=path, query=query)

        class Users(Base):
            """
            @namespace  Slack.apps
            @class      Apps.Permissions.Users
            @brief      Slackアプリケーション権限のスコープ情報取得クラス
            """
            path = {
                "list": "apps.permissions.users.list",
                "request": "apps.permissions.users.request"
            }

            def list(self, cursor: str = None, limit: int = None):
                query = get_arguments(locals())
                path = self.path[sys._getframe().f_code.co_name]
                return self.http_request(method="get", path=path, query=query)

            def request(self, scopes: list, trigger_id: str, user: str):
                query = get_arguments(locals())
                path = self.path[sys._getframe().f_code.co_name]
                return self.http_request(method="get", path=path, query=query)

        path = {
            "info": "apps.permissions.info",
            "request": "apps.permissions.request"
        }

        __scopes: Scopes = None
        __resources: Resources = None
        __users: Users = None

        def info(self):
            path = self.path[sys._getframe().f_code.co_name]
            return self.http_request(method="get", path=path)

        def request(self, scopes: list, trigger_id: str = None):
            query = get_arguments(locals())
            path = self.path[sys._getframe().f_code.co_name]
            return self.http_request(method="get", path=path, query=query)

        @property
        def resources(self):
            if self.__resources is None:
                self.__resources = self.__class__.Resources(client=self)
            return self.__resources

        @property
        def scopes(self):
            if self.__scopes is None:
                self.__scopes = self.__class__.Scopes(client=self)
            return self.__scopes

        @property
        def users(self):
            if self.__users is None:
                self.__users = self.__class__.Users(client=self)
            return self.__users

    path = {
        "uninstall": "apps.uninstall"
    }
    __permissions: Permissions = None

    def uninstall(self, client_id: str, client_secret: str):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    @property
    def permissions(self):
        if self.__permissions is None:
            self.__permissions = self.__class__.Permissions(client=self)
        return self.__permissions
