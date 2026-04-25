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
    conn = get_db()
    posts = conn.execute(
        "SELECT * FROM posts ORDER BY created_at DESC"
    ).fetchall()
    conn.close()
    return render_template("list.html", posts=posts)


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


if __name__ == "__main__":
    app.run(debug=True)
