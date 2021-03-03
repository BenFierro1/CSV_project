import csv
from datetime import datetime

open_file = open("sitka_weather_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

open_file2 = open("death_valley_2018_simple.csv", "r")
csv_file2 = csv.reader(open_file2, delimiter=",")
header_row2 = next(csv_file2)

for index, column_header in enumerate(header_row):
    print("Index:", index, "Column Name:", column_header)


highs_sitka = []
lows_sitka = []
dates_sitka = []
highs_dv = []
lows_dv = []
dates_dv = []

for row in csv_file:
    highs_sitka.append(int(row[5]))
    lows_sitka.append(int(row[6]))
    converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    dates_sitka.append(converted_date)

for row in csv_file2:
    try:
        high = int(row[4])
        low = int(row[5])
        converted_date = datetime.strptime(row[2], "%Y-%m-%d")
    except ValueError:
        print(f"missing data for {converted_date}")
    else:
        highs_dv.append(high)
        lows_dv.append(low)
        dates_dv.append(converted_date)


import matplotlib.pyplot as plt


fig, a = plt.subplots(2, 1)

fig.autofmt_xdate()

a[0].plot(dates_sitka, highs_sitka, c="red")
a[0].plot(dates_sitka, lows_sitka, c="blue")

a[0].fill_between(dates_sitka, highs_sitka, lows_sitka, facecolor="blue", alpha=0.1)

a[0].set_title("SITKA AIRPORT, AK US", fontsize=8)
plt.xlabel("", fontsize=6)
plt.ylabel("", fontsize=6)
plt.tick_params(axis="both", which="major", labelsize=8)

fig.autofmt_xdate()

a[1].plot(dates_dv, highs_dv, c="red")
a[1].plot(dates_dv, lows_dv, c="blue")

a[1].fill_between(dates_dv, highs_dv, lows_dv, facecolor="blue", alpha=0.1)

a[1].set_title("DEATH VALLEY, CA US", fontsize=8)

fig.suptitle(
    "Temperature Comparison Between SITKA AIRPORT, AK US and DEATH VALLEY, CA US",
    fontsize=7,
)
plt.show()


# fig2, a = plt.subplots(2)

# a[0].plot(dates, highs, c="red")
# a[1].plot(dates, lows, c="blue")

# plt.show()
