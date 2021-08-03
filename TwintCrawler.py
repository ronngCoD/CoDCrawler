import twint
import json

def scrape(keyword, limit):
    # configuration
    config = twint.Config()
    config.Search = keyword
    config.Lang = "en"
    config.Limit = limit

    config.Store_object = True
    # running search
    twint.run.Search(config)
    tweets = twint.output.tweets_list
    print(tweets)
    #with open('data/' + keyword + '.txt', 'w', encoding='utf-8') as f:

       # f.write(json.dumps(tweets) + '\n')

if __name__ == "__main__":
    scrape('#payup', 10)


