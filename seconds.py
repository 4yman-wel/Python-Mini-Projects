x = input ('Enter the total seconds :\n')

x1 = int(x)

y = x1 // 60

s = x1 % 60
h = y // 60
m = y % 60

s_1 = str(s)
m_1 = str(m)
h_1 = str(h)
print('The time is : '+ h_1 +' hours and '+ m_1+ ' minutes and '+ s_1 +' seconds.')
  