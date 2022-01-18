a = 56
b = 10
print('bitwise a = 56')
print('bitwise b = 10')
print("(a) a&b : " + str(a&b))

print("(b) a|b : " + str(a|b))

print("(c) a^b : " + str(a^b))


leftshift_a = a<<2
leftshift_b= b<<2
print('(d) left-shift of bitwise operator a : ' + str(leftshift_a) + ' and left-shift of bitwise operator b : ' + str(leftshift_b))

rightsift_a = a>>2
rightshift_b = b>>4
print('(e) right-shift of a by 2:' + str(rightsift_a) + ' and right-shift of b by 4: '+ str(rightshift_b))