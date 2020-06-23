# -*- coding: utf-8 -*-
# import module snippets
from .base import Base
from .api import Api
from .apps import Apps
from .auth import Auth
from .bots import Bots
from .calls import Calls
from .chat import Chat
from .conversations import Conversations
from .dialog import Dialog
from .dnd import Dnd
from .emoji import Emoji
from .files import Files
from .migration import Migration
from .oauth import OAuth
from .pins import Pins
from .reactions import Reactions
from .reminders import Reminders
from .rtm import Rtm
from .stars import Stars
from .team import Team
from .users import Users
from .usergroups import UserGroups
from .views import Views


class Client(Base):
    _api: Api = None
    _apps: Apps = None
    _bots: Bots = None
    _calls: Calls = None
    _conv: Conversations = None
    _dialog: Dialog = None
    _dnd: Dnd = None
    _emoji: Emoji = None
    _files: Files = None
    _mig: Migration = None
    _oauth: OAuth = None
    _pins: Pins = None
    _react: Reactions = None
    _remind: Reminders = None
    _rtm: Rtm = None
    _stars: Stars = None
    _team: Team = None
    _users: Users = None
    _u_grs: UserGroups = None
    _views: Views = None

    @property
    def api(self):
        self._api = self._api if self._api else Api(client=self)
        return self._api

    @property
    def apps(self):
        self._apps = self._apps if self._apps else Apps(client=self)
        return self._apps

    @property
    def auth(self):
        self._auth = self._auth if self._auth else Auth(client=self)
        return self._auth

    @property
    def bots(self):
        self._bots = self._bots if self._bots else Bots(client=self)
        return self._bots

    @property
    def calls(self):
        self._calls = self._calls if self._calls else Calls(client=self)
        return self._calls

    @property
    def chat(self):
        self._chat = self._chat if self._chat else Chat(client=self)
        return self._chat

    @property
    def conversations(self):
        self._conv = self._conv if self._conv else Conversations(client=self)
        return self._conv

    @property
    def dialog(self):
        self._dialog = self._dialog if self._dialog else dialog(client=self)
        return self._dialog

    @property
    def dnd(self):
        self._dnd = self._dnd if self._dnd else Dnd(client=self)
        return self._dnd

    @property
    def emoji(self):
        self._emoji = self._emoji if self._emoji else Emoji(client=self)
        return self._emoji

    @property
    def files(self):
        self._files = self._files if self._files else Files(client=self)
        return self._files

    @property
    def migration(self):
        self._mig = self._mig if self._mig else Migration(client=self)
        return self._mig

    @property
    def oauth(self):
        self._oauth = self._oauth if self._oauth else OAuth(client=self)
        return self._oauth

    @property
    def pins(self):
        self._pins = self._pins if self._pins else Pins(client=self)
        return self._pins

    @property
    def reactions(self):
        self._react = self._react if self._react else Reactions(client=self)
        return self._react

    @property
    def reminders(self):
        self._remind = self._remind if self._remind else Reminders(client=self)
        return self._remind

    @property
    def rtm(self):
        self._rtm = self._rtm if self._rtm else Rtm(client=self)
        return self._rtm

    @property
    def stars(self):
        self._stars = self._stars if self._stars else Stars(client=self)
        return self._stars

    @property
    def team(self):
        self._team = self._team if self._team else Team(client=self)
        return self._team

    @property
    def users(self):
        self._users = self._users if self._users else Users(client=self)
        return self._users

    @property
    def usergroups(self):
        self._u_grs = self._u_grs if self._u_grs else UserGroups(client=self)
        return self._u_grs

    @property
    def views(self):
        self._views = self._views if self._views else Views(client=self)
        return self._views
