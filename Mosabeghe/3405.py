list = []
n = int(input(''))

while n!=0:
    list.insert(len(list), n)
    n = int(input(''))

size = len(list)

if size>0:
    for i in range(1, size):
        print(list[size-i])
    print(list[0], end='')
