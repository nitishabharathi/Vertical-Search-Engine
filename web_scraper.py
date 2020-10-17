import requests
from bs4 import BeautifulSoup
import re


class WebScraper:
    def __init__(self):
        self.urls = []

    def fetch_url(self, file):
        '''
        Creates a list of URLS to be scraped.
        '''
        f = open(file, 'r')
        for line in f:
            line = line.rstrip()
            self.urls.append(line)

    def state_scraper(self):
        '''
        Scraps State Government Schemes.
        '''

        for state in self.urls:
            i = 1
            s = state
            s = s.split('/')
            state_name = s[3]
            page = requests.get(state)
            soup = BeautifulSoup(page.text, 'html5lib')
            main_content = soup.find_all(class_='inside-article')
            try:
                main_content = main_content[-1]
            except:
                continue
            urls = main_content.findAll(
                'a', attrs={'href': re.compile("^https://sarkariyojana")})
            url = []
            for u in urls:
                url.append(u.get('href'))

            for u in url:
                page = requests.get(u)
                soup = BeautifulSoup(page.text, 'html5lib')
                content = soup.findAll(class_='entry-content')
                try:
                    content = BeautifulSoup(
                        str(content[0]), features="html5lib")
                    content = content.get_text()
                    filename = 'state_' + state_name + \
                        '_doc_' + str(i) + '.txt'
                    with open(filename, 'w', encoding="utf-8") as file1:

                        file1.write(content)
                    i = i + 1
                except:
                    continue

    def central_scraper(self):
        '''
        Scraps Central Government Schemes.
        '''
        page = requests.get(
            "https://sarkariyojana.com/complete-list-schemes-launched-pm-narendra-modi/")
        soup = BeautifulSoup(page.text, 'html5lib')
        main_content = soup.find_all('ol')
        main_content = main_content[0]
        content_split = main_content.find_all('li')

        for i in range(len(content_split)):
            content = BeautifulSoup(str(content_split[i]), features="html5lib")
            content = content.get_text()
            filename = 'central_doc_' + str(i+1) + '.txt'
            with open(filename, 'w', encoding="utf-8") as file1:
                file1.write(content)


if __name__ == "__main__":
    s = WebScraper()
    s.fetch_url('urls.txt')
    s.state_scraper()
    s.central_scraper()
