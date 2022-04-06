import argparse
import yaml

from core.main import main
from core.setup import setup

description = """
This is a MMM tournament creation app. It's aim is to make creating MMM tournaments on Challonge easier and faster.
"""

parser = argparse.ArgumentParser(description=description)

parser.add_argument("config", type=open, help="config file according to which the tournament shall be created")

parser.add_argument("--name", "-n", default="", help="this is a value that can be used in the configs")
parser.add_argument("--number", "-N", default="", help="this is a value that can be used in the configs")                                           
parser.add_argument("--url_suffix", "-u", default="", help="this is a value that can be used in the configs")
parser.add_argument("--delete", "-d", action='store_true', help="gives the user an option to delete the tournament after it is created")

values = parser.parse_args()


setup()
main(yaml.safe_load(values.config), values.delete, {"name": values.name, "number": values.number, "url_suffix": values.url_suffix})