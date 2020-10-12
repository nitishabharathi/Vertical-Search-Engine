import requests 
from bs4 import BeautifulSoup
import pandas
import os

page = requests.get("https://sarkariyojana.com/complete-list-schemes-launched-pm-narendra-modi/")
soup = BeautifulSoup(page.text, 'html5lib')
main_content = soup.find_all('ol')
main_content = main_content[0]
content_split = main_content.find_all('li')

for i in range(len(content_split)):
     
    content = BeautifulSoup(str(content_split[i]),features="html5lib")
    content = content.get_text()

    filename = 'central_doc_' + str(i+1) +  '.txt'
    with open(filename, 'w',encoding="utf-8") as file1:
            
        file1.write(content)
