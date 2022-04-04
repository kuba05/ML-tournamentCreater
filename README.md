# Magic Mage Masters Tournament Creation Script

This script is part of a project to automatize as much as possible in MMM tournaments.

## how to use
Either use a tool in coresponding directory (/windows or /linux) or run the python scipt called parse.py from your commandline.

The standard usage of the script is:

    python3 parse.py config/tournamentConfigs/MLconfig -N 18

If in doubt, use -h or --help switch to see documentation for the script :)

 - - -
 
Don't forget to install dependencies and add your real credentials to config/credentials.yaml (see https://challonge.com/settings/developer).

    pip install -r requirements.txt

## structure
- /core contains all the python code
- /config contains all config files, including credentials.yaml
- /windows includes tools to use this app on windows
- /linux includes tools to use this app on linux

