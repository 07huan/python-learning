students = [
    {"name": "amy", "score": 90},
    {"name": "john", "score": 70},
    {"name": "tom", "score": 49},
    {"name": "jim", "score": 90}
]

def calculate_total(students):
    total = 0

    for student in students:
        total += student["score"]

    return total / len(students)


print(calculate_total(students))