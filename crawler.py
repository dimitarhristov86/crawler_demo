import requests
from bs4 import BeautifulSoup

# pass web page url
url = "https://www.autokelly.bg/bg/products/43758570.html?ids=39849642;51224611"

# set variable for document
html = "./html_data/motor_oils.html"

# create request(url=url, escaping SSL Certificate)
r = requests.get(url, verify=False)

# set encoding of page
r.encoding = "utf-8"

# set variable for html text
content = r.text

# save html text of the response
with open(html, 'w') as f:
    f.write(content)

# create a list
links = []

# loop through all a tags
for link in BeautifulSoup(content).find_all('a', href=True):

    # add just the href tags to a list(links)
    links.append(link['href'])

# loop through all href tags to check what returns web crawler
for link in links:
    print(link)

