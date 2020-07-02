# -*- coding: utf-8 -*-
# import module snippets
import sys
import datetime
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Calls(Base):
    """
    @namespace  Slack.calls
    @class      Callls
    @brief      Slack通話用クラス
    """

    class Participants(Base):
        """
        @namespace  Slack.calls
        @class      Participants
        @brief      Slack参加者管理用クラス
        """

        path = {
            "add": "calls.participants.add",
            "remove": "calls.participants.remove"
        }

        @formation
        def add(
            self, id: str, users: list,
            payload: dict = None
        ):
            path = self.path[sys._getframe().f_code.co_name]
            return self.http_request(method="post", path=path, payload=payload)

        @formation
        def remove(
            self, id: str, users: list,
            payload: dict = None
        ):
            path = self.path[sys._getframe().f_code.co_name]
            return self.http_request(method="post", path=path, payload=payload)

    path = {
        "add": "calls.add",
        "end": "calls.end",
        "info": "calls.info",
    }

    __participants: Participants = None

    @formation
    def add(
        self, external_unique_id: str, join_url: str, created_by: str = None,
        date_start: datetime.datetime = None, desktop_app_join_url: str = None,
        external_display_id: str = None, title: str = None, users: list = None,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @formation
    def end(self, id: str, duration: int = None, payload: dict = None):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @formation
    def info(self, id: str, payload: dict = None):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @formation
    def update(
        self, id: str, desktop_app_join_url: str = None, join_url: str = None,
        title: str = None, payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @property
    def particcipants(self):
        if self.__particcipants is None:
            self.__particcipants = self.__class__.Particcipants(client=self)
        return self.__particcipants
