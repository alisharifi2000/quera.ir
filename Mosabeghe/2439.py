def fact(n):
    if n < 1:
        return 1
    else:
        return n * fact(n - 1)


s = str(input(''))
s = s.split(' ')

n1 = int(s[0])
n2 = int(s[1])

r = fact(n1)
r = str(r)

counter = 0

for items in r:
    if int(items) == n2:
        counter = counter + 1

print(counter, end='')
