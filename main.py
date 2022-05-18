import argparse
import yaml


from core.sel import prepareSelenium, createTournamentSelenium, stopSelenium, deleteTournamentSelenium
from core.helper import setupAuthentication, setupLogging, endLogging, loadParamsFromConfigAndFormateConfig, confirm


setupLogging("log/main.log")


description = """
This is a MMM tournament creation app. It's aim is to make creating MMM tournaments on Challonge easier and faster.
"""

parser = argparse.ArgumentParser(description=description)

parser.add_argument("config", type=open, help="config file according to which the tournament shall be created")

parser.add_argument("--delete", "-d", action='store_true', help="give the user an option to delete the tournament after it is created")

parser.add_argument("--headless", "-H", action='store_true', help="run selenium headless")


def main(values):
    setupAuthentication()
    
    config = loadParamsFromConfigAndFormateConfig(yaml.safe_load(values.config))

    print("Tournament creation in progress...", flush=True)

    selenium = prepareSelenium(values.headless)

    tournamentURL = createTournamentSelenium(selenium, config["tournament"]["creation"], config["tournament"]["event"])

    print("Tournament created!", flush=True)

    if values.delete:
        if confirm("Do you want to delete the tournament?[Y/N] "):
            deleteTournamentSelenium(selenium, tournamentURL)
            print("Tournament deleted!", flush=True)
            
    stopSelenium(selenium)


main(parser.parse_args())

endLogging()