# -*- coding: utf-8 -*-
# import module snippets
import sys
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Reactions(Base):
    """
    @namespace  Slack.reaction
    @class      Reactions
    @brief      Slack絵文字リアクション操作用クラス
    """

    path = {
        "add": "reactions.add",
        "get": "reactions.get",
        "list": "reactions.list",
        "remove": "reactions.remove",
    }

    @formation
    def add(
        self, channel: str, name: str, timestamp: str,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    def get(
        self, channel: str = None, file: str = None, file_comment: str = None,
        full: bool = None, timestamp: str = None
    ):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    def list(
        self, count: int = 100, cursor: str = None, full: bool = None,
        limit: int = 0, page: int = 1, user: str = None
    ):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    @formation
    def remove(
        self, name: str, channel: str = None, file: str = None,
        file_comment: str = None, timestamp: str = None, payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)
