import csv
from datetime import datetime

open_file = open("sitka_weather_07-2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

# the enumerate() function returns both the index of each item adn the value of each
# item as you loop through a list

for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)

highs = []
dates = []

# as an example
# my_date = "2018-07-01"
# converted_date = datetime.strptime(my_date, "%Y-%m-%d")
# print(converted_date)

# We call the method strptime() using the string containing the date we want to work with
# as its first argument. The second argument tells python how the date is formatted.
# In this example, Python interperts "%Y-" to mean the part of the string before the first
# dash is a four-digit year; "%m-" means the part of the string before the second dash is
# number representing the month; and "%d" means the last part of the string is the day of
# month, from 1 to 31.

for row in csv_file:
    highs.append(int(row[5]))
    converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates.append(converted_date)

# print(highs)

# plot highs on a chart

import matplotlib.pyplot as plt


fig = plt.figure()

plt.plot(dates, highs, c="red")

# The call fig.autofmt_xdate() draws the date labels diagonally to prevent them from overlapping

fig.autofmt_xdate()

plt.title("Daily High Temperatures, July 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

plt.show()
