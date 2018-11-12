# task 1

with open('input.txt', 'r') as a:
    with open('output.txt','w') as b:
        for i in a:
            if (18 > (2018 - int(i[4]))):
                print (i[0], i[1], file = b, end='')
print()