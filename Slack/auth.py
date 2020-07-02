# -*- coding: utf-8 -*-
# import module snippets
import sys
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Auth(Base):
    """
    @namespace  Slack.auth
    @class      Auth
    @brief      Slack認証用クラス
    """

    path = {
        "revoke": "auth.revoke",
        "test": "auth.test"
    }

    def revoke(self, test: str = None):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    def test(self):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path)
