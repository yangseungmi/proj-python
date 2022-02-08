"""
data = "4546793"

numbers = list(map(int,data))
result = []

for i, num in enumerate(numbers):
    result.append(num)
    if i < len(numbers)-1:
        is_odd = num%2 == 1
        is_next_odd = numbers[i+1]%2 == 1
        if is_odd and is_next_odd:
            result.append('-')
        elif not is_odd and not is_next_odd:
            result.append('*')
       
print(result)
print("".join(result))
"""

print("".join(['4','ㄱ','6']))
print("".join(['4',5]))