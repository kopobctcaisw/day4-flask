import os
from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.jinja_env.filters["korean_date"] = lambda s: datetime.strptime(s, "%Y-%m-%d %H:%M:%S").strftime("%Y년 %m월 %d일") if isinstance(s, str) else s.strftime("%Y년 %m월 %d일")
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "board.db")


def get_db():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS posts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)
    conn.commit()
    conn.close()


init_db()


@app.route("/")
def post_list():
    per_page = 10
    try:
        page = int(request.args.get("page", "1"))
    except ValueError:
        page = 1
    page = max(1, page)

    search_query = (request.args.get("q") or "").strip()
    sort = (request.args.get("sort") or "latest").strip()
    sort_map = {
        "latest": "created_at DESC",
        "oldest": "created_at ASC",
        "title": "title COLLATE NOCASE ASC",
    }
    order_by = sort_map.get(sort, sort_map["latest"])
    if sort not in sort_map:
        sort = "latest"

    where_clause = ""
    query_params = []
    if search_query:
        like_query = f"%{search_query}%"
        where_clause = " WHERE title LIKE ? OR content LIKE ?"
        query_params = [like_query, like_query]

    conn = get_db()
    total_count = conn.execute(
        f"SELECT COUNT(*) FROM posts{where_clause}",
        query_params,
    ).fetchone()[0]
    total_pages = max(1, (total_count + per_page - 1) // per_page)
    page = min(page, total_pages)
    offset = (page - 1) * per_page

    posts = conn.execute(
        f"SELECT * FROM posts{where_clause} ORDER BY {order_by} LIMIT ? OFFSET ?",
        (*query_params, per_page, offset),
    ).fetchall()
    conn.close()

    return render_template(
        "list.html",
        posts=posts,
        total_count=total_count,
        page=page,
        total_pages=total_pages,
        has_prev=page > 1,
        has_next=page < total_pages,
        prev_page=page - 1,
        next_page=page + 1,
        search_query=search_query,
        sort=sort,
    )


@app.route("/write", methods=["GET", "POST"])
def write_post():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        conn = get_db()
        conn.execute(
            "INSERT INTO posts (title, content) VALUES (?, ?)",
            (title, content),
        )
        conn.commit()
        conn.close()
        return redirect(url_for("post_list"))
    return render_template("write.html")


@app.route("/post/<int:post_id>")
def post_detail(post_id):
    conn = get_db()
    post = conn.execute(
        "SELECT * FROM posts WHERE id = ?", (post_id,)
    ).fetchone()
    conn.close()
    if post is None:
        return redirect(url_for("post_list"))
    return render_template("detail.html", post=post)


@app.route("/post/<int:post_id>/edit", methods=["GET", "POST"])
def edit_post(post_id):
    conn = get_db()
    if request.method == "POST":
        conn.execute(
            "UPDATE posts SET title=?, content=? WHERE id=?",
            (request.form["title"], request.form["content"], post_id),
        )
        conn.commit()
        conn.close()
        return redirect(url_for("post_detail", post_id=post_id))
    post = conn.execute("SELECT * FROM posts WHERE id=?", (post_id,)).fetchone()
    conn.close()
    if post is None:
        return redirect(url_for("post_list"))
    return render_template("write.html", post=post)


@app.route("/post/<int:post_id>/delete", methods=["POST"])
def delete_post(post_id):
    conn = get_db()
    conn.execute("DELETE FROM posts WHERE id=?", (post_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("post_list"))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
