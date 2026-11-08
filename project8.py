x = input('Enter type length :\n')
y = input('Enter type width :\n')
t = input('How much for 1 metre? \n')

int_x = float(x)
int_y = float(y)
int_t = float(t)
area = (int_x * int_y)
price = (int_t * area)

print('The total area is: ' +str( area))
print('Give the guy :$' + str(price ))
