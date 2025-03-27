from os import sys

"""05 number of days bw two dates"""
def check_leap_year(year):
    """определени високосного года"""
    if year % 400 == 0:
        #год, номер которого кратен 400, — високосный;
        return True
    elif year % 100 == 0:
        #остальные годы, номер которых кратен 100, — невисокосные
        return False
    elif year % 4 == 0:
        #остальные годы, номер которых кратен 4, — високосные
        return True
    return False #все остальные годы — невисокосные

def days_in_month(month, year):
    """кол-ва дней в месяце"""
    if month == 2:
        if check_leap_year(year):
            return 29
        else:
            return 28
    elif month < 8:
        if month % 2 == 0:
            return 30
        else:
            return 31
    else:
        if month % 2 == 0:
            return 31
        else:
            return 30

def bad_date(date: list):
    max_days = days_in_month(date[1], date[2])
    if max_days < date[0] or date[0] < 1:
        return True
    if date[1] > 12 or date[1] < 1:
        return True
    if date[2] < 1:
        return True
    return False

try:
    date_1 = input("Введите начальную дату в формате dd/mm/yyyy:  ").split("/")
    date_2 = input("Введите конечную датув формате dd/mm/yyyy:  ").split("/")
    for index, value in enumerate(date_1):
        date_1[index] = int(value)
    for index, value in enumerate(date_2):
        date_2[index] = int(value)

except:
    print("Требуется вводить даты в формате dd/mm/yyyy!")
    sys.exit(1)


if date_1[0] + date_1[1] + date_1[2] > date_2[0] + date_2[1] + date_2[2]:
    #если в обратно порядке даты указна, просто их переложим
    temp_list = date_1.copy()
    for index, value in enumerate(date_2):
        date_1[index] = int(value)
    
    for index, value in enumerate(temp_list):
        date_2[index] = int(value)

if bad_date(date_2) or bad_date(date_1):
    print("Некорректная дата")
    sys.exit(1)

days = 0 # кол-во дней между датами

if date_2[2] - date_1[2] > 0:
    #если прошел переход между годами
    year_loop = date_1[2]
    while year_loop < date_2[2]:
        if year_loop == date_1[2]:
            #посчитаем оставшиеся дни для текущего года
            month_loop = date_1[1]
            while month_loop <= 12:
                days += days_in_month(month_loop, year_loop)
                if month_loop == date_1[1]:
                    days -= date_1[0]
                month_loop += 1
        year_loop += 1
    #т.к. посчитали все дни до 1января целевого года, сбросим число
    date_1[2] = year_loop
    date_1[1] = 1
    date_1[0] = 0

month_loop = date_1[1]
while month_loop <= date_2[1]:
    days += days_in_month(month_loop, date_1[2])
    if month_loop == date_1[1]:
        days -= date_1[0]
    if month_loop == date_2[1]:
        days -= (days_in_month(month_loop, date_1[2]) - date_2[0])
    month_loop += 1
print(days)
