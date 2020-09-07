import json
import re

from parseStuff import parse_effect, parse_name
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from pprint import pprint

BASE_URL: str   = "https://solomonk.fr/fr/"
USER_AGENT: str = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"


def parse_stuff(url: str) -> json:
    print(f'parsing url : {url}')
    headers: dict = {}
    headers['User-Agent'] = USER_AGENT
    req: Request = Request(url, headers=headers)
    html: str = urlopen(req, timeout=2.0).read()
    parsed_html: BeautifulSoup = BeautifulSoup(html, "html.parser")

    json_data: dict = {}
    json_data['id']     = int(re.search(r'\d+', url).group())
    json_data['name']   = parse_name(parsed_html)
    json_data['effect'] = parse_effect(parsed_html)

    return json_data


def parse_monster(url):
    pass


def check_url(url: str) -> bool:
    if url == "": return False
    if not url.startswith(BASE_URL): return False
    return True


def parse_url(url: str) -> json:
    if "equipement" in url:
        return parse_stuff(url)
    if "monstre" in url:
        return parse_monster(url)

    return ""


if __name__ == "__main__":
    url: str = "https://solomonk.fr/fr/equipement/8285/coiffe-du-dragon-cochon"
    if check_url(url):
        data: json = parse_url(url)
        pprint(data)
        #with open(f"out/{data['id']}.json", "w") as f:
        #    f.write(json.dumps(data))
    else:
        raise Exception('Incorrect url')
