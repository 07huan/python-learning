def scores(cj):
    count = 0
    for score in cj:
        if score >= 60:
            count += 1
        
    return count
          
cj = [70,55,90,40,85]
result = scores(cj)
print(result)