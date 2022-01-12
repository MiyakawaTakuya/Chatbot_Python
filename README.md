# チャットボットニュース
これはPython講義のデモアプリの1つで、 `Flask`と `BeautifulSoup`の練習課題です.  
声で話しかけると、Webスクレイピングを行い、最近話題のオススメ記事を1つ教えてくれます.  
***
![チャットボットニュース](https://raw.githubusercontent.com/yoheimune-python-lecture/chatbot-news/image/resources/screenshot.png)
[デモはこちら](http://demo-chatbot-news.paint-ink.com/)  


# 演習の準備
以下の手順で演習を進めることができます。
## レポジトリの取得
以下の要領で、レポジトリを取得してローカルにソースコードを持ってきます.
```
$ git clone https://github.com/yoheimune-python-lecture/chatbot-news.git
```
## 必要ライブラリのインストール
`Flask`と `BeautifulSoup` を使うのでそれらを `pip`でインストールします.
```
$ pip3 install --upgrade flask
$ pip3 install --upgrade beautifulsoup4
```
## 起動確認
まずは起動してみて動くことを確認します.
```
$ cd practice
$ python3 app.py
```
以下のURLでアクセス可能です。
```
http://localhost:5004
```

# 基礎課題
この演習では、Flaskアプリケーション上でWebスクレイピングを行う部分を実装します。修正するプログラムは以下です。  
- app.py

app.py内の以下の箇所で、Webスクレイピングを実装してください。
```python
@app.route("/api/recommend_article")
def api_recommend_article():
    """はてブのホットエントリーから記事を入手して、ランダムに1件返却します."""

    """
        **** ここを実装します ****

        1. はてブのホットエントリーページのHTMLを取得する
        2. BeautifulSoupでHTMLを読み込む
        3. 記事一覧を取得する
        4. ランダムに1件取得する
        5. 以下の形式で返却する.
            {
                "content" : "記事のタイトル",
                "link" : "記事のURL"
            }
    """

    # ダミー
    return json.dumps({
        "content" : "記事のタイトルだよー",
        "link" : "記事のURLだよー"
    })
```
無事に動くことを祈っています！！！  

# 発展課題
上記が完成しましたら、さらに他のWebスクレイピングにもチャレンジしてみてください。例えば以下などはいかがでしょうか？
* 明日の天気を取得する  
* 今日の晩御飯をお勧めしてくれる  

# 課題の答え
課題の答えは、以下のディレクトリにありますので、適宜ご確認ください。  

[課題の答えはこちら](https://github.com/yoheimune-python-lecture/chatbot-news/tree/master/answer)  
