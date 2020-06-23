# -*- coding: utf-8 -*-
# import module snippets
import sys
from .base import Base
from .Utilities.utilities import get_arguments


class Rtm(Base):
    """
    @namespace  Slack.rtm
    @class      Rtm
    @brief      Slackリアルタイムメッセージ操作用クラス
    """

    path = {
        "connect": "rtm.connet",
        "start": "rtm.start"
    }

    def connect(
        self, batch_presence_aware: str = None, presence_sub: str = None
    ):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    def start(
        self, batch_presence_aware: str = None, include_local: bool = None,
        mpim_aware: bool = None, no_latest: int = 0, presence_sub: str = None,
        simple_latest: bool = None
    ):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)
