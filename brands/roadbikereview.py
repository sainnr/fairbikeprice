from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
from brands.Brand import Brand


def get_url(url):
    """
    GET an HTTP URL
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if resp.status_code == 200:
                return resp.content
            else:
                return None

    except RequestException as e:
        print('Error requesting {0}, reason: {1}'.format(url, str(e)))
        return None


def get_review_brands():
    print('Getting bike brands')

    target = 'https://www.roadbikereview.com/latest-bikes.html'
    response = get_url(target)
    brands = set()

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        main_div = html.find('div', attrs={'class': 'golf-club-list-items'})

        if main_div is not None:
            for a in main_div.select('a'):
                print(a.string)
        else:
            print('No main div found!')

    return brands
