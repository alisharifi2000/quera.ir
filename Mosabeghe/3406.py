n1 = str(input(''))
new_n1 = (int(n1[2]))*100 + (int(n1[1]))*10 + (int(n1[0]))

n2 = str(input(''))
new_n2 = (int(n2[2]))*100 + (int(n2[1]))*10 + (int(n2[0]))

if new_n2 > new_n1:
   result = str(n1)+' '+'<'+' '+str(n2)
   print(result,end='')

elif new_n2 < new_n1:
    result = str(n2) + ' ' + '<' + ' ' + str(n1)
    print(result, end='')

else:
    result = str(n2) + ' ' + '=' + ' ' + str(n1)
    print(result, end='')
