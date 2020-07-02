# -*- coding: utf-8 -*-
# import module snippets
import sys
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Stars(Base):
    """
    @namespace  Slack.stars
    @class      Stars
    @brief      Slack スター操作用クラス
    """

    path = {
        "add": "stars.add",
        "list": "stars.list",
        "remove": "stars.remove",
    }

    @formation
    def add(
        self, channel: str, file: str = None, file_comment: str = None,
        timestamp: str = None, payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    def list(
        self,
        count: int = 100, cursor: str = None, limit: int = 0, page: int = 1
    ):
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
