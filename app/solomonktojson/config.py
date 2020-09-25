import configparser


class Config:
    def __init__(self, config_file=None):
        self.config = configparser.ConfigParser()
        self.config.read(config_file)

    def get(self, *args, **kwargs):
        return self.config.get(*args, **kwargs)
