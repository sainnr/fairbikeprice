from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup


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


if __name__ == '__main__':
    print('Getting bike brands')

    target = 'https://www.roadbikerider.com/list-of-bike-brands-from-a-to-z/'
    response = get_url(target)

    if response is not None:
        html = BeautifulSoup(response, 'html.parser')
        main_div = html.find('div', attrs={'class': 'entry-content'})

        if main_div is not None:
            brands = set()
            for ps in main_div.select('p'):
                ch = list(ps.children)
                if len(ch) >= 3:
                    b_raw = [c.string.replace('\n', '').replace('\xa0', ' ').strip() for c in ch
                             if c.name != 'br' and c.string is not None]
                    b_filtered = [b for b in b_raw if len(b) > 0]
                    print(b_filtered)
        else:
            print('No main div found!')
