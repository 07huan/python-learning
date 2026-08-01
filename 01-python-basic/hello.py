students = [
    {"name": "Amy", "score": 90},
    {"name": "Tom", "score": 40},
    {"name": "Tim", "score": 69},
    {"name": "Jerry", "score": 87}
]

total = 0
count = 0

with open("成绩报告.txt", "w") as file:
    for student in students:
        total += student["score"]

        if student["score"] >= 60:
            count += 1
            result = "合格"
        else:
            result = "不合格"

        file.write(
            f"{student['name']} 成绩：{student['score']} {result}\n"
        )

    average = total / len(students)

    file.write(f"合格人数：{count}人\n")
    file.write(f"平均分：{average}")