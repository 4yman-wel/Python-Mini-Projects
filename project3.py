print('Salam akhi lyoum ghanswlek des questions 3la La Boite a Merveille :')
print("lets gooo")

score = 0

#1
a =    input("Chno smit lkatiib dyal le roman?\n")
if a.lower() == 'ahmed sefrioui' :
    print('M9awwed')
    score +=1
else :
    print('la ghalat,Ahmed sefrioui')

#2
b = int(input('Achmen 3am tktbat fih?\n'))
if b == 1952: 
    print("M9awwed")
    score +=1
else:
    print('You lose ')

#result
print('THe quiz complete')
print('You score is '+ str(score) + ' men 2')

if score==2  :
    print('good job man')
elif score==1 :
    print('la ba2ss bih')
else:
    print('sir 9ra 3la kerrek....')
