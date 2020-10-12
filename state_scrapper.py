import requests 
from bs4 import BeautifulSoup
import pandas
import os
import re

state_urls = ['https://sarkariyojana.com/haryana/','https://sarkariyojana.com/uttar-pradesh/','https://sarkariyojana.com/delhi/','https://sarkariyojana.com/madhya-pradesh/','https://sarkariyojana.com/maharashtra/','https://sarkariyojana.com/odisha/','https://sarkariyojana.com/rajasthan/','https://sarkariyojana.com/andhra-pradesh/','https://sarkariyojana.com/bihar/','https://sarkariyojana.com/chhattisgarh/','https://sarkariyojana.com/punjab/','https://sarkariyojana.com/jharkhand/','https://sarkariyojana.com/karnataka/','https://sarkariyojana.com/himachal-pradesh/','https://sarkariyojana.com/kerala/','https://sarkariyojana.com/gujarat/','https://sarkariyojana.com/tamilnadu/','https://sarkariyojana.com/telangana/','https://sarkariyojana.com/assam/','https://sarkariyojana.com/west-bengal/','https://sarkariyojana.com/uttarakhand/','https://sarkariyojana.com/jammu-kashmir/','https://sarkariyojana.com/goa/','https://sarkariyojana.com/tripura/','https://sarkariyojana.com/manipur/','https://sarkariyojana.com/meghalaya/','https://sarkariyojana.com/chandigarh/','https://sarkariyojana.com/mizoram/']

state_names = []
for state in state_urls:
    i = 1
    s = state
    s = s.split('/')
    state_name = s[3]
    page = requests.get(state)
    soup = BeautifulSoup(page.text, 'html5lib')
    main_content = soup.find_all(class_ = 'inside-article')
    try:
        main_content = main_content[-1]
    except:
        continue
    urls = main_content.findAll('a', attrs={'href': re.compile("^https://sarkariyojana")})
    url = []
    for u in urls:
        url.append(u.get('href'))

    for u in url:
        page = requests.get(u)
        soup = BeautifulSoup(page.text, 'html5lib')
        content = soup.findAll(class_ = 'entry-content')
        try:
            content = BeautifulSoup(str(content[0]),features="html5lib")
            content = content.get_text()
            filename = 'state_' + state_name + '_doc_' + str(i) +  '.txt'
            with open(filename, 'w',encoding="utf-8") as file1:
                    
                file1.write(content)
            i = i + 1
        except:
            continue
