import argparse
from core.main import main
import yaml

description = """
This is a MMM tournament creation app. It's aim is to make creating MMM tournaments on Challonge easier and faster.
"""

parser = argparse.ArgumentParser(description=description)

parser.add_argument("config", type=open, help="config file according to which the tournament shall be created")


parser.add_argument("--name", "-n", help="this is a value that can be used in the configs")
parser.add_argument("--number", "-N", help="this is a value that can be used in the configs")
parser.add_argument("--delete", "-d", action='store_true', help="gives the user an option to delete the tournament after it is created")

values = parser.parse_args()
print(values)
main(yaml.safe_load(values.config.read()), values.delete, {"name": values.name, "number": values.number})