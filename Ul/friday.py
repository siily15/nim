import datetime

def has_friday_13(month, year):
    d = datetime.datetime(year, month, 13)
    date_as_weekday_number = d.strftime('%w')
    if date_as_weekday_number == "5":
        return True
    else:
        return False

print(has_friday_13(11, 2020))
