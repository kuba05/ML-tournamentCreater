# Magic Mage Masters Tournament Creation Script

This script is part of a project to automatize as much as possible in MMM tournaments.

## how to use
Run the python scipt called main.py from your commandline.

The standard usage of the script is:

    python3 main.py -H tournamentConfigs/MLconfig

If in doubt, use -h or --help switch to see documentation for the script :)

 - - -
 
Don't forget to install dependencies:

    pip install -r requirements.txt

## structure
- /core contains all the python code
    - /core/sel includes all selenium code
    - /core/helper includes helpers that have no other specific location
- /config contains all app config files, including credentials.yaml
- /tournamentConfig contains all tournament configs, i.e. prescriptions of how the tournaments should be created
- /log contains all logs