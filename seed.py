import os
import sqlite3

import crawler

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.environ.get("DB_PATH", os.path.join(BASE_DIR, "board.db"))


def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_posts_table(conn):
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()


def seed_posts():
    items = crawler.fetch_rss(crawler.RSS_URL)

    conn = get_db_connection()
    init_posts_table(conn)

    fetched_count = len(items)
    skipped_count = 0
    inserted_count = 0

    for item in items:
        title = item.title.get_text(strip=True) if item.title else "제목 없음"
        link = item.link.get_text(strip=True) if item.link else "링크 없음"
        pub_date = item.pubDate.get_text(strip=True) if item.pubDate else "발행시간 없음"
        description_raw = item.description.get_text(strip=True) if item.description else ""
        summary = crawler.parse_description(description_raw)

        exists = conn.execute(
            "SELECT 1 FROM posts WHERE title = ? LIMIT 1",
            (title,),
        ).fetchone()
        if exists:
            skipped_count += 1
            continue

        content = f"{summary}\n\n링크: {link}\n발행시간: {pub_date}"
        conn.execute(
            "INSERT INTO posts (title, content) VALUES (?, ?)",
            (title, content),
        )
        inserted_count += 1

    conn.commit()
    conn.close()

    print(f"가져온 뉴스: {fetched_count}건")
    print(f"중복으로 건너뜀: {skipped_count}건")
    print(f"추가됨: {inserted_count}건")


if __name__ == "__main__":
    seed_posts()
