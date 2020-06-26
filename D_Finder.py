import datefinder
import re
import datetime


def date_check(segment1, segment2):
    def check_format(segment, date):
        str_date = datetime.datetime.strftime(date, '%d/%m/%Y')
        if len(re.findall(str_date, segment)) > 0:
            return True
        else:
            str_date = datetime.datetime.strftime(date, '%d.%m.%Y')
            if len(re.findall(str_date, segment)) > 0:
                return True
        return False

    matches1 = list(datefinder.find_dates(segment1))
    matches2 = list(datefinder.find_dates(segment2))
    if len(matches1) > 0 and len(matches2) > 0:
        date1 = matches1[0]
        date2 = matches2[0]
        if check_format(segment1, date1) is True and check_format(segment2, date2) is True:
            if date1 == date2:
                print("Date Format Correct")
            else:
                print("Date in both segments doesn't match")
        else:
            print("Date Found, But Not in expected format")
    else:
        print('No date found')


date_check("Hello!!! 29/06/1999", "29/06/1999")
