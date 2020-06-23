# -*- coding: utf-8 -*-
# import module snippets
import sys
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Api(Base):
    """
    @namespace  Slack
    @class      Api
    @brief      SlackAPIテスト用クラス
    """

    path = {
        "test": "api.test"
    }

    @formation
    def test(self, error: str = None, foo: str = None, payload: dict = None):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, payload=payload)
