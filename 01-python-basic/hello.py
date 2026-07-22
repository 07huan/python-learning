scores = [80, 90, 70, 60]
def average(x):
    total = 0
    for score in x:
        total = total + score
    return total / len(x)

print(average(scores))