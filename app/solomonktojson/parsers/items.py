import collections
import json
import os
import re

from bs4 import BeautifulSoup, NavigableString, ResultSet  # type: ignore
from urllib.request import Request, urlopen

from solomonktojson.constants import EFFECTS  # type: ignore

from .stats import StatParser


__all__ = ["ItemParser"]


def nested():
    return collections.defaultdict(nested)


class ItemParser:
    def __init__(self, item: int, config) -> None:
        headers: dict = {
            'User-Agent': config.get('browser', 'user_agent')
        }
        self.item: int = item
        url: str = os.path.join(config.get('browser', 'base_url'), 'fr', 'equipement', str(item))
        req: Request = Request(url, headers=headers)
        html: str = urlopen(req, timeout=3.0).read()
        self.parsed_html: BeautifulSoup = BeautifulSoup(html, "html.parser")

    def _get_name(self) -> str:
        data = self.parsed_html.find('div', attrs={'class': 'card-solo-item-title'})
        return data.a.string

    def _get_description(self) -> str:
        data: NavigableString = self.parsed_html.find('div', attrs={'class': 'card-solo-item-description'})
        return data.string

    def _get_recipe(self) -> list:
        data: NavigableString = self.parsed_html.find('div', attrs={'class': 'list-craft'})
        if not data:
            return []

        recipe_data: list = []
        all_link: ResultSet = data.find_all('a')
        for a in all_link:
            tmp_dict = {}
            tmp_dict['id'] = int(re.search(r'\d+', a.get('href')).group())
            tmp_dict['name'] = a.string
            tmp_dict['quantity'] = 0
            recipe_data.append(tmp_dict)

        i: int = 0
        for string in data.strings:
            if re.match(r'(, )?\d+x', string):
                quantity: int = int(re.search(r'\d+', string).group())
                recipe_data[i]['quantity'] = quantity
                i += 1

        return recipe_data

    def _get_condition(self) -> list:
        data: ResultSet = self.parsed_html.find_all('ul', attrs={'class': 'list-unstyled'})
        data_list: list = []

        if len(data) > 1:
            for li in data[1].children:
                data_list.append(li.string)

        return data_list

    def _get_effects(self) -> str:
        data: ResultSet = self.parsed_html.find_all('ul', attrs={'class': 'list-unstyled'})
        if not data:
            return ""

        d = nested()
        for li in data[0].children:
            for effect in EFFECTS:
                if li.get(effect):
                    d = StatParser.parse(d, effect, li)
        return json.dumps(d)

    def get_output(self) -> dict:
        return {
            'name': self._get_name(),
            'description': self._get_description(),
            'recipe': self._get_recipe(),
            'condition': self._get_condition(),
            'effects': self._get_effects(),
        }
