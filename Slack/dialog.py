# -*- coding: utf-8 -*-
# import module snippets
import sys
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Dialog(Base):
    """
    @namespace  Slack.dialog
    @class      Dialog
    @brief      Slackダイアログ操作用
    """
    path = {
        "open": "dialog.open"
    }

    @formation
    def open(self, trigger_id: str, dialog: dict, payload: dict = None):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)
