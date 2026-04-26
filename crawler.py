import requests
from bs4 import BeautifulSoup
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RSS_URL = "https://news.google.com/rss?hl=ko&gl=KR&ceid=KR:ko"
MAX_ITEMS = 10


def parse_description(raw_description: str) -> str:
    if not raw_description:
        return "요약 없음"
    return BeautifulSoup(raw_description, "html.parser").get_text(" ", strip=True)


def fetch_rss(url: str):
    response = requests.get(url, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "xml")
    return soup.find_all("item")[:MAX_ITEMS]


def print_items(items):
    if not items:
        print("가져온 뉴스가 없습니다.")
        return

    print(f"총 {len(items)}건 뉴스\n")

    for idx, item in enumerate(items, start=1):
        title = item.title.get_text(strip=True) if item.title else "제목 없음"
        link = item.link.get_text(strip=True) if item.link else "링크 없음"
        pub_date = item.pubDate.get_text(strip=True) if item.pubDate else "발행시간 없음"
        description_raw = item.description.get_text(strip=True) if item.description else ""
        description = parse_description(description_raw)

        print(f"[{idx}] {title}")
        print(f"발행시간: {pub_date}")
        print(f"링크: {link}")
        print(f"요약: {description}")
        print("-" * 80)


def main():
    try:
        items = fetch_rss(RSS_URL)
        print_items(items)
    except requests.RequestException as e:
        print(f"RSS 요청 중 오류가 발생했습니다: {e}")


if __name__ == "__main__":
    main()
