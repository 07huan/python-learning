students =[
    {"name":"john","score":60},
    {"name":"amy","score":94},
    {"name":"mike","score":78},
    {"name":"jane","score":85}
]

def show_student(students):
    for student in students:
        print(f"学生名单{student['name']}")

def hege(students):
    for student in students:
        if student["score"] >=60:
            print(f"{student['name']}同学及格了")    

def calculate_average(students):
    total = 0
    for student in students:
        total += student["score"]             
    average = total / len(students)
    print(f"平均成绩是{average}")

def count_fail(students):
    no = 0

    for student in students:
        if student["score"] < 60:
            no += 1
            print(f"{student['name']}同学不及格。")

    print(f"所以不合格的人数为：{no}")

def main():
    show_student(students)
    hege(students)
    calculate_average(students)
    count_fail(students)
main()