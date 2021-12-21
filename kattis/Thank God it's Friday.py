# CPU: 0.05 s
months = ("JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT",
    "NOV", "DEC")
weekdays = ("SUN", "MON", "TUE", 'WED', "THU", "FRI", "SAT")
prefix_sum = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)

day, month = input().split()
day = int(day)
month = months.index(month)
weekday_1st_jan = weekdays.index(input())

day_count = day - 1 + prefix_sum[month]
weekday = (weekday_1st_jan + day_count) % 7

if month > 1 and (weekday == 4 or weekday == 5):
    print("not sure")
elif weekday == 5:
    print("TGIF")
else:
    print(":(")
