from bs4 import BeautifulSoup, ResultSet


def parse_name(parsed_html: BeautifulSoup) -> str:
    data = parsed_html.find('div', attrs={'class': 'card-solo-item-title'})
    return data.a.string


def init_stuff_dict() -> dict:
    data: dict = {}

    data['vitality'] = {}
    data['vitality']['bonus'] = {}
    data['vitality']['malus'] = {}

    data['wisdom'] = {}
    data['wisdom']['bonus'] = {}
    data['wisdom']['malus'] = {}

    data['intelligence'] = {}
    data['intelligence']['bonus'] = {}
    data['intelligence']['malus'] = {}
    data['intelligence']['resistance'] = {}
    data['intelligence']['resistance']['bonus'] = {}
    data['intelligence']['resistance']['malus'] = {}
    data['intelligence']['resistance_percent'] = {}
    data['intelligence']['resistance_percent']['bonus'] = {}
    data['intelligence']['resistance_percent']['malus'] = {}

    data['strength'] = {}
    data['strength']['bonus'] = {}
    data['strength']['malus'] = {}
    data['strength']['resistance'] = {}
    data['strength']['resistance']['bonus'] = {}
    data['strength']['resistance']['malus'] = {}
    data['strength']['resistance_percent'] = {}
    data['strength']['resistance_percent']['bonus'] = {}
    data['strength']['resistance_percent']['malus'] = {}

    data['agility'] = {}
    data['agility']['bonus'] = {}
    data['agility']['malus'] = {}
    data['agility']['resistance'] = {}
    data['agility']['resistance']['bonus'] = {}
    data['agility']['resistance']['malus'] = {}
    data['agility']['resistance_percent'] = {}
    data['agility']['resistance_percent']['bonus'] = {}
    data['agility']['resistance_percent']['malus'] = {}

    data['chance'] = {}
    data['chance']['bonus'] = {}
    data['chance']['malus'] = {}
    data['chance']['resistance'] = {}
    data['chance']['resistance']['bonus'] = {}
    data['chance']['resistance']['malus'] = {}
    data['chance']['resistance_percent'] = {}
    data['chance']['resistance_percent']['bonus'] = {}
    data['chance']['resistance_percent']['malus'] = {}

    data['range'] = {}
    data['range']['bonus'] = {}
    data['range']['malus'] = {}

    data['critical'] = {}
    data['critical']['bonus'] = {}
    data['critical']['malus'] = {}

    data['damage'] = {}
    data['damage']['bonus'] = {}
    data['damage']['malus'] = {}


    return data


