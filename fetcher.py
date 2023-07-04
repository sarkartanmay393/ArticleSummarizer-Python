import requests
from newspaper import Article


def Fetcher(article_url="https://labs.hakaioffsec.com/nginx-alias-traversal/"):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    session = requests.Session()

    try:
        response = session.get(article_url, headers=headers, timeout=10)
        if response.status_code == 200:
            article = Article(article_url)
            article.download()
            article.parse()

            return article

            # print(article.title + "\n")
            # print(article.text)
        else:
            print("Error fetching article url")

    except Exception as e:
        print("Error occured while fetching the news article")
