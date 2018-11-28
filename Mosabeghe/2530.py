word = str(input(''))
p =1
for items in word:
    if(items == "D"):
        p = p*2
    elif(items == "L"):
        p = p*2
    elif(items == "T"):
        p = p*2
    elif(items == "F"):
        p = p*2
print(p,end='')
