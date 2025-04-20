# 檔案路徑：web_app.py
from flask import Flask, request, render_template
from db.index_db import IndexDB
from core.inverted_index_searcher import InvertedIndexSearcher

app = Flask(__name__)

# 初始化搜尋器（只做一次）
index_db = IndexDB("test.db")
searcher = InvertedIndexSearcher(index_db)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/search")
def search():
    query = request.args.get("q", "")
    results = searcher.search(query, top_k=3) if query else []
    return render_template("index.html", query=query, results=results)

if __name__ == "__main__":
    app.run(debug=True)
