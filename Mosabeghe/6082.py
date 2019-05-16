l = str(input())
l = l.split(' ')
n = int(l[0])
m = int(l[1])

counter = 0

for i in range(0,n):
    line = str(input())
    lines = list(line)
    for items in lines:
        if items == '*':
            counter = counter + 1

print(counter,end='')

