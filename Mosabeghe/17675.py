def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return fib(n - 1) + fib(n - 2)


num = int(input(''))

list = []
temp_list = []
temp = 1

for i in range(0, num):
    list.insert(len(list), '-')

while fib(temp) <= num:
    temp_list.insert(len(temp_list), fib(temp))
    temp = temp + 1

for items in temp_list:
    list[items - 1] = '+'

for i in range(0, len(list)):
    print(list[i], end='')
