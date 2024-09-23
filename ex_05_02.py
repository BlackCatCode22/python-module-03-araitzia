
num = 0
tot = 0.0
largest = 0
smallest = 0

while True:
    sval = input ('Enter a number: ')
    if sval =='done':
        break
    try:
        fval = float(sval)
        if fval > largest:
            largest = fval
        elif fval < smallest:
            smallest = fval
    except:
        print('Invalid input')
        continue
    print (fval)
    num = num + 1
    tot = tot + fval

print ('ALL DONE')
print(tot,num,largest,smallest)











