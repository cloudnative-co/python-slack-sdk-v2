# -*- coding: utf-8 -*-
# import module snippets
import sys
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Views(Base):
    """
    @namespace  Slack.views
    @class      Views
    @brief      Slackモーダルビュー操作用
    """
    path = {
        "open": "views.open",
        "publish": "views.publish",
        "push": "views.push",
        "update": "views.update",
    }

    @formation
    def open(self, trigger_id: str, view: dict, payload: dict = None):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, payload=payload)

    @formation
    def publish(
        self, user_id: str, view: dict, hash: str = None, payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, payload=payload)

    @formation
    def push(self, trigger_id: str, view: dict, payload: dict = None):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, payload=payload)

    @formation
    def update(
        self, view: dict, external_id: str = None, hash: str = None,
        view_id: str = None, payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, payload=payload)
