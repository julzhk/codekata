# save actual stdin in case we need it again later

STD_IN = [
    '08 05 2015',
]


def input():
    return STD_IN.pop(0)


import calendar

if __name__ == '__main__':
    month, day, year = map(int, input().split(' '))
    days = ['MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', 'SUNDAY']
    day_index = (calendar.weekday(year, month, day))
    print(days[day_index])
