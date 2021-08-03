import twint
import shutil

def scrape(keyword, limit):
    # configuration
    config = twint.Config()
    config.Search = keyword
    config.Lang = "en"
    config.Limit = limit
    config.Store_json = True
    config.Output = keyword + ".txt"
    # running search
    twint.run.Search(config)

if __name__ == "__main__":
    searchWord = '#payyourworkers'
    scrape(searchWord, limit=1000)
    file = searchWord + ".txt"
    original = r'C:\Users\pc-179\PycharmProjects\CoDCrawler\\' + file
    target = r'C:\Users\pc-179\PycharmProjects\CoDCrawler\data'
    shutil.move(original, target)



