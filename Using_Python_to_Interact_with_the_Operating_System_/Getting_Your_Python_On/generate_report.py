#!/usr/bin/env python3

"""A Python script that reads a CSV file containing a list of the employees in the organization, counts how many people are in each department, and then generates a report using this information"""

import csv

def read_employees(csv_file_location):
    """This function receives a CSV file as a parameter and returns a list of dictionaries from that file"""
    with open(csv_file_location) as csv_file:
        csv.register_dialect('empDialect', skipinitialspace=True, strict=True)
        employee_file = csv.DictReader(csv_file, dialect = 'empDialect')
        employee_list = []
        for data in employee_file:
            employee_list.append(data)

    return employee_list

def process_data(employee_list):
    """function process_data() should now receive the list of dictionaries, i.e., employee_list as a parameter and return a dictionary of department:amount"""
    department_list = []
    for employee_data in employee_list:
        department_list.append(employee_data['Department'])

    department_data = {}
    for department_name in set(department_list):
        department_data[department_name] = department_list.count(department_name)

    return department_data

def write_report(dictionary, report_file):
    """This function writes a dictionary of department:amount to a file"""
    with open(report_file, "w+") as file:
        for key, value in sorted(dictionary.items(), key = lambda x : x[0]):
            file.write(str(key)+':'+str(value)+'\n')
    file.close()

####################################################################
employee_list = read_employees('/home/student-00-c5171c34e7b9/data/employees.csv')
#print(employee_list)

dictionary = process_data(employee_list)
#print(dictionary)

write_report(dictionary, '/home/student-00-c5171c34e7b9/test_report.txt')
