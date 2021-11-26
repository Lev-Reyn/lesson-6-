import requests
from bs4 import BeautifulSoup

url = 'https://www.maxidom.ru/catalog/kruzhki/'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.85 YaBrowser/21.11.0.2015 Yowser/2.5 Safari/537.36',
    'accept': '*/*'
}


def parse(url):
    r = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(r.text, 'html.parser')
    items = soup.find_all('article', class_='item-list group')
    for item in items:
        item: BeautifulSoup
        name = item.find('a', class_='name-big').text.strip()
        link = 'https://www.maxidom.ru' + item.find('a', class_='name-big')['href']
        price = item.find('span', class_='price-list').find('span').text.strip()[:-2]

        print(price)


if __name__ == '__main__':
    for i in range(1, 46):
        url = f'https://www.maxidom.ru/catalog/kruzhki/?amount=12&PAGEN_3={i}'
        parse(url)
        print(f'спарсили {i} страниц из 45')
