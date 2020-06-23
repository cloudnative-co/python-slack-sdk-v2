# -*- coding: utf-8 -*-
# import module snippets
import sys
from .base import Base
from .Utilities.utilities import get_arguments
from .Utilities.utilities import formation


class Search(Base):
    """
    @namespace  Slack.search
    @class      Search
    @brief      Slack検索用クラス
    """

    path = {
        "all": "search.all",
        "files": "search.files",
        "messages": "search.messages",
    }

    def all(
        self,
        query: str,
        count: int = 20,
        highlight: bool = None,
        page: int = 1,
        sort: str = "score",
        sort_dir: str = "desc"
    ):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    def files(
        self,
        query: str,
        count: int = 20,
        highlight: bool = None,
        page: int = 1,
        sort: str = "score",
        sort_dir: str = "desc"
    ):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)

    def messages(
        self,
        query: str,
        count: int = 20,
        highlight: bool = None,
        page: int = 1,
        sort: str = "score",
        sort_dir: str = "desc"
    ):
        query = get_arguments(locals())
        path = self.path[sys._getframe().f_code.co_name]
        return self.http_request(method="get", path=path, query=query)
