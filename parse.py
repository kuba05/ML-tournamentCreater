import argparse
import yaml

from core.main import createTournament, deleteTournament
from core.setup import setup, formateConfig
from core.sel import prepareSelenium, CreateTournamentWithSelenium, stopSelenium

description = """
This is a MMM tournament creation app. It's aim is to make creating MMM tournaments on Challonge easier and faster.
"""

parser = argparse.ArgumentParser(description=description)

parser.add_argument("config", type=open, help="config file according to which the tournament shall be created")

parser.add_argument("--name", "-n", default="", help="this is a value that can be used in the configs")
parser.add_argument("--number", "-N", default="", help="this is a value that can be used in the configs")                                           
parser.add_argument("--url_suffix", "-u", default="", help="this is a value that can be used in the configs")
parser.add_argument("--delete", "-d", action='store_true', help="gives the user an option to delete the tournament after it is created")
parser.add_argument("--date", "-D", help="Date of the tournament. Use format: YYYY-MM-DD-HH:mm:SS (UTC+0)")
values = parser.parse_args()

config = yaml.safe_load(values.config)

# formate the config
config = formateConfig(config, {"name": values.name, "number": values.number, "url_suffix": values.url_suffix, "date": values.date})

#setup()

#tournamentURL = createTournament(config)
    
# make sure we delete the tournament if requested
try:    
    selenium = prepareSelenium()
    
    CreateTournamentWithSelenium(selenium, config)
    
    stopSelenium(selenium)

except Exception as e:
    print("Error in selenium:",e)
    raise e
    
    
if values.delete:
    deleteTournament(tournamentURL)
