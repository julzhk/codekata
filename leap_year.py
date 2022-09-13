def is_leap(year):
    if year % 100 == 0:
        return bool(year % 400 == 0)
    return bool(year % 4 == 0)


year = int(input())
print(is_leap(year))

assert is_leap(1990) == False
