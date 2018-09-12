"""datetime relativedelta Example.

Answer for: https://stackoverflow.com/q/52290952/1896134
Calculating number of years between two dates, but rounded in the standard way
"""
# from datetime import datetime
from datetime import date
from dateutil.relativedelta import relativedelta

almost_one_year_ago = (date.today() -
                       relativedelta(years=1) +
                       relativedelta(days=1)
                       )

# THIS IS WHAT YOU NEED to get one year.
almost_one_year_ago_wo_day = (date.today() -
                              relativedelta(years=1)
                              )

# print("Almost_one_year_ago: {}".format(almost_one_year_ago))
# print("Almost_one_year_ago_wo_day: {}".format(almost_one_year_ago_wo_day))
# print("Today Last Year: {}".format(date.today() - relativedelta(years=1)))
# print("Today Relativedelta 1: {}".format(date.today() -
#                                          relativedelta(days=1)))
# print("Today Relativedelta 0: {}".format(date.today() -
#                                          relativedelta(days=0)))

print(relativedelta(date.today(),
                    almost_one_year_ago).years)

print(relativedelta(date.today(),
                    almost_one_year_ago_wo_day).years)
