import requests
from bs4 import BeautifulSoup


def get_content():
    url = input('enter a url:')
    resp = requests.get(url)
    return resp.text


def execute():
    content = get_content()
    web_scrapper = BeautifulSoup(content, 'lxml')

    scrapped_external_link = web_scrapper.find_all('a', target='_blank')

    found_link = False
    for i, link in enumerate(scrapped_external_link, 1):
        found_link = True
        print(f'{i}. {link}')

    if not found_link:
        print('No external links are found')


execute()

