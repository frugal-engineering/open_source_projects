#!/usr/bin/python

import time
import calendar
import sys
from datetime import date

ONE_DAY = 60 * 60 * 24

def main(options):
    first_date = format_date(options.first_date)
    second_date = format_date(options.second_date)

    date_validity(first_date)
    date_validity(second_date)

    difference_in_seconds = abs(calendar.timegm(second_date) - calendar.timegm(first_date))
    difference_in_days = difference_in_seconds / ONE_DAY

    print "Number of days between %s and %s: %d " % (options.first_date, options.second_date, difference_in_days)

def format_date(date):
    day = int(date[:2])
    month = int(date[2:4])
    year = int(date[4:])

    return (year, month, day, 0, 0, 0)

def date_validity(formatted_date):
    try:
        date(formatted_date[0], formatted_date[1], formatted_date[2])
    except ValueError:
        print str(formatted_date) + " is not a valid date"
        sys.exit()

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser(description="Outputs the number of days between 2 dates")
    p.add_argument('first_date', type=str, help="Enter the first date in the format [DDMMYYYY]")
    p.add_argument('second_date', type=str, help="Enter the second date in the format [DDMMYYYY]")
    
    options = p.parse_args()

    main(options)
