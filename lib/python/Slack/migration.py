# -*- coding: utf-8 -*-
# import module snippets
import sys
from .base import Base
from .Utilities.utilities import get_arguments


class Migration(Base):
    """
    @namespace  Slack.migration
    @class      Migration
    @brief      Slackマイグレーション用クラス
    """

    path = {
        "exchange": "migration.exchange"
    }

    def exchange(self, users: list, to_old: bool = None):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)
