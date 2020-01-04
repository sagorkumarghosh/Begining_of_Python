month_days = [0, 31, 28, 31, 30, 31, 30, 31, 30, 31, 31, 30, 31]
def year(y):
    return y % 4 == 0
    #print("{}, is leap year".format(y))
    #else:
     # print("{}, is not leap year".format(y))

def days_in_month(y, month):
    #if not 1 <= month <= 12:
    if month <= 1 or month >=12:
        return "Invalid Month"
    if month == 2 and year(y):
        return 29

    return month_days[month]

print(days_in_month(2021, 2))
