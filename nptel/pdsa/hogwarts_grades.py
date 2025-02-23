import sys

def disp_list(lst):
    for student in lst:
        print (student[0], student[1], student[2], sep='~')

courses_list, students_list, grades_list = list(), list(), list()
ret_list = list()
grades_dict = {'A':10, 'AB':9, 'B':8, 'BC':7, 'C':6, 'CD':5, 'D':4}
students_dict = dict()

courses_prompt = input()
if courses_prompt != "Courses":
    sys.exit()
    
courses_input = input()
while courses_input != "Students":
    courses_tuple = courses_input.split("~")
    courses_list.append(courses_tuple)
    courses_input = input()    

students_input = input()
while students_input != "Grades":
    students_tuple = students_input.split("~")
    students_list.append(students_tuple)
    students_input = input()    

grades_input = input()
while grades_input != "EndOfInput":
    grades_tuple = grades_input.split("~")
    grades_list.append(grades_tuple)
    grades_input = input()    

for student in students_list:
    students_dict[student[0]] = (student[1], 0, 0)

for grade in grades_list:
    student = students_dict[grade[3]]
    students_dict[grade[3]] = (student[0], student[1]+1, student[2]+grades_dict[grade[4]])

for student in students_list:
    vals = students_dict[student[0]]
    if vals[1] != 0:
        students_dict[student[0]] = (vals[0], vals[1], round(vals[2]/vals[1], 2))
    else:
        students_dict[student[0]] = (vals[0], vals[1], 0)
    vals = students_dict[student[0]]
    ret_list.append ( ( student[0], vals[0], vals[2] ) )
ret_list.sort(key=lambda x:x[0])
disp_list( ret_list )
