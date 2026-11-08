x =int(input('enter number of secondes:'))
hours = x // 3600
minutes = (x % 3600) // 60
secondes = x % 60
print(f'the time is {hours} hours and {minutes} minutes and {secondes} secondes.')

