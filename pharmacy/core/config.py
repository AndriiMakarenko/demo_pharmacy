import os

import yaml

from pharmacy.core.exceptions import InvalidConfigException


class Config:
    def __init__(self, config_file="config.yaml"):
        config_file_path = os.path.join(os.path.dirname(__file__), config_file)

        with open(config_file_path, "r") as f:
            config_data = yaml.safe_load(f)

        for key, value in config_data.items():
            setattr(self, key, value)
