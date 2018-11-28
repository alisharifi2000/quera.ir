import math

lx = []
ly = []
lsum = []

s = str(input(''))
s = s.split(' ')

n = int(s[0])
x = int(s[1])
y = int(s[2])

min_in = min(x,y)

for i in range(0, math.floor(n / min_in)+1):
    r = n - i * x
    if r == 0:
       lx.insert(len(lx),i)
       ly.insert(len(ly),0)

    elif r % y == 0:
        lx.insert(len(lx), i)
        ly.insert(len(ly), int(r / y))

size = len(lx)

if size == 0:
    print('-1', end='')
else:
    for i in range(0, size):
        sum = lx[i] + ly[i]
        lsum.insert(len(lsum), sum)

    index = 0
    m = lsum[0]
    for i in range(1, size):
        if m >= lsum[i]:
            m = lsum[i]
            index = i

    print(str(lx[index]) + ' ' + str(ly[index]), end='')
