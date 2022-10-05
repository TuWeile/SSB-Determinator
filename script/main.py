import configparser

config = configparser.ConfigParser()

with open("data/SGS - Historical Prices and Yields - Benchmark Issues September.csv") as f:
    lines = f.readlines()
    print(lines)

"""
config.add_section("datasets")
config.set("datasets", )
"""