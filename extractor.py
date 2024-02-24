import requests
from bs4 import BeautifulSoup

class ArticlesExtractor:
    def __init__(self, urls, category='tecnologia'):
        self.urls = urls
        self.category = category

    def extract_articles(self):
        articles_result = {'artigos': []}
        
        for url in self.urls:
            try:
                response = requests.get(url, timeout=10)
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    if self.category == 'tecnologia':
                        self.parse_tecnologia_articles(url, soup, articles_result)
            except requests.RequestException as e:
                print(f"Request failed for {url}: {e}")
                
        return articles_result

    def parse_tecnologia_articles(self, url, soup, articles_result):
        if 'cnet.com' in url:
            articles = soup.select('.c-storiesLatest_content > a')
            for article in articles:
                title_element = article.find('h3')
                link = article.get('href')
                if title_element and link:
                    title = title_element.text.strip()
                    articles_result['artigos'].append({'title': title, 'link': 'https://www.cnet.com' + link})

        elif 'g1.globo.com/tecnologia' in url:
            articles = soup.select('.feed-post-body')
            for article in articles:
                title_element = article.find('a', class_='feed-post-link')
                if title_element:
                    title = title_element.text.strip()
                    link = title_element.get('href')
                    articles_result['artigos'].append({'title': title, 'link': link})

