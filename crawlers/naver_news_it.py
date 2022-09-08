import os
import sys

sys.path.insert(0, "../")

from typing import Dict, Tuple
from typing import Any
from base_crawler import BaseCrawler
from selenium.webdriver.common.by import By


class NaverNewsIt(BaseCrawler):
    def pre_process(self, *args: Tuple[Any], **kwargs: Dict[Any, Any]) -> Any:
        # 파라메터로 받은 url 로 이동
        self.driver.get(self.url)

    def _run_crawler_impl(self, *args: Tuple[Any], **kwargs: Dict[Any, Any]) -> Any:
        content_a_tags = self.driver.find_elements(By.XPATH, '//*[@id="main_content"]/div[2]/ul[1]/li/dl/dt[2]/a')
        for v in content_a_tags:
            print(v.get_attribute("href"))
        return super()._run_crawler_impl()

    def post_process(self, *args: Tuple[Any], **kwargs: Dict[Any, Any]) -> Any:
        self.driver.close()
        pass
        # return super().post_process()


if __name__ == "__main__":
    crawler = NaverNewsIt("https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230")
    crawler.run_crawler()
