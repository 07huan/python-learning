scores = [70, 55, 90, 40, 85]
for score in scores:
    print(score)
count=0
for score in scores:
    if score >= 60:
        print(score,"合格")
        count += 1
    else:
        print(score,"不合格")

print(f"合格人数为：{count}")