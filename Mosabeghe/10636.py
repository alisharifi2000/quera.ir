n =  int(input())
list = []
for i in range(0,n):
    w = str(input())
    word = w.split(" ")
    list.insert(len(list),word[0])
listc =[]
counter = 1
for i in range(0,len(list)):
    for j in range (i+1,len(list)):
        if(list[i] == list[j]):
            counter = counter + 1

    listc.insert(len(listc),counter)
    counter = 1
m = listc[0]
for k in range(1,len(listc)):
    if(listc[k]>= m):
        m = listc[k]

print(m,end="")
