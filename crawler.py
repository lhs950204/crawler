from typing import Any
from typing_extensions import Literal
from selenium import webdriver
from utils import logger_wrapper

OS_TYPES = Literal["mac", "window", "m1", "linux"]


class BaseCrawler(object):
    def __init__(self, url: str, os_type: OS_TYPES = "mac") -> None:
        self.url = url
        self.driver = self.load_selenium(os_type)

    def load_selenium(self, os_type: OS_TYPES) -> webdriver.Chrome:
        if os_type == "mac":
            driver_path = "./drivers/chromedriver_mac_64"
        elif os_type == "window":
            driver_path = "./drivers/chromedriver_win_32.exe"
        elif os_type == "linux":
            driver_path = "./drivers/chromedriver_mac_64"
        else:
            assert os_type == "m1", "올바르지 않은 os type 입니다."
            driver_path = "./drivers/chromedriver_mac_m1"

        driver = webdriver.Chrome(driver_path)
        return driver

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
