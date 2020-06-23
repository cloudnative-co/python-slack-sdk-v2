# -*- coding: utf-8 -*-
# import module snippets
import sys
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Conversations(Base):
    """
    @namespace  Slack.conversations
    @class      Conversations
    @brief      Slackチャンネル操作用クラス
    """
    path = {
        "archive": "conversations.archive",
        "close": "conversations.close",
        "create": "conversations.create",
        "history": "conversations.history",
        "info": "conversations.info",
        "invite": "conversations.invite",
        "join": "conversations.join",
        "kick": "conversations.kick",
        "leave": "conversations.leave",
        "list": "conversations.list",
        "members": "conversations.members",
        "open": "conversations.open",
        "rename": "conversations.rename",
        "replies": "conversations.replies",
        "set_purpose": "conversations.setPurpose",
        "set_topic": "conversations.setTopic",
        "unarchive": "conversations.unarchive"
    }

    @formation
    def archive(
        self,
        channel: str = None,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @formation
    def close(
        self,
        channel: str = None,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @formation
    def create(
        self,
        name: str,
        is_private: bool = None,
        user_ids: list = None,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    def history(
        self,
        channel: str,
        cursor: str = None,
        inclusive: bool = False,
        latest: str = "now",
        limit: int = 100,
        oldest: float = 0
    ):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    def info(
        self,
        channel: str,
        include_locale: bool = False,
        include_num_members: bool = False
    ):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    @formation
    def invite(
        self,
        channel: str,
        users: list,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @formation
    def join(
        self,
        channel: str,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @formation
    def kick(
        self,
        channel: str,
        user: str,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @formation
    def leave(
        self,
        channel: str,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    def list(
        self,
        cursor: str = None,
        exclude_archived: bool = False,
        limit: int = 100,
        types: list = None
    ):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    def members(
        self,
        channel: str,
        cursor: str = None,
        limit: int = 100,
    ):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    @formation
    def open(
        self,
        channel: str = None,
        return_im: bool = None,
        users: list = None,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @formation
    def rename(
        self,
        channel: str,
        name: str,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    def replies(
        self,
        channel: str,
        ts: float,
        cursor: str = None,
        inclusive: bool = False,
        latest: str = "now",
        limit: int = 100,
        oldest: float = 0
    ):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    @formation
    def set_purpose(
        self,
        channel: str,
        purpose: str,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @formation
    def set_topic(
        self,
        channel: str,
        topic: str,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @formation
    def unarchive(
        self,
        channel: str = None,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)
