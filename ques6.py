a= int(input('length of side A: '))
b= int(input('length of side B: '))
c= int(input('length of side C: '))

if a+b<c:
    print('yes')
elif a+c<b:
    print('yes')
elif b+c<a:
    print('yes')
else:
    print('no')