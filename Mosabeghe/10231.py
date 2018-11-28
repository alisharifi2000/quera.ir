list = []
for i in range(0, 5):
    s = str(input(''))
    list.insert(len(list), s)

r = []
counter = 0
for items in list:
    if ('MOLANA' in items) or ('HAFEZ' in items):
        r.insert(len(r), counter)
    counter = counter + 1

size = len(r)
s = ''
if size == 0:
    print('NOT FOUND!', end='')
else:
    for i in range(0, size):
        if i != 0:
            s = s + ' ' + str(r[i] + 1)
        else:
            s = s + str(r[i] + 1)
    print(s, end='')
