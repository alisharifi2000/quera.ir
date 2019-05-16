import math

n1 = int(input(''))
n2 = int(input(''))

result = []

if n1 >= n2:
    for val in range(n2, n1 + 1):
        if val > 1:
            for n in range(2, val):
                if (val % n) == 0:
                    break
            else:
                result.insert(len(result),val)

else:
    for val in range(n1, n2 + 1):
        if val > 1:
            for n in range(2, val):
                if (val % n) == 0:
                    break
            else:
                result.insert(len(result),val)

for i in range(0,len(result)):
    if i == len(result) - 1:
        print(result[i],end='')
    else:
        print(result[i])

