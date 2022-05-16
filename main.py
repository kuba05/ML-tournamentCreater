import argparse
import yaml


from core.setup import formateConfig
from core.sel import prepareSelenium, createTournamentSelenium, stopSelenium, deleteTournamentSelenium
from core.helper import loadFromEnviroment, loadFromUser


description = """
This is a MMM tournament creation app. It's aim is to make creating MMM tournaments on Challonge easier and faster.
"""

parser = argparse.ArgumentParser(description=description)

parser.add_argument("config", type=open, help="config file according to which the tournament shall be created")

parser.add_argument("--delete", "-d", action='store_true', help="gives the user an option to delete the tournament after it is created")

values = parser.parse_args()

config = yaml.safe_load(values.config)


#load params
params = config["parameters"]
params = dict(**loadFromEnviroment(params["env"]), **loadFromUser(params["user"]))

# formate the config
formatedConfig = formateConfig(config["tournament"], params)


# make sure we delete the tournament if requested

selenium = prepareSelenium()

tournamentURL = createTournamentSelenium(selenium, formatedConfig)

if values.delete:
    while True:
        answer = input("Do you want to delete the tournament?[Y/N] ")
        if len(answer) == 0:
            continue
        if answer[0].lower() == "y":
            deleteTournamentSelenium(selenium, tournamentURL)
            break
        if answer[0].lower() == "n":
            break

input()
stopSelenium(selenium)
