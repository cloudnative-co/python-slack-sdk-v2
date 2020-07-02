import sys
from .base import Base


class Emoji(Base):
    path = {
        "list": "emoji.list"
    }
    """
    @namespace  Slack
    @class      emoji
    """
    def list(self):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path)
