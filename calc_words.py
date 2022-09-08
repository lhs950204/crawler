import typer
import pandas as pd
import mecab
from collections import Counter

from crawlers.naver_news_it import NaverNewsIt


def main(
    with_crawling: bool = False,
    os_type: str = "mac",
    result_file: str = "result.tsv",
):
    if with_crawling:
        crawler = NaverNewsIt(
            "https://news.naver.com/main/list.naver?mode=LS2D&mid=shm&sid1=105&sid2=230", os_type=os_type
        )
        crawler.run_crawler()

    mecab_instance = mecab.MeCab()
    df = pd.read_csv(result_file, sep="\t")

    df["title_nouns"] = df["title"].apply(lambda v: mecab_instance.nouns(v))
    df["title_counter"] = df["title_nouns"].apply(lambda v: Counter(v))

    df["content_nouns"] = df["content"].apply(lambda v: mecab_instance.nouns(v))
    df["content_counter"] = df["content_nouns"].apply(lambda v: Counter(v))

    title_counter = Counter()
    for c in df["title_counter"]:
        title_counter.update(c)
    pd.DataFrame.from_dict(title_counter, orient="index").reset_index().rename(
        columns={"index": "word", 0: "count"}
    ).to_csv("title_counter.tsv", "\t", index=False)

    content_counter = Counter()
    for c in df["content_counter"]:
        content_counter.update(c)
    pd.DataFrame.from_dict(content_counter, orient="index").reset_index().rename(
        columns={"index": "word", 0: "count"}
    ).to_csv("content_counter.tsv", "\t", index=False)


if __name__ == "__main__":
    typer.run(main)
