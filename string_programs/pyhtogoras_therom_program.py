import math
print ('Enter "-" to find the length of a side')
a = int(input("Enter the length of the side \"a\" of the triangle : "))
b = int(input("Enter the length of the side \"b\" of the triangle : "))
c = int(input("Enter the length of the side \"c\" of the triangle : "))
if a == "x" :
    a_square = int(c ** 2) - int(b ** 2)
    print('The value of "x" is : ',math.sqrt(a_square))
elif b == "x" :
    b_square = int(c ** 2) - int(a ** 2)
    print('The value of "x" is : ',math.sqrt(b_square))
elif c == "x" :
    c_square = int(a ** 2) + int(b ** 2)
    print('The value of "x" is : ',math.sqrt(c_square))