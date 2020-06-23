# -*- coding: utf-8 -*-
# import module snippets
import sys
import datetime
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Reminders(Base):
    """
    @namespace  Slack.reminders
    @class      Reminders
    @brief      Slackリマインダー操作用クラス
    """

    path = {
        "add": "reminders.add",
        "complete": "reminders.complete",
        "delete": "reminders.delete",
        "info": "reminders.info",
        "list": "reminders.list"
    }

    @formation
    def add(
        self, text: str, time: datetime.datetime, user: str,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @formation
    def complete(self, reminder: str, payload: dict = None):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @formation
    def delete(self, reminder: str, payload: dict = None):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    def info(self, reminder: str):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    def list(self):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)
