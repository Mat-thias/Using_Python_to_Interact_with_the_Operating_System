#!/usr/bin/env python3

"""This is a script that generates two different reports from this internal ticketing system log file i.e., syslog.log"""

import re
import csv

def defining_global_variables():
    global ERROR_DICT, USAGE_DICT, RE_PATTERN, INFO_PATTERN, ERROR_PATTERN

    USAGE_DICT = {}
    ERROR_DICT = {}

    # RE_PATTERN = r" (INFO|ERROR) ([\w ']+) (\[#\d\d\d\d\])?[ ]?\(([\w.]+)\)"
    RE_PATTERN = r" (INFO|ERROR) "
    RE_PATTERN= re.compile(RE_PATTERN)
    INFO_PATTERN = r" (INFO) ([\w ']+) \[#\d+\] \(([\w.]+)\)"
    INFO_PATTERN = re.compile(INFO_PATTERN)
    ERROR_PATTERN = r" (ERROR) ([\w ']+) \(([\w.]+)\)"
    ERROR_PATTERN = re.compile(ERROR_PATTERN)
    '''To match example lines and extract required field
    "May 27 11:45:40 ubuntu.local ticky: INFO: Created ticket [#1234] (username)"'''

def increase_user_dict(username, exit_status):
    """This is a function that increases the corresponding exit status for each user"""
    if username not in USAGE_DICT:
        USAGE_DICT[username] = {"INFO" : 0, "ERROR" : 0}

    if exit_status in USAGE_DICT[username]:
        USAGE_DICT[username][exit_status] = USAGE_DICT[username][exit_status] + 1
   
    # USAGE_DICT[username][exit_status] = USAGE_DICT[username][exit_status] .get(exit_status, 0) + 1

def increase_error_dict(error_message):
    """This is a function that increases the value for corresponding exit messages"""

    ERROR_DICT[error_message] = ERROR_DICT.get(error_message, 0) + 1

    # if error_message in ERROR_DICT:
    #     ERROR_DICT[error_message] = ERROR_DICT[error_message] + 1
    # else:
    #     ERROR_DICT[error_message] = 1

def generate_error_dict():
    """Generates error dictionary whose keys are the error messages"""

    with open("syslog.log") as file:
        for line in file:
            pattern_result = ERROR_PATTERN.search(line)

            if pattern_result:
                increase_error_dict(pattern_result.group(2))

        file.close()  

def generate_user_usage_dict():
    """Generates a user usage statistics whose keys are the username and values are dictionaries with values of the number of successful and failed exit"""

    with open("syslog.log") as file:
        for line in file:
            pattern_result = RE_PATTERN.search(line)

            if (pattern_result and (pattern_result.group(1) == "INFO")):
                pattern_result = INFO_PATTERN.search(line)

            elif (pattern_result and (pattern_result.group(1) == "ERROR")):
                pattern_result = ERROR_PATTERN.search(line)

            increase_user_dict(pattern_result.group(3), pattern_result.group(1))

        file.close()

def convert_error_dict_csv():
    """THis is a function thaa=t concverts the error dict to a csv file"""

    with open("error_message.csv", "w") as file:
        writer = csv.writer(file)

        header = ["Error", "Count"]
        writer.writerow(header)
        for error, count in sorted(ERROR_DICT.items(), key=lambda x:x[1], reverse=True):
            row = [error, count]

            writer.writerow(row)

        file.close()

def convert_usage_dict_csv():
    """THis is a function thaa=t concverts the usage dict to a csv file"""

    sorted_usernames = sorted(USAGE_DICT)

    with open("user_statistics.csv", "w") as file:
        writer = csv.writer(file)

        header = ["Username", "INFO", "ERROR"]
        writer.writerow(header)
        for username in sorted_usernames:
            row = [username]
            row.append(USAGE_DICT[username]["INFO"])
            row.append(USAGE_DICT[username]["ERROR"])

            writer.writerow(row)

        file.close()

def main():
    defining_global_variables()
    generate_error_dict()
    generate_user_usage_dict()
    convert_error_dict_csv()
    convert_usage_dict_csv()


if __name__ == "__main__":
    main()