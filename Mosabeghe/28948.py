s = str(input())
l = list(s)
counter = 0
for items in l:
    if items == '=':
        counter = counter + 1


while counter>0:
    flag = 0
    for i in range(len(l)-1,-1,-1):
        if flag == 0 and l[i] == '=':
            flag = 1
            l[i] = '*'

        elif flag == 1 and l[i] != '=' and l[i] != '*' and (l[i+1] == '*' or l[i+1] == '='):
            l[i] = '*'
            flag = 0
            counter = counter - 1


result = ''
for items in l:
    if items != '*':
        result = result + items

print(result,end='')






