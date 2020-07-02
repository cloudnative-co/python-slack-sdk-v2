import sys
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation
import threading


class Channels(Base):
    """
    @namespace  Slack
    @class      Channel
    @brief      Slackチャンネル操作用
    """
    path = {
        "info": "channels.info"
    }

    def info(self, channel: str, include_locale: bool = False):
        args = locals()
        path = self.path[sys._getframe().f_code.co_name]
        query = get_arguments(args)
        return self.http_request(method="get", path=path, query=query)

    def members(self, channel: str):
        response = self.info(channel=channel)
        users = response["channel"]["members"]
        results = []
        threadlist = list()
        for user_id in users:
            thread = threading.Thread(
                target=self.__get_profile,
                args=([user_id, results]),
            )
            threadlist.append(thread)
            thread.start()
        for thread in threadlist:
            thread.join()
        return results

    def __get_profile(self, user_id: str, results):
        response = self.user.profile(user=user_id)
        results.append(response["profile"])

    def history(
        self, channel: str,
        count: int = 100, inclusive: int = 0,
        latest: str = "", oldest: int = 0, unreads: int = 0
    ):
        query = locals()
        del query["self"]
        path = "{}.history".format(self.path)
        return self.http_request(method="get", path=path, query=query)
