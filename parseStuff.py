from bs4 import BeautifulSoup, ResultSet

effect_list: list = [
    'data-bonus-vitality-min',
    'data-bonus-vitality-max',
    'data-malus-vitality-min',
    'data-malus-vitality-max',

    'data-bonus-wisdom-min',
    'data-bonus-wisdom-max',
    'data-malus-wisdom-min',
    'data-malus-wisdom-max',

    'data-bonus-intelligence-min',
    'data-bonus-intelligence-max',
    'data-malus-intelligence-min',
    'data-malus-intelligence-max',

    'data-bonus-strength-min',
    'data-bonus-strength-max',
    'data-malus-strength-min',
    'data-malus-strength-max',

    'data-bonus-agility-min',
    'data-bonus-agility-max',
    'data-malus-agility-min',
    'data-malus-agility-max',

    'data-bonus-chance-min',
    'data-bonus-chance-max',
    'data-malus-chance-min',
    'data-malus-chance-max',

    'data-bonus-neutral-resistance-min',
    'data-bonus-neutral-resistance-max',
    'data-bonus-fire-resistance-min',
    'data-bonus-fire-resistance-max',
    'data-bonus-earth-resistance-min',
    'data-bonus-earth-resistance-max',
    'data-bonus-water-resistance-min',
    'data-bonus-water-resistance-max',
    'data-bonus-air-resistance-min',
    'data-bonus-air-resistance-max',
    'data-malus-neutral-resistance-min',
    'data-malus-neutral-resistance-max',
    'data-malus-fire-resistance-min',
    'data-malus-fire-resistance-max',
    'data-malus-earth-resistance-min',
    'data-malus-earth-resistance-max',
    'data-malus-water-resistance-min',
    'data-malus-water-resistance-max',
    'data-malus-air-resistance-min',
    'data-malus-air-resistance-max',

    'data-bonus-neutral-resistance-percent-min',
    'data-bonus-neutral-resistance-percent-max',
    'data-bonus-fire-resistance-percent-min',
    'data-bonus-fire-resistance-percent-max',
    'data-bonus-earth-resistance-percent-min',
    'data-bonus-earth-resistance-percent-max',
    'data-bonus-water-resistance-percent-min',
    'data-bonus-water-resistance-percent-max',
    'data-bonus-air-resistance-percent-min',
    'data-bonus-air-resistance-percent-max',
    'data-malus-neutral-resistance-percent-min',
    'data-malus-neutral-resistance-percent-max',
    'data-malus-fire-resistance-percent-min',
    'data-malus-fire-resistance-percent-max',
    'data-malus-earth-resistance-percent-min',
    'data-malus-earth-resistance-percent-max',
    'data-malus-water-resistance-percent-min',
    'data-malus-water-resistance-percent-max',
    'data-malus-air-resistance-percent-min',
    'data-malus-air-resistance-percent-max',

    'data-bonus-critical-hit-min',
    'data-bonus-critical-hit-max',

    'data-bonus-range-min',
    'data-bonus-range-max',

    'data-bonus-damage-min',
    'data-bonus-damage-max',

    'data-bonus-damage-percent-min',
    'data-bonus-damage-percent-max',

    'data-bonus-initiative-min',
    'data-bonus-initiative-max',

    'data-bonus-movementpoint-min',
    'data-bonus-movementpoint-max',
    'data-malus-movementpoint-min',
    'data-malus-movementpoint-max',

    'data-bonus-actionpoint-min',
    'data-bonus-actionpoint-max',
    'data-malus-actionpoint-min',
    'data-malus-actionpoint-max',

    'data-bonus-pod-min',
    'data-bonus-pod-max',

    'data-bonus-summon-min',
    'data-bonus-summon-max',

    'data-bonus-prospecting-min',
    'data-bonus-prospecting-max',

    'data-bonus-initiative-min',
    'data-bonus-initiative-max',

    'data-bonus-heal-min',
    'data-bonus-heal-max',

    'data-bonus-trap-damage-min',
    'data-bonus-trap-damage-max',
    'data-bonus-trap-damage-percent-min',
    'data-bonus-trap-damage-percent-max'
]

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

    data['neutral'] = {}
    data['neutral']['resistance'] = {}
    data['neutral']['resistance']['bonus'] = {}
    data['neutral']['resistance']['malus'] = {}
    data['neutral']['resistance_percent'] = {}
    data['neutral']['resistance_percent']['bonus'] = {}
    data['neutral']['resistance_percent']['malus'] = {}

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
    data['damage']['trap'] = {}
    data['damage']['trap']['bonus'] = {}
    data['damage']['trap']['malus'] = {}
    data['damage']['trap']['percent'] = {}
    data['damage']['trap']['percent']['bonus'] = {}
    data['damage']['trap']['percent']['malus'] = {}

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

    data['summon'] = {}
    data['summon']['bonus'] = {}
    data['summon']['malus'] = {}

    data['prospecting'] = {}
    data['prospecting']['bonus'] = {}
    data['prospecting']['malus'] = {}

    data['initiative'] = {}
    data['initiative']['bonus'] = {}
    data['initiative']['malus'] = {}

    data['heal'] = {}
    data['heal']['bonus'] = {}
    data['heal']['malus'] = {}

    return data

def get_effect(current_data: dict, effect: str, li: str) -> dict:
    new_data: dict = current_data.copy()

    if "trap-damage-percent" in effect:
        _, bn, tr, dm, pr, mm = effect.split('-')
        new_data[dm][tr][pr][bn][mm] = li.get(effect)
    elif "trap-damage" in effect:
        _, bn, st, dm, mm = effect.split('-')
        new_data[dm][st][bn][mm] = li.get(effect)
    elif "damage-percent" in effect:
        _, bn, st, pr, mm = effect.split('-')
        new_data[st][pr][bn][mm] = li.get(effect)
    elif "percent" in effect:
        _, bn, st, rs, _, mm = effect.split('-')
        st = "intelligence" if st == "fire" else st
        st = "chance" if st == "water" else st
        st = "strength" if st == "earth" else st
        st = "agility" if st == "air" else st
        rs = rs + "_percent"

        new_data[st][rs][bn][mm] = li.get(effect)
    elif "resistance" in effect:
        _, bn, st, rs, mm = effect.split('-')
        st = "intelligence" if st == "fire" else st
        st = "chance" if st == "water" else st
        st = "strength" if st == "earth" else st
        st = "agility" if st == "air" else st

        new_data[st][rs][bn][mm] = li.get(effect)
    elif "hit" in effect:
        _, bn, st, _, mm = effect.split('-')
        new_data[st][bn][mm] = li.get(effect)
    else:
        _, bn, st, mm = effect.split('-')

        new_data[st][bn][mm] = li.get(effect)

    return new_data


def parse_effect(parsed_html: BeautifulSoup) -> dict:
    data: ResultSet = parsed_html.find_all('ul', attrs={'class': 'list-unstyled'})
    if not data:
        return {}

    data_dict: dict = init_stuff_dict()
    for li in data[0].children:
        for effect in effect_list:
            if li.get(effect):
                data_dict = get_effect(data_dict, effect, li)

    return data_dict


def parse_condition(parsed_html: BeautifulSoup) -> list:
    data: ResultSet = parsed_html.find_all('ul', attrs={'class': 'list-unstyled'})
    data_list: list = []

    if len(data) > 1:
        for li in data[1].children:
            data_list.append(li.string)

    return data_list
