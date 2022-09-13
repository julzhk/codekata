import re
from collections import namedtuple

if __name__ == '__main__':
    no_students, col_names = int(input()) , re.split(r'\s{2,}', input())
    StudentData = namedtuple('StudentData', ','.join(col_names))
    students = [StudentData(*(re.split(r'\s{2,}', input()))) for _ in range(no_students)]
    print(sum([float(student.MARKS) for student in students]) / no_students)
