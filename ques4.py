print('enter three different numbers only')

a= str(int(input('number 1: ')))
b= str(int(input('number 2: ')))
c= str(int(input('number 3: ')))

if a<b:
    if b>c:
        print('greatest number is ' +b)
    else:
        print('greatest number is ' + c)

else:
    if a<c:
        print('greatest number is ' + c)
    else:
        print('greatest number is ' + a)



