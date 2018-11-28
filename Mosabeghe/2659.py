n = int(input())
word1 = str(input())
word2 = str(input())
counter = 0
for i in range(0,n):
    if(not(word1[i]== word2[i])):
        counter = counter + 1
print(counter,end="")
