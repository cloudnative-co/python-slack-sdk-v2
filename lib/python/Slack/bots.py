# -*- coding: utf-8 -*-
# import module snippets
import sys
from .base import Base
from .Utilities.utilities import get_arguments


class Bots(Base):
    """
    @namespace  Slack
    @class      Bots
    @brief      Slackボット情報取得クラス
    """

    path = {
        "info": "bots.info"
    }

    def info(self, bot: str = None):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)
