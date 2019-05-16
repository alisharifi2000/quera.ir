l = str(input())
l = l.split(' ')
result = l
list = []
for i in range(0, len(l)):
    list.insert(len(list), int(l[i]))

if list[0] > 1:
    result[0] = 1 - list[0]
elif list[0] <= 1:
    result[0] = 1 - list[0]

if list[1] > 1:
    result[1] = 1 - list[1]
elif list[1] <= 1:
    result[1] = 1 - list[1]

if list[2] > 2:
    result[2] = 2 - list[2]
elif list[2] <= 2:
    result[2] = 2 - list[2]

if list[3] > 2:
    result[3] = 2 - list[3]
elif list[3] <= 2:
    result[3] = 2 - list[3]

if list[4] > 2:
    result[4] = 2 - list[4]
elif list[4] <= 2:
    result[4] = 2 - list[4]

if list[5] > 8:
    result[5] = 8 - list[5]
elif list[5] <= 8:
    result[5] = 8 - list[5]

s = ''
for i in range(0,len(result)):
    if i == 0:
        s = str(result[i])
    else:
        s = s + ' ' + str(result[i])
print(s,end='')
