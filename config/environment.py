#This file reads the config.yaml file and it allows us to for configuration of the Cases.


import yaml

def load_config():
    with open("config/config.yaml", "r") as file:
        return yaml.safe_load(file)

config = load_config()