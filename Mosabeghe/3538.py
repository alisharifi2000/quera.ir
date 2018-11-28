l = [0,0,0,0,0,0,0]
counter = 0

n1 = int(input(''))
d1 = str(input(''))
n2 = int(input(''))
d2 = str(input(''))
n3 = int(input(''))
d3 = str(input(''))

d1 = d1.split(' ')
d2 = d2.split(' ')
d3 = d3.split(' ')

dtotal = d1+d2+d3

for items in dtotal:
    if items == 'shanbe':
        l[0] = 1
    elif items == '1shanbe':
        l[1] = 1
    elif items == '2shanbe':
        l[2] = 1
    elif items == '3shanbe':
        l[3] = 1
    elif items == '4shanbe':
        l[4] = 1
    elif items == '5shanbe':
        l[5] = 1
    elif items == 'jome':
        l[6] = 1

for items in l:
    if items == 0:
        counter = counter+1

print(counter,end='')
