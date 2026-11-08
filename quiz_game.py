print("Salam! Marhba bik f l Quiz Game 🧠")
print("Ghadi nsawlouk 5 as2ila, w njarbo ch7al 3andek m3rifa!")

score = 0

# Question 1
jawab1 = input("1) Chno hiya l3asima dyal Maroc? ")
if jawab1.lower() == "rabat":
    print("Sahiiih! ✅")
    score += 1
else:
    print("Ghalat ❌, l jawb sa7i7 howa: Rabat")

# Question 2
jawab2 = input("2) Ch7al 3andna men continent f l3alam? ")
if jawab2 == "7":
    print("Zwin! ✅")
    score += 1
else:
    print("La la... howa 7 ❌")

# Question 3
jawab3 = input("3) Wach Python hiya langage de programmation? (ah / la) ")
if jawab3.lower() == "ah":
    print("Bravo! ✅")
    score += 1
else:
    print("Non! Python hiya langage! ❌")

# Question 4
jawab4 = input("4) Chno smit rass l3am f l calendrier miladi? ")
if jawab4.lower() == "janvier":
    print("Tbarkellah 3lik ✅")
    score += 1
else:
    print("Ghalat ❌, howa: Janvier")

# Question 5
jawab5 = input("5) Wach 2 + 2 = 4? (ah / la) ")
if jawab5.lower() == "ah":
    print("Nta brilliant ✅")
    score += 1
else:
    print("Ewa daba!? ❌")

# Resultat
print("\n✅✅✅ L jeu tsala!")
print("Jbt", score, "men 5")
if score == 5:
    print("Champion! 🏆")
elif score >= 3:
    print("Mezyan bzaf! 🔥")
else:
    print("Khasك tzid t9ra shwiya 😉")
