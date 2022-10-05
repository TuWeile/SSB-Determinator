import numpy as np
import pandas as pd
import configparser


class RunImport:
    def __init__(self):
        self.config_obj = configparser.ConfigParser()
        self.config_obj.read("script/config.ini")
        self.config_data = self.config_obj["datasets"]
        self.dataset = self.config_data["data"]

    def import_data(self):
        data_source = pd.read_csv(self.dataset, skiprows=lambda x: x not in [i for i in range(5, 40)],
                                  usecols=[i for i in range(3, 7)], header=None)
        data_source = data_source.dropna()

        return data_source
