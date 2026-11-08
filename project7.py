x = input ('Enter the total seconds :\n')

x1 = int(x)

y = x1 // 3600
print(y)

t = x1 // 60
print(t)



r = x1 % 60
print(r)

print('Your score is '+str(y)+ ' hours and '+str(t)+ ' minutes and '+str(r) +' seconds.')