def parse_effect(parsed_html: BeautifulSoup) -> dict:
    data: ResultSet = parsed_html.find_all('li')
    if not data:
        return {}

    data_dict: dict = init_stuff_dict()
    for li in data:
        # get vitality
        if not li.get('data-bonus-vitality-min') is None:
            data_dict['vitality']['bonus']['min'] = li.get('data-bonus-vitality-min')
        if not li.get('data-bonus-vitality-min') is None:
            data_dict['vitality']['bonus']['max'] = li.get('data-bonus-vitality-max')

        # get wisdom
        if not li.get('data-bonus-wisdom-min') is None:
            data_dict['wisdom']['bonus']['min'] = li.get('data-bonus-wisdom-min')
        if not li.get('data-bonus-wisdom-min') is None:
            data_dict['wisdom']['bonus']['max'] = li.get('data-bonus-wisdom-max')

        # get intelligence
        if not li.get('data-bonus-intelligence-min') is None:
            data_dict['intelligence']['bonus']['min'] = li.get('data-bonus-intelligence-min')
        if not li.get('data-bonus-intelligence-max') is None:
            data_dict['intelligence']['bonus']['max'] = li.get('data-bonus-intelligence-max')

        # get strength
        if not li.get('data-bonus-strength-min') is None:
            data_dict['strength']['bonus']['min'] = li.get('data-bonus-strength-min')
        if not li.get('data-bonus-strength-max') is None:
            data_dict['strength']['bonus']['max'] = li.get('data-bonus-strength-max')

        # get agility
        if not li.get('data-bonus-agility-min') is None:
            data_dict['agility']['bonus']['min'] = li.get('data-bonus-agility-min')
        if not li.get('data-bonus-agility-min') is None:
            data_dict['agility']['bonus']['max'] = li.get('data-bonus-agility-max')

        # get chance
        if not li.get('data-bonus-chance-min') is None:
            data_dict['chance']['bonus']['min'] = li.get('data-bonus-chance-min')
        if not li.get('data-bonus-chance-min') is None:
            data_dict['chance']['bonus']['max'] = li.get('data-bonus-chance-max')

        # get intelligence resistance
        if not li.get('data-bonus-fire-resistance-min') is None:
            data_dict['intelligence']['resistance']['bonus']['min'] = li.get('data-bonus-fire-resistance-min')
        if not li.get('data-bonus-fire-resistance-max') is None:
            data_dict['intelligence']['resistance']['bonus']['max'] = li.get('data-bonus-fire-resistance-max')

        # get strength resistance
        if not li.get('data-bonus-earth-resistance-min') is None:
            data_dict['strength']['resistance']['bonus']['min'] = li.get('data-bonus-earth-resistance-min')
        if not li.get('data-bonus-earth-resistance-max') is None:
            data_dict['strength']['resistance']['bonus']['max'] = li.get('data-bonus-earth-resistance-max')

        # get water resistance
        if not li.get('data-bonus-water-resistance-min') is None:
            data_dict['chance']['resistance']['bonus']['min'] = li.get('data-bonus-water-resistance-min')
        if not li.get('data-bonus-water-resistance-max') is None:
            data_dict['chance']['resistance']['bonus']['max'] = li.get('data-bonus-water-resistance-max')

        # get agility resistance
        if not li.get('data-bonus-air-resistance-min') is None:
            data_dict['agility']['resistance']['bonus']['min'] = li.get('data-bonus-air-resistance-min')
        if not li.get('data-bonus-air-resistance-max') is None:
            data_dict['agility']['resistance']['bonus']['max'] = li.get('data-bonus-air-resistance-max')

        # get intelligence resistance percent
        if not li.get('data-bonus-fire-resistance-percent-min') is None:
            data_dict['intelligence']['resistance_percent']['bonus']['min'] = li.get('data-bonus-fire-resistance-percent-min')
        if not li.get('data-bonus-fire-resistance-percent-max') is None:
            data_dict['intelligence']['resistance_percent']['bonus']['max'] = li.get('data-bonus-fire-resistance-percent-max')

        # get strength resistance percent
        if not li.get('data-bonus-earth-resistance-percent-min') is None:
            data_dict['strength']['resistance_percent']['bonus']['min'] = li.get('data-bonus-earth-resistance-percent-min')
        if not li.get('data-bonus-earth-resistance-percent-max') is None:
            data_dict['strength']['resistance_percent']['bonus']['max'] = li.get('data-bonus-earth-resistance-percent-max')

        # get water resistance percent
        if not li.get('data-bonus-water-resistance-percent-min') is None:
            data_dict['chance']['resistance_percent']['bonus']['min'] = li.get('data-bonus-water-resistance-percent-min')
        if not li.get('data-bonus-water-resistance-percent-max') is None:
            data_dict['chance']['resistance_percent']['bonus']['max'] = li.get('data-bonus-water-resistance-percent-max')

        # get agility resistance percent
        if not li.get('data-bonus-air-resistance-percent-min') is None:
            data_dict['agility']['resistance_percent']['bonus']['min'] = li.get('data-bonus-air-resistance-percent-min')
        if not li.get('data-bonus-air-resistance-percent-max') is None:
            data_dict['agility']['resistance_percent']['bonus']['max'] = li.get('data-bonus-air-resistance-percent-max')

        # get critical
        if not li.get('data-bonus-critical-hit-min') is None:
            data_dict['critical']['bonus']['min'] = li.get('data-bonus-critical-hit-min')
        if not li.get('data-bonus-critical-hit-max') is None:
            data_dict['critical']['bonus']['max'] = li.get('data-bonus-critical-hit-max')

        # get range
        if not li.get('data-bonus-range-min') is None:
            data_dict['range']['bonus']['min'] = li.get('data-bonus-range-min')
        if not li.get('data-bonus-range-max') is None:
            data_dict['range']['bonus']['max'] = li.get('data-bonus-range-max')

        # get damage
        if not li.get('data-bonus-damage-min') is None:
            data_dict['damage']['bonus']['min'] = li.get('data-bonus-damage-min')
        if not li.get('data-bonus-damage-max') is None:
            data_dict['damage']['bonus']['max'] = li.get('data-bonus-damage-max')

    # print(data_dict)
    return data_dict
