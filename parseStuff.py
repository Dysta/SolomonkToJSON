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
    data['damage']['percent'] = {}
    data['damage']['percent']['bonus'] = {}
    data['damage']['percent']['malus'] = {}

    data['initiative'] = {}
    data['initiative']['bonus'] = {}
    data['initiative']['malus'] = {}

    data['movementpoint'] = {}
    data['movementpoint']['bonus'] = {}
    data['movementpoint']['malus'] = {}

    data['actionpoint'] = {}
    data['actionpoint']['bonus'] = {}
    data['actionpoint']['malus'] = {}

    data['pod'] = {}
    data['pod']['bonus'] = {}
    data['pod']['malus'] = {}

    return data


def parse_effect(parsed_html: BeautifulSoup) -> dict:
    data: ResultSet = parsed_html.find_all('li')
    if not data:
        return {}

    data_dict: dict = init_stuff_dict()
    for li in data:
        # get vitality
        if li.get('data-bonus-vitality-min'):
            data_dict['vitality']['bonus']['min'] = li.get('data-bonus-vitality-min')
        if li.get('data-bonus-vitality-min'):
            data_dict['vitality']['bonus']['max'] = li.get('data-bonus-vitality-max')
        # malus
        if li.get('data-malus-vitality-min'):
            data_dict['vitality']['malus']['min'] = li.get('data-malus-vitality-min')
        if li.get('data-malus-vitality-min'):
            data_dict['vitality']['malus']['max'] = li.get('data-malus-vitality-max')

        # get wisdom
        if li.get('data-bonus-wisdom-min'):
            data_dict['wisdom']['bonus']['min'] = li.get('data-bonus-wisdom-min')
        if li.get('data-bonus-wisdom-min'):
            data_dict['wisdom']['bonus']['max'] = li.get('data-bonus-wisdom-max')
        # malus
        if li.get('data-malus-wisdom-min'):
            data_dict['wisdom']['malus']['min'] = li.get('data-malus-wisdom-min')
        if li.get('data-malus-wisdom-min'):
            data_dict['wisdom']['malus']['max'] = li.get('data-malus-wisdom-max')

        # get intelligence
        if li.get('data-bonus-intelligence-min'):
            data_dict['intelligence']['bonus']['min'] = li.get('data-bonus-intelligence-min')
        if li.get('data-bonus-intelligence-max'):
            data_dict['intelligence']['bonus']['max'] = li.get('data-bonus-intelligence-max')
        # malus
        if li.get('data-malus-intelligence-min'):
            data_dict['intelligence']['malus']['min'] = li.get('data-malus-intelligence-min')
        if li.get('data-malus-intelligence-max'):
            data_dict['intelligence']['malus']['max'] = li.get('data-malus-intelligence-max')

        # get strength
        if li.get('data-bonus-strength-min'):
            data_dict['strength']['bonus']['min'] = li.get('data-bonus-strength-min')
        if li.get('data-bonus-strength-max'):
            data_dict['strength']['bonus']['max'] = li.get('data-bonus-strength-max')
        # malus
        if li.get('data-malus-strength-min'):
            data_dict['strength']['malus']['min'] = li.get('data-malus-strength-min')
        if li.get('data-malus-strength-max'):
            data_dict['strength']['malus']['max'] = li.get('data-malus-strength-max')

        # get agility
        if li.get('data-bonus-agility-min'):
            data_dict['agility']['bonus']['min'] = li.get('data-bonus-agility-min')
        if li.get('data-bonus-agility-min'):
            data_dict['agility']['bonus']['max'] = li.get('data-bonus-agility-max')
        # malus
        if li.get('data-malus-agility-min'):
            data_dict['agility']['malus']['min'] = li.get('data-malus-agility-min')
        if li.get('data-malus-agility-min'):
            data_dict['agility']['malus']['max'] = li.get('data-malus-agility-max')

        # get chance
        if li.get('data-bonus-chance-min'):
            data_dict['chance']['bonus']['min'] = li.get('data-bonus-chance-min')
        if li.get('data-bonus-chance-min'):
            data_dict['chance']['bonus']['max'] = li.get('data-bonus-chance-max')
        # malus
        if li.get('data-malus-chance-min'):
            data_dict['chance']['malus']['min'] = li.get('data-malus-chance-min')
        if li.get('data-malus-chance-min'):
            data_dict['chance']['malus']['max'] = li.get('data-malus-chance-max')

        # get intelligence resistance
        if li.get('data-bonus-fire-resistance-min'):
            data_dict['intelligence']['resistance']['bonus']['min'] = li.get('data-bonus-fire-resistance-min')
        if li.get('data-bonus-fire-resistance-max'):
            data_dict['intelligence']['resistance']['bonus']['max'] = li.get('data-bonus-fire-resistance-max')

        # get strength resistance
        if li.get('data-bonus-earth-resistance-min'):
            data_dict['strength']['resistance']['bonus']['min'] = li.get('data-bonus-earth-resistance-min')
        if li.get('data-bonus-earth-resistance-max'):
            data_dict['strength']['resistance']['bonus']['max'] = li.get('data-bonus-earth-resistance-max')

        # get water resistance
        if li.get('data-bonus-water-resistance-min'):
            data_dict['chance']['resistance']['bonus']['min'] = li.get('data-bonus-water-resistance-min')
        if li.get('data-bonus-water-resistance-max'):
            data_dict['chance']['resistance']['bonus']['max'] = li.get('data-bonus-water-resistance-max')

        # get agility resistance
        if li.get('data-bonus-air-resistance-min'):
            data_dict['agility']['resistance']['bonus']['min'] = li.get('data-bonus-air-resistance-min')
        if li.get('data-bonus-air-resistance-max'):
            data_dict['agility']['resistance']['bonus']['max'] = li.get('data-bonus-air-resistance-max')

        # get intelligence resistance percent
        if li.get('data-bonus-fire-resistance-percent-min'):
            data_dict['intelligence']['resistance_percent']['bonus']['min'] = li.get('data-bonus-fire-resistance-percent-min')
        if li.get('data-bonus-fire-resistance-percent-max'):
            data_dict['intelligence']['resistance_percent']['bonus']['max'] = li.get('data-bonus-fire-resistance-percent-max')

        # get strength resistance percent
        if li.get('data-bonus-earth-resistance-percent-min'):
            data_dict['strength']['resistance_percent']['bonus']['min'] = li.get('data-bonus-earth-resistance-percent-min')
        if li.get('data-bonus-earth-resistance-percent-max'):
            data_dict['strength']['resistance_percent']['bonus']['max'] = li.get('data-bonus-earth-resistance-percent-max')

        # get water resistance percent
        if li.get('data-bonus-water-resistance-percent-min'):
            data_dict['chance']['resistance_percent']['bonus']['min'] = li.get('data-bonus-water-resistance-percent-min')
        if li.get('data-bonus-water-resistance-percent-max'):
            data_dict['chance']['resistance_percent']['bonus']['max'] = li.get('data-bonus-water-resistance-percent-max')

        # get agility resistance percent
        if li.get('data-bonus-air-resistance-percent-min'):
            data_dict['agility']['resistance_percent']['bonus']['min'] = li.get('data-bonus-air-resistance-percent-min')
        if li.get('data-bonus-air-resistance-percent-max'):
            data_dict['agility']['resistance_percent']['bonus']['max'] = li.get('data-bonus-air-resistance-percent-max')

        # get critical
        if li.get('data-bonus-critical-hit-min'):
            data_dict['critical']['bonus']['min'] = li.get('data-bonus-critical-hit-min')
        if li.get('data-bonus-critical-hit-max'):
            data_dict['critical']['bonus']['max'] = li.get('data-bonus-critical-hit-max')

        # get range
        if li.get('data-bonus-range-min'):
            data_dict['range']['bonus']['min'] = li.get('data-bonus-range-min')
        if li.get('data-bonus-range-max'):
            data_dict['range']['bonus']['max'] = li.get('data-bonus-range-max')

        # get damage
        if li.get('data-bonus-damage-min'):
            data_dict['damage']['bonus']['min'] = li.get('data-bonus-damage-min')
        if li.get('data-bonus-damage-max'):
            data_dict['damage']['bonus']['max'] = li.get('data-bonus-damage-max')

        # get damage percent
        if li.get('data-bonus-damage-percent-min'):
            data_dict['damage']['percent']['bonus']['min'] = li.get('data-bonus-damage-percent-min')
        if li.get('data-bonus-damage-percent-max'):
            data_dict['damage']['percent']['bonus']['max'] = li.get('data-bonus-damage-percent-max')

        # get initiative
        if li.get('data-bonus-initiative-min'):
            data_dict['initiative']['bonus']['min'] = li.get('data-bonus-initiative-min')
        if li.get('data-bonus-initiative-min'):
            data_dict['initiative']['bonus']['max'] = li.get('data-bonus-initiative-max')

        # get movementpoint
        if li.get('data-bonus-movementpoint-min'):
            data_dict['movementpoint']['bonus']['min'] = li.get('data-bonus-movementpoint-min')
        if li.get('data-bonus-movementpoint-min'):
            data_dict['movementpoint']['bonus']['max'] = li.get('data-bonus-movementpoint-max')

        # get actionpoint
        if li.get('data-bonus-actionpoint-min'):
            data_dict['actionpoint']['bonus']['min'] = li.get('data-bonus-actionpoint-min')
        if li.get('data-bonus-actionpoint-min'):
            data_dict['actionpoint']['bonus']['max'] = li.get('data-bonus-actionpoint-max')

        # get pod
        if li.get('data-bonus-pod-min'):
            data_dict['pod']['bonus']['min'] = li.get('data-bonus-pod-min')
        if li.get('data-bonus-pod-min'):
            data_dict['pod']['bonus']['max'] = li.get('data-bonus-pod-max')

    return data_dict
