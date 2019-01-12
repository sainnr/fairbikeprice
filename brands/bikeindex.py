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


def get_index_brands():
    print('Getting bike brands')

    target = 'https://bikeindex.org/manufacturers'
    response = get_url(target)
    brands = set()

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        main_table = html.find('table', attrs={'id': 'manufacturers-list'})

        if main_table is not None:
            for row in main_table.select('tr'):
                ch = row.find_all('td')
                ch1 = ch[0]
                ch2 = ch[1]
                # print('%s %s' % (ch1, ch2))

                if ch2 != '&#x2713;':
                    left = ch1.a
                    href = ''

                    if left is None:
                        name = ch1.string.strip()
                    else:
                        href = left['href']
                        name = left.string.strip()

                    print('%s %s' % (name, href))
        else:
            print('No main table found!')

    return brands
