import requests
from newspaper import Article

# this function takes article URL and return it in Article object.
# I included a default value for the url, it never matters.
def GetNewsArticle(article_url="https://labs.hakaioffsec.com/nginx-alias-traversal/"):

    # Fetches the news article from the given URL

    # header object for the request we have make to article url
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }

    # Create a session object that we can use for calling get, post function with that url.
    session = requests.Session()


    # try catch block
    try:
        # making the request with url, header, and timeout parameter.
        response = session.get(article_url, headers=headers, timeout=10)
        if response.status_code == 200:
            # if response comes with no issues, we make the article object
            # it takes the url and does everything we did using request and session on its own. 
            article = Article(article_url)
            article.download()
            article.parse()

            # after downloading and parsing the data, we're returning it.
            return article
        else:
            # this is just for error checking
            print("Error fetching article url")

    # this is also for error checking
    except Exception as e:
        print("Error occured while fetching the news article")
