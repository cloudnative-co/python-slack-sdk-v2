# -*- coding: utf-8 -*-
# import module snippets
import sys
from typing import Union
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Team(Base):
    """
    @namespace  Slack.team
    @class      Team
    @brief      Slack チーム操作用クラス
    """
    class Profile(Base):
        """
        @namespace  Slack.team
        @class      Profile
        @brief      チームプロファイル操作用クラス
        """
        path = {
            "get": "team.profile.get"
        }

        def get(
            self,
            visiblity: str = None
        ):
            query = get_arguments(locals())
            path = self.path[sys._getframe().f_code.co_name]
            return self.http_request(method="get", path=path, query=query)

    path = {
        "access_logs": "team.accessLogs",
        "billable_info": "team.billableInfo",
        "info": "team.info",
        "integration_logs": "team.integrationLogs",
    }

    __profile = None

    def access_logs(
        self, before: Union[str, int] = "now", count: int = 100, page: int = 1
    ):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    def billable_info(self, user: str):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    def info(self, team: str):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    def integration_logs(
        self, app_id: str = None, change_type: str = None, count: int = 100,
        page: int = 1, service_id: str = None, user: str = None
    ):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    @property
    def profile(self):
        if self.__profile is None:
            self.__profile = self.__class__.Profile(client=self)
        return self.__profile
