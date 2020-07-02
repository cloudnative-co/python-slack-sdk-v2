# -*- coding: utf-8 -*-
# import module snippets
import sys
from .base import Base
from .Utilities.utilities import formation


class OAuth(Base):
    """
    @namespace  Slack.oauth
    @class      OAuth
    @brief      Slack認証用クラス
    """

    path = {
        "access": "oauth.v2.access"
    }

    @formation
    def access(
        self,
        code: str,
        client_id: str = None,
        client_secret: str = None,
        redirect_uri: str = None,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)
