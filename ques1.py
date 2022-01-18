ques1 = 'Python is a case sensitve language'
#A

print('(a) ' + str(len(ques1)))

#B
print('(b) reverse string: '+ ques1[::-1])
#C
c = ques1[10:25]
print('(c) ' + c)

#D
new_string = ques1[0:10] + 'object orientated' + ques1[25:]
print('(d) ' + new_string)

#E
index = ques1.index("a")
print('(e) index of "a" is ' + str(index))

#F
print('(f) {removing white spaces} : ' + ques1.replace(" ","") )