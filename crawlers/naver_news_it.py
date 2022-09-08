import sys
import pandas as pd


sys.path.insert(0, "../")

from typing import Dict, List, Tuple
from typing import Any
from base_crawler import BaseCrawler
from utils import logger_wrapper
from selenium.webdriver.common.by import By


class NaverNewsIt(BaseCrawler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.items: List[Dict[str, str]] = []

    @logger_wrapper
    def pre_process(self, *args: Tuple[Any], **kwargs: Dict[Any, Any]) -> Any:
        # 파라메터로 받은 url 로 이동
        self.driver.get(self.url)

    def _run_crawler_impl(self, *args: Tuple[Any], **kwargs: Dict[Any, Any]) -> Any:
        content_a_tags = self.driver.find_elements(By.XPATH, '//*[@id="main_content"]/div[2]/ul[1]/li/dl/dt[2]/a')
        urls = [v.get_attribute("href") for v in content_a_tags]
        for url in urls:
            self.driver.get(url)
            title = self.driver.find_element(By.XPATH, '//*[@id="ct"]/div[1]/div[2]/h2')
            content = self.driver.find_element(By.ID, "dic_area")
            self.items.append(
                {
                    "url": url,
                    "title": title.text.replace("\n", " ").strip(),
                    "content": content.text.replace("\n", " ").strip(),
                }
            )

    @logger_wrapper
    def post_process(self, *args: Tuple[Any], **kwargs: Dict[Any, Any]) -> Any:
        self.driver.close()
        df = pd.DataFrame.from_records(self.items)
        df.to_csv("result.tsv", sep="\t", index=False)


if __name__ == "__main__":
    crawler = NaverNewsIt("https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230")
    crawler.run_crawler()
