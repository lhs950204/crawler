from typing import Any
import logging
import selenium

from utils import logger_wrapper

logger = logging.getLogger()


class BaseCrawler(object):
    def __init__(self, url: str) -> None:
        self.url = url

    @logger_wrapper
    def pre_process(self) -> Any:
        raise NotImplementedError

    def run_crawler(self) -> Any:
        self.pre_process()
        self._run_crawler_impl()
        self.post_process()

    @logger_wrapper
    def _run_crawler_impl(self) -> Any:
        pass

    @logger_wrapper
    def post_process(self) -> Any:
        raise NotImplementedError
