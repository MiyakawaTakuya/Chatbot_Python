import json
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template
from bs4 import BeautifulSoup
import re
from pprint import pprint
#seleniumを使う場合
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


app = Flask(__name__)

@app.route("/")
def index():
    """初期画面を表示します."""
    return render_template("index.html")

@app.route("/api/recommend_article")
def api_recommend_article():
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

@app.route("/api/zukan_pokemon")
def api_pokemon_name():
    CHROMEDRIVER = "/Users/miyagawatakuya/Documents/chrome/chromedriver"
    browser = webdriver.Chrome(CHROMEDRIVER)
    browser.get("https://zukan.pokemon.co.jp/")
    html = browser.page_source.encode('utf-8')
    soup = BeautifulSoup(html, "html.parser")
    names = soup.find_all('p', class_="name__loadItem")
    browser.quit()
    names = [t.string for t in names]
    return json.dumps({
        "content" : names[3],
        # "link" : item.find("link").string
#        "link": item.get('rdf:about')
    })
#TODO 名前をランダムに取り出して詳細リンクを引っ張り出してretrunする


if __name__ == "__main__":
    app.run(debug=True, port=5004)
    #app.run(debug=True, port=5000)
