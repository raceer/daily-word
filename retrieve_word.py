from bs4 import BeautifulSoup
import requests

class TextParser:
    def __init__(self, url):
        self.soup = self.get_website(url)
        sublink = self.get_right_url(url)
        self.soup = self.get_website(sublink)
        
    def get_website(self, url):
        html_website = requests.get(url).text
        return BeautifulSoup(html_website, features="html.parser")

    def get_right_url(self, url):
        for link in self.soup.find_all('a'):
            if "koko" in str(link):
                link = str(link)
                idx1 = link.find('"')
                idx2 = link.find('"', idx1 + 1)
                sublink = link[idx1 + 1:idx2]
        return url[:url.rfind("/") + 1] + sublink

    def get_daily_word(self):
        word = self.soup.find("h1")
        explanation = self.soup.select_one("li p")
        example = self.soup.select_one("li em")
        return list(map(lambda x: x.string, [word, explanation, example]))

if __name__ == "__main__":
    parser = TextParser("https://www.suomisanakirja.fi/paivan.php")
    print(parser.get_daily_word())


