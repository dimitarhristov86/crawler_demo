import requests
from bs4 import BeautifulSoup


class Crawler:
    def __init__(self, seed):
        self.seed = seed
        self.urls_to_visit = [seed]
        self.visited_urls = []

    def run(self):
        for url in self.urls_to_visit:
            try:
                self.get_html_content(url)

                self.visited_urls.append(url)
                self.urls_to_visit.remove(url)
            except:


    def get_html_content(self, url):
        try:
            # create request(se     ed=seed, escaping SSL Certificate)
            response = requests.get(url, verify=False)

            # set encoding of page
            response.encoding = "utf-8"

            # set variable for html text
            content = response.text
            return content
        except requests.RequestException as error:
            print(error)

    def save_content_to_file(self):

        # set variable for document
        html = "../../html_data/motor_oils.html"

    def get_links_from_html(self):
        pass


crawler = Crawler("https://www.autokelly.bg/bg/products/43758570.html?ids=39849642;51224611")




# save html text of the response
with open(html, 'w') as f:
    f.write(content)

# create a list
links = []

# loop through all a tags
for link in BeautifulSoup(content, features='html.parser').find_all('a', href=True):
    # add just the href tags to a list(links)
    if '/bg/autokelly/item/' in link['href']:
        links.append(link['href'])

# loop through all href tags to check what returns web crawler
for link in links:
    print(link)

#



