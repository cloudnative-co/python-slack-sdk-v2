# -*- coding: utf-8 -*-
# import module snippets
import io
import sys
import datetime
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Chat(Base):
    """
    @namespace  Slack
    @class      Chat
    @brief      Slackチャットメッセージ操作用クラス
    """

    class ScheduledMessages(Base):
        """
        @namespace  Slack
        @class      ScheduledMessages
        @brief      Slack予約メッセージ一覧クラス
        """

        path = {
            "list": "chat.scheduledMessages.list"
        }

        @formation
        def list(
            self, channel: str = None,
            cursor: str = None,
            latest: str = None,
            limit: int = None,
            oldest: datetime.datetime = None,
            payload: dict = None
        ):
            path = self.path[sys._getframe().f_code.co_name]
            return self.http_request(method="post", path=path, payload=payload)

    path = {
        "delete": "chat.delete",
        "delete_scheduled_message": "chat.deleteScheduledMessage",
        "get_permalink": "chat.getPermalink",
        "me_message": "chat.meMessage",
        "post_ephemeral": "chat.postEphemeral",
        "post_message": "chat.postMessage"
    }

    __scheduled_messages = None

    @formation
    def delete(
        self, channel: str, ts: str, as_user: bool = False,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @formation
    def delete_scheduled_message(
        self, channel: str, scheduled_message_id: str,
        as_user: bool = False, payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    def get_permalink(self, channel: str, message_ts: str):
        path = self.path[sys._getframe().f_code.co_name]
        query = get_arguments(locals())
        return self.http_request(method="get", path=path, query=query)

    @formation
    def me_message(self, channel: str, text: str, payload: dict = None):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @formation
    def post_ephemeral(
        self, channel: str, text: str, user: str, attachments: dict = None,
        as_user: bool = None, blocks: dict = None, icon_emoji: str = None,
        icon_url: str = None, link_names: bool = None, parse: str = None,
        thread_ts: float = None, username: str = None,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @formation
    def post_message(
        self, channel: str, text: str, as_user: bool = None,
        attachments: dict = None, blocks: dict = None, icon_emoji: str = None,
        icon_url: str = None, link_names: bool = None, mrkdwn: bool = None,
        parse: str = None, reply_broadcast: bool = None, thread_ts: str = None,
        unfurl_links: bool = None, unfurl_media: bool = None,
        username: str = None, payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @formation
    def schedule_message(
        self, channel: str, post_at: datetime.datetime, text: str,
        as_user: bool = None, attachments: dict = None, blocks: dict = None,
        link_names: bool = None, parse: str = None,
        reply_broadcast: bool = None, thread_ts: str = None,
        unfurl_links: bool = None, unfurl_media: bool = None,
        payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @formation
    def schedule_message(
        self, channel: str, ts: float, unfurls: str,
        user_auth_message: str = None, user_auth_required: str = None,
        user_auth_url: str = None, payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @formation
    def update_message(
        self, channel: str, text: str, ts: str, as_user: bool = False,
        attachments: dict = None, blocks: dict = None, link_names: bool = True,
        parse: str = None, payload: dict = None
    ):
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="post", path=path, payload=payload)

    @property
    def scheduled_messages(self):
        if self.__scheduled_messages is None:
            self.__scheduled_messages = self.__class__.ScheduledMessages(
                client=self
            )
        return self.__scheduled_messages
