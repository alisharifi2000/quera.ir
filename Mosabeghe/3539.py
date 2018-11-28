num = str(input(''))
sum = 0
for items in num:
    sum = sum + int(items)
    if(sum>=10):
        n = str(sum)
        s = 0
        for item in n :
            s = s + int(item)
        sum = s

print(sum)
