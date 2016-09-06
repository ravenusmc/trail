from datetime import datetime
from datetime import timedelta
import pandas as pd


startdate = "3/1/1848"
enddate = pd.to_datetime(startdate) + pd.DateOffset(days=1)
print(startdate)
print(enddate)

startdate = "3/1/1848"
print(startdate)
x = 0

while x < 95:
  newDate = pd.to_datetime(startdate) + pd.DateOffset(days=x)
  print(newDate)
  x += 1





# month = "April"
# day = 1

# print(month, day, "1848")

# date = "1848-03-01"
# convertedDate = datetime.strptime(date, '%Y-%m-%d')
# end_date = convertedDate + datetime.timedelta(days=1)
# print(convertedDate)

# def calender(month):
#   months = ["March", "April", "May", "June", "July", "August"]
#   while True:
#     if month == "March":






# test = int(datetime.datetime(1848, 4, 1).strftime('%Y%m%d'))
# print(type(test))
# print(test + 1)

#This converts from Calender day to julian date. 
# fmt = '%Y.%m.%d'
# start = '1848.04.01'
# dt = datetime.datetime.strptime(start, fmt)
# tt = dt.timetuple()
# print(tt.tm_yday)

#Need to convert from Julian date back to calender date.
