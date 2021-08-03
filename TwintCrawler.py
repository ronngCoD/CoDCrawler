import twint
import json

def scrape(keyword, limit):
    with open('data/' + keyword + '.txt', 'w', encoding='utf-8') as f:
        # configuration
        config = twint.Config()
        config.Search = keyword
        config.Lang = "en"
        config.Limit = limit
        config.Store_object = True
        tweets = twint.output.tweets_list
        # running search
        twint.run.Search(config)
        f.write(tweets)

if __name__ == "__main__":
    searchWord = '#payup'
    scrape(searchWord, limit=200)

