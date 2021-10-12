import requests
from bs4 import BeautifulSoup

url = "https://www.autokelly.bg/bg/products/43758570.html?ids=39849642;51224611"
html = "./html_data/motor_oils.html"
r = requests.get(url, verify=False)
r.encoding = "utf-8"
content = r.text
with open(html, 'w') as f:
    f.write(content)

links = []
for link in BeautifulSoup(content).find_all('a', href=True):
    links.append(link['href'])
for link in links:
    print(link)

