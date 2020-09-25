from bs4.element import Tag  # type: ignore

from solomonktojson.constants import STAT_TO_FR  # type: ignore

__all__ = ["StatParser"]


class StatParser:
    @staticmethod
    def trad(st):
        try:
            st = STAT_TO_FR[st]
        except KeyError:
            pass
        finally:
            return st

    @staticmethod
    def parse(data: dict, effect: str, li: Tag) -> dict:
        if "trap-damage-percent" in effect:
            _, bn, tr, dm, pr, mm = effect.split('-')
            data[dm][tr][pr][bn][mm] = li.get(effect)
        elif "trap-damage" in effect:
            _, bn, st, dm, mm = effect.split('-')
            data[dm][st][bn][mm] = li.get(effect)
        elif "damage-percent" in effect:
            _, bn, st, pr, mm = effect.split('-')
            data[st][pr][bn][mm] = li.get(effect)
        elif "fighters" in effect and "percent" in effect:
            _, bn, ft, st, rs, pr, mm = effect.split('-')
            st = StatParser.trad(st)
            data[st][f"{rs}_percent"][ft][bn][mm] = li.get(effect)
        elif "fighters" in effect:
            _, bn, ft, st, rs, mm = effect.split('-')
            st = StatParser.trad(st)
            data[st][rs][ft][bn][mm] = li.get(effect)
        elif "percent" in effect:
            _, bn, st, rs, _, mm = effect.split('-')
            st = StatParser.trad(st)
            data[st][f"{rs}_percent"][bn][mm] = li.get(effect)
        elif "resistance" in effect:
            _, bn, st, rs, mm = effect.split('-')
            st = StatParser.trad(st)
            data[st][rs][bn][mm] = li.get(effect)
        elif "hit" in effect:
            _, bn, st, _, mm = effect.split('-')
            data[st][bn][mm] = li.get(effect)
        else:
            _, bn, st, mm = effect.split('-')
            data[st][bn][mm] = li.get(effect)

        return data
