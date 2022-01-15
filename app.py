
from urllib.request import urlopen
from random import shuffle
from flask import Flask, render_template
from bs4 import BeautifulSoup
import re
from pprint import pprint
import requests
import json
import time
import lxml
# import chromedriver_binary
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
    # return html
    soup = BeautifulSoup(html, "html.parser")
    items = soup.select("item")
    shuffle(items)
    item = items[0]
    return json.dumps({
        "content" : item.find("title").string, #titleはHTMLタグの名前
        "link": item.get('rdf:about')
    })

@app.route('/api/pokemon_details')
def api_pokemon_name():
    # opts = Options()
    # opts.headless = True
    driver = webdriver.Chrome("/Users/miyagawatakuya/Documents/chrome/chromedriver")
    driver.get("https://zukan.pokemon.co.jp/")
    html = driver.page_source.encode('utf-8')
    # time.sleep(5)
    soup = BeautifulSoup(html, "lxml")
    # time.sleep(3)
    a = soup.find_all('a', class_="link__loadtItem")
    a_array = [t.string for t in a]
    # shuffle(a_array)
    a_ = a_array[0]
    # name = a_.find("p", class_="name__loadItem").text
    # pprint(name)
    link = "https://zukan.pokemon.co.jp" + a_.get('href') 
    # driver.quit()
    return json.dumps({
        "content" : "たくやのGithub",
        "link": link
    })


if __name__ == "__main__":
    app.run(debug=True, port=5004)

# =============================================================================
# @app.route('/api/pokemon_details')
# def api_pokemon_name():
#     CHROMEDRIVER = "/Users/miyagawatakuya/Documents/chrome/chromedriver"
#     # browser = webdriver.Chrome(CHROMEDRIVER)
#     # browser.get("https://zukan.pokemon.co.jp/")
#     # html = browser.page_source.encode('utf-8')
#     # html = browser.page_source
#     # html = browser.read().decode("utf-8")
#     # return browser.page_source
#     driver = webdriver.Chrome(CHROMEDRIVER)
#     # opts = Options()
#     # opts.headless = True
#     # driver = webdriver.Chrome(options=opts)
#     driver.get("https://zukan.pokemon.co.jp/")
#     ##Seleniumからブラウザを操作して出力された目的のページのHTML
#     html = driver.page_source.encode('utf-8')
#     ##Beautifulsoup4でHTMLの中身の構造を解析
#     soup = BeautifulSoup(html, "lxml")
#     # soup = BeautifulSoup(html, "html.parser")
#     return soup
#     # return soup
#     # li = soup.find_all('a', class_="link__loadtItem")
#     # li = [t.string for t in li]
#     # shuffle(li)
#     # li_ = li[0]
#     # return li_
#     # print(li_)
#     # # a = li_.find("p", class_="name__loadItem").string  #.textを入れるべき？
#     # a = li_.find(class_="name__loadItem").string
#     # link = "https://zukan.pokemon.co.jp" + li_.get('href') 
#     # browser.quit()
#     # return json.dumps({
#     #     "content" : a,
#     #     "link": link
#     # })
# =============================================================================
    



# 文字列をバイト列に変換するには encode メソッドを使用
# バイト列を文字列に変換するには decode メソッド

# =============================================================================
# @app.route('/api/pokemon_details')
# def api_pokemon_name():
#     with urlopen("https://zukan.pokemon.co.jp/") as res:
#         html = res.read().decode("utf-8")
#     time.sleep(7)
#     soup = BeautifulSoup(html, "html.parser")
#     time.sleep(7)
#     li = soup.find_all('a', class_="link__loadtItem")
#     li = [t.string for t in li]
#     shuffle(li)
#     li_ = li[0]
#     return li_
# =============================================================================

    # .find("a").get_attribute("textContent")



