import requests
import time

API_key="bf0aa31f0d154dd79d2a1b940f2782f7" # enter your api key here
Base_url="https://newsapi.org/v2/everything"
date="2025-03-02"  # try date one day before of current date if api is not updated with latest news
#yyyy-mm-dds

def fetch_news(query):
    url=f"{Base_url}?q={query}&from={date}&sortBy=publishedAt&apiKey={API_key}"
    
    try:
        response=requests.get(url) # get response from the api first
        data=response.json() # filter response data with json as an dict
        
        # data looks like that"
        # {
#   "status": "ok",
#   "totalResults": 1234,
#   "articles": [
#     {
#       "source": {"id": "cnn", "name": "CNN"},
#       "author": "John Doe",
#       "title": "Tesla launches new model",
#       "description": "Tesla's new model...",
#       "url": "https://example.com",
#       "publishedAt": "2025-02-03T12:00:00Z"
#     }
#   ]
# }
        
        # check that our req is sucessfull or not
        if response.status_code != 200 or data.get("status")!="ok":
            print(f"Error: {data.get('message','Unable to fetch news')}")# try to find msg in data dict and if unable to find print default as unable to fetch news
            return
        
        articles = data.get("articles", []) # fetch articles from dict (data) default is empty list
        if not articles: # if empty list found as default value
            print("No articles found.")
            return

        print("\n--- Latest News ---\n")
        for i, article in enumerate(articles[:5], start=1):  # Display top 5 articles
            print(f"{i}. {article['title']}")
            print(f"   Source: {article['source']['name']}")
            print(f"   Published: {article['publishedAt']}")
            print(f"   URL: {article['url']}\n")

    except requests.exceptions.RequestException as e:
        print(f"Network error: {e}")

if __name__ == "__main__":
    topic = input("Enter a topic to search for news: ")
    fetch_news(topic)
    



# Author : Jenis Surani
# Topic  : News App
# Date   : 03/03/2025