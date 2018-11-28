word = str(input())
w = word.split(" ")
n = int(w[0])
w1 =""
for i in range(0,n):
    w1 = w1 + "copy of "
wfinal = w1+w[1]
print(wfinal,end="")
