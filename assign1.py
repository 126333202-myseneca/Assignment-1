#!/usr/bin/env python3



'''

OPS435 Assignment 1 - Winter 2023

Program: assign1.py (replace student_id with your Seneca User name)

Author: Md Younus Islam

The python code in this file (assign1.py) is original work written by

Md Younus Islam. No code in this file is copied from any other source 

except those provided by the course instructor, including any person, 

textbook, or on-line resource. I have not shared this python script 

with anyone or anything except for submission for grading.  

I understand that the Academic Honesty Policy will be enforced and 

violators will be reported and appropriate action will be taken.



Description: This is a script to calculate the date after or before a given date by a given number of days.



Date: 15/03/2023

'''



import sys



def usage():

    '''This function prints out the usage message when the user inputs invalid command line arguments.'''

    print("Usage: assign1.py DD-MM-YYYY N")

    sys.exit()



def days_in_mon(month):

    '''This function takes a month in MM format, and returns the number of days in that month.'''

    if month in (1, 3, 5, 7, 8, 10, 12):

        return 31

    elif month in (4, 6, 9, 11): 

        return 30

    else:

        return 0



def valid_date(date):

    '''This function takes a date in DD-MM-YYYY format, and returns True if it is a valid date, False otherwise.'''

    str_day, str_month, str_year = date.split('-')

    day = int(str_day)

    month = int(str_month)

    year = int(str_year)

    

    if month > 12:

        print("Error: wrong month entered")

        sys.exit()

    if days_in_mon(month) < day:

        print("Error: wrong day entered")

        sys.exit()

    

    return True



def leap_year(year):

    '''takes a year in YYYY format, and returns True if it's a leap year, False otherwise.'''

    lyear = year % 4

    if lyear == 0:

        feb_max = 29 # this is a leap year

    else:

        feb_max = 28 # this is not a leap year



    lyear = year % 100

    if lyear == 0:

        feb_max = 28 # this is not a leap year



    lyear = year % 400

    if lyear == 0:

        feb_max = 29 # this is a leap year

    

    return feb_max



def after(today):

    '''after takes a valid date string in DD-MM-YYYY format and returns

    a date string for the next day in DD-MM-YYYY format.'''

    if len(today) != 10:

        return '00-00-0000'

    else:

        str_day, str_month, str_year = today.split('-')

        year = int(str_year)

        month = int(str_month)

        day = int(str_day)



        feb_max = leap_year(year)



        mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

        tmp_day = day + 1 # next day

        if tmp_day > mon_max[month]:

            to_day = tmp_day % mon_max[month] # if tmp_day > this month's max, reset to 1

            tmp_month = month + 1

        else:

            to_day = tmp_day

            tmp_month = month + 0



        if tmp_month > 12:

            to_month = 1

            year = year + 1

        else:

            to_month = tmp_month + 0



        next_date = str(to_day).zfill(2)+"-"+str(to_month).zfill(2)+"-"+str(year)

        return next_date



def before(today):

    '''before takes a valid date string in DD-MM-YYYY format and returns

    a date string for the day before in DD-MM-YYYY format.'''

    if len(today) != 10:

        return '00-00-0000'

    else:

        str_day, str_month, str_year = today.split('-')

        year = int(str_year)

        month = int(str_month)

        day = int(str_day)



        feb_max = leap_year(year)



        mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

        tmp_day = day - 1 # previous day

        if tmp_day <= 0:

            tmp_month = month - 1

            if tmp_month <= 0:

                tmp_month = 12

                year = year - 1

            to_day = mon_max[tmp_month]

        else:

            to_day = tmp_day

            tmp_month = month + 0



        to_month = tmp_month + 0



        prev_date = str(to_day).zfill(2)+"-"+str(to_month).zfill(2)+"-"+str(year)

        return prev_date



def dbda(start_date, num_days):

    '''This function takes a start date in "DD-MM-YYYY" format and a positive or negative integer, and returns a date either before or after the given date according to the value of the given integer in the same format.'''

    end_date = start_date

    if num_days >= 0:

        for i in range(num_days):

            end_date = after(end_date)

    else:

        for i in range(-num_days):

            end_date = before(end_date)

    return end_date



if __name__ == "__main__":

    if len(sys.argv) != 3:

        usage()

    else:

        start_date = sys.argv[1]

        num_days = int(sys.argv[2])

        valid_date(start_date)

        end_date = dbda(start_date, num_days)

        print(end_date)
