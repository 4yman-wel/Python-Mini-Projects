x = int(input('Enter the total seconds :\n'))
y = x // 60
s = x % 60
h = y // 60
m = y % 60
print(f'The time is : {h} hours and {m} minutes and {s} seconds.')