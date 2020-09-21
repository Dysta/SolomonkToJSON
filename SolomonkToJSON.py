import json
import re
import parseStuff

from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from pprint import pprint

BASE_URL: str   = "https://solomonk.fr/fr/"
USER_AGENT: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"


def parse_stuff(url: str) -> dict:
    print(f'parsing url : {url}')
    headers: dict = {}
    headers['User-Agent'] = USER_AGENT
    req: Request = Request(url, headers=headers)
    html: str = urlopen(req, timeout=3.0).read()
    parsed_html: BeautifulSoup = BeautifulSoup(html, "html.parser")

    item_data: dict = {}
    item_data['id']          = int(re.search(r'\d+', url).group())
    item_data['name']        = parseStuff.parse_name(parsed_html)
    item_data['effect']      = parseStuff.parse_effect(parsed_html)
    item_data['condition']   = parseStuff.parse_condition(parsed_html)
    item_data['recipe']      = parseStuff.parse_recipe(parsed_html)
    item_data['description'] = parseStuff.parse_description(parsed_html)

    return item_data


def parse_monster(url):
    pass


def check_url(url: str) -> bool:
    if url == "": return False
    if not url.startswith(BASE_URL): return False
    return True


def parse_url(url: str) -> dict:
    if "equipement" in url:
        return parse_stuff(url)
    if "monstre" in url:
        return parse_monster(url)

    return ""


if __name__ == "__main__":
    url: str = "https://solomonk.fr/fr/equipement/6660/chapeau-du-marie"
    if check_url(url):
        data: dict = parse_url(url)
        pprint(data)
        #with open(f"out/{data['id']}.json", "w") as f:
        #    f.write(json.dumps(data))
    else:
        raise Exception('Incorrect url')
