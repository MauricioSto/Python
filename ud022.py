#!/usr/bin/env python
# Calculo dos dias de vida
def nextDay(year, month, day):
    """
    if day < 30:
        return year, month, day + 1
    else:
        if month < 12:
            return year, month + 1, 1
        else:
            return year + 1, 1, 1

    Returns the year, month, day of the next day.
    Simple version: assume every month has 30 days.
    """
    # YOUR CODE HERE

    if day >= 30:
        day = 1
        month = month + 1
        if month >= 12:
            month = 1
            year = year + 1
        return year, month, day
    else:
        day = day + 1
        month = month
        year = year
        return year, month, day


print (nextDay(1999, 12, 30))
print (nextDay(2013, 1, 30))
print (nextDay(2012, 12, 30))