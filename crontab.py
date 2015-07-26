# Skript: command_line
# Date: 27.07.2015
# Author: Eugen Geist
# Summary: Provides a method to create cron jobs with a file.

import command_line
import sys

def create_cronjobs_from_file(file_path):
    if file_path == None:
        print("File with cronjobs not defined. Exit.")
        sys.exit(1)

    print(command_line.exec_command("crontab " + file_path))
    return None

def set_cronjob(minute, hour, day_of_m, day_of_w, month, command):
    if command == None:
        print("No command defined, exiting")
        sys.exit(1)

    if minute == None:
        exec_minute = "*"
    else:
        exec_minute = minute
        
    if hour == None:
        exec_hour = "*"
    else:
        exec_hour = hour

    if day_of_m == None:
        exec_day_of_m = "*"
    else:
        exec_day_of_m = day_of_m

    if day_of_w == None:
        exec_day_of_w = "*"
    else:
        exec_day_of_w = day_of_w

    if month == None:
        exec_month = "*"
    else:
        exec_month = month

    print(command_line.exec_command("crontab -e {} {} {} {} {} {}".format(exec_minute, exec_hour, exec_day_of_m, exec_day_of_w, exec_month, command))
    return None
        
