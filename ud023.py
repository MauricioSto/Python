"""from datetime import date

def daysBetweenDates(y1, m1, d1, y2, m2, d2 ):
    dat1 = date(year1, month1, day1)
    dat2 = date(year2, month2, day2)
    return (dat2 - dat1).days

print(daysBetweenDates(1980,7,8,2017,12,15))
"""

def nextDay(year, month, day):
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """Returns the number of days between year1/month1/day1
       and year2/month2/day2. Assumes inputs are valid dates
       in Gregorian calendar, and the first date is not after
       the second."""

    # YOUR CODE HERE!
    if year2 == year1:
        day = 0
    else:
        day = (year2 - year1) * 360

    if month2 == month1:
        day = day
    if month2 > month1:
        day = day + ((month2 - month1)*30)
    else:
        day = day + (((12 - month1)+month2)*30)

    if day2 == day1:
        day = day
    if day2 > day1:
        day = day + (day2 - day1)
    else:
        day = day + ((30 - day1)+day2)

    return (day)


def test():
    test_cases = [((2012, 9, 30, 2012, 10, 30), 30),
                  ((2012, 1, 1, 2013, 1, 1), 360),
                  ((2012, 9, 1, 2012, 9, 4), 3)]

    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print ("Test with data:", args, "failed")
        else:
            print ("Test case passed!")


test()