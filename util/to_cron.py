from argparse import ArgumentParser
from croniter import croniter
import re

from os import mkdir


if __name__ == "__main__":
    arg_parser = ArgumentParser()
    arg_parser.add_argument("--cron_job", nargs=2, type=str, action="append", dest="cron_jobs", help="an cron expression + the command to be executed")
    
    args = vars(arg_parser.parse_args())

    mkdir("./output")
    for cron_exp, command in args["cron_jobs"]:
        if not croniter.is_valid(cron_exp):
            print([cron_exp, command], "contains invalid cron expression!")
            
        else:
            with open("./output/" + re.split("\W+", command[command.rindex("/")+1:])[0], "w") as file:
                file.write(f"{cron_exp} {command}\n")
        
    