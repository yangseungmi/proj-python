import random

result = []
while len(result) < 6:
    n = random.randint(1,45)
    if n not in result :
        result.append(n)


print(result)


