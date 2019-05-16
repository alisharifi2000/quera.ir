s = str(input(''))

counter_r = 0
counter_y = 0
counter_g = 0

for items in s:
    if items == 'R':
        counter_r = counter_r + 1
    elif items == 'Y':
        counter_y = counter_y + 1
    elif items == 'G':
        counter_g = counter_g + 1

if counter_g == 0 or counter_r >= 3 or (counter_r >= 2 and counter_y >= 2):
    print('nakhor lite', end='')
else:
    print('rahat baash', end='')
