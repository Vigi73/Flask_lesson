import requests
from pprint import pprint
from bs4 import BeautifulSoup as BS

BASE_URL = 'https://www.python.org/blogs/'


def get_html(url):
    try:
        res = requests.get(url)
        res.raise_for_status()
        res.encoding = 'utf-8'
        return res.text
    except(requests.RequestException, ValueError):
        return False


def get_python_news():
    html = get_html(BASE_URL)
    if html:
        soup = BS(html, 'html.parser')
        all_news = soup.find('ul', {'class': 'list-recent-posts'}).find_all('li')
        result_news = []
        for news in all_news:
            title = news.h3.text
            url = news.a['href']
            data = news.p.text
            result_news.append(
                {
                    'title': title,
                    'url': url,
                    'published': data
                }
            )
        return result_news
    return False

