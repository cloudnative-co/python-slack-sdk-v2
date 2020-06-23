# -*- coding: utf-8 -*-
# import module snippets
import sys
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Pins(Base):
    """
    @namespace  Slack.pins
    @class      Pins
    @brief      Slackピン操作用クラス
    """

    path = {
        "add": "pins.add",
        "list": "pins.list",
        "remove": "pins.remove",
    }

    @formation
    def add(self, channel: str, timestamp: str, payload: dict = None):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    def list(self, channel: str):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    @formation
    def remove(
        self, channel: str,
        file: str = None, file_comment: str = None, timestamp: str = None,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)
