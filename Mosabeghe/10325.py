s = str(input(''))
s = s.split(' ')

r = int(s[0])
c = int(s[1])

if 1 <= c <= 10:
    dr = 10 - r + 1
    dc = c
    result = 'Right ' + str(dr) + ' ' + str(dc)
    print(result, end='')
else:
    dr = 10 - r + 1
    dc = 20 - c + 1
    result = 'Left ' + str(dr) + ' ' + str(dc)
    print(result, end='')
