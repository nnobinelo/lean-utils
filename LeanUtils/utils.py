import json
from pathlib import Path
from LeanUtils import BACKTEST_CONFIG_FILENAME, BACKTEST_CONFIG_ID_KEY


def get_backtest_id(backtest_dir):
    with open((Path(backtest_dir) / BACKTEST_CONFIG_FILENAME).resolve(), "r") as json_file:
        config = json.load(json_file)
    return config[BACKTEST_CONFIG_ID_KEY]
