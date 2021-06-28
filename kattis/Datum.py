# CPU: 0.06 s
from datetime import date
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day, month = map(int, input().split())
print(weekdays[date(2009, month, day).weekday()])

# CPU: 0.05 s
# 1st Jan 2009 -- Thursday
# day, month = map(int, input().split())
# prefix_sum = [31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
# weekdays = ["Wednesday", "Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday"]
# if month >= 2:
#     day += prefix_sum[month - 2]
# print(weekdays[day % 7])
