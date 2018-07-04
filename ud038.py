# calculo de horas em um dia
def hours2days(h):
    days = 0
    hours = 0
    if h < 24:
        days = 0
        hours = h
    else:
        days = h // 24
        hours = h % 24
    return days, hours

print(hours2days(10000))
print(hours2days(24))
print(hours2days(25))