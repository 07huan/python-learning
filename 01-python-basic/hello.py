scores = [60, 75, 88, 92, 55]

for score in scores:
    if   60 <= score <= 70:
        print(score,"及格")
    elif 70 < score < 100 :
        print(score,"优秀")
    else:
        print(score,"不合格")