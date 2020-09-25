import argparse
import datetime
import json

from pprint import pprint

from solomonktojson.config import Config  # type: ignore
from solomonktojson.parsers import ItemParser  # type: ignore


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--item', dest='items', nargs='+', type=int, help='<Required> Items to parse', required=True)
    parser.add_argument('--export', dest='export', default=False, action='store_true')
    parser.add_argument('--config', dest='config', required=True)
    args = parser.parse_args()

    config = Config(args.config)
    output = {}
    for item in args.items:
        output[item] = ItemParser(item, config).get_output()

    pprint(output)

    if args.export:
        with open(f"../out/{str(datetime.datetime.now())}.json", "w") as f:
            f.write(json.dumps(output))
