# Leap year
def is_leap_year(year):
    result = 0
    if year % 4 == 0:
        if not year % 100 == 0 or year % 400 == 0:
            result = 1
    if result:
        return True
    return False


def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid month"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap_year(year):
        return 29
    return month_days[month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
