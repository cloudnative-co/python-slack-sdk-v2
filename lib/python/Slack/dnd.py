# -*- coding: utf-8 -*-
# import module snippets
import sys
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Dnd(Base):
    """
    @namespace  Slack.dnd
    @class      Dnd
    @brief      Slack拒否モード(Do Not Disturb)設定用クラス
    """

    path = {
        "end_dnd": "dnd.endDnd",
        "end_snooze": "dnd.endSnooze",
        "info": "dnd.info",
        "set_snooze": "dnd.setSnooze",
        "team_info": "dnd.teamInfo"
    }

    def end_dnd(self):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path)

    def end_snooze(self):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path)

    def info(self, user: str = None):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    def set_snooze(self, num_minuites: int):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    def team_info(self, users: list):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)
