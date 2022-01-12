import json
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route("/")
def index():
    """初期画面を表示します."""
    return render_template("index.html")

@app.route("/api/recommend_article")
def api_recommend_article():
    """はてブのホットエントリーから記事を入手して、ランダムに1件返却します."""
    with urlopen("http://feeds.feedburner.com/hatena/b/hotentry") as res:
        html = res.read().decode("utf-8")
    soup = BeautifulSoup(html, "html.parser")
    items = soup.select("item")
    shuffle(items)
    item = items[0]
    print(item)
    return json.dumps({
        "content" : item.find("title").string,
        # "link" : item.find("link").string
        "link": item.get('rdf:about')
    })

if __name__ == "__main__":
    app.run(debug=True, port=5003)
