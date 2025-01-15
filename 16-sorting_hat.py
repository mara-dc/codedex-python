# Write code below 💖

print('The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft')
print('and Wizardry. The hat decides which of the four "Houses" each first-year student')
print('goes to:')
print('🦁 Gryffindor')
print('🦅 Ravenclaw')
print('🦡 Hufflepuff')
print('🐍 Slytherin')

Gr = 0
Rv = 0
Hf = 0
Sl = 0

print(' ')

print('Q1) Do you like Dawn or Dusk?')
print('1) Dawn')
print('2) Dusk')

print(' ')

Q1 = int(input('Type 1 or 2: '))

if Q1 == 1:
  Gr += 1
  Rv += 1
elif Q1 == 2:
  Hf += 1
  Sl += 1
else:
  print('Wrong input')

print(' ')

print('Q2) When I’m dead, I want people to remember me as:')
print('1) The Good')
print('2) The Great')
print('3) The Wise')
print('4) The Bold')

print(' ')

Q2 = int(input('Type 1, 2, 3, or 4: '))

if Q2 == 1:
  Hf += 2
elif Q2 == 2:
  Sl += 2
elif Q2 == 3:
  Rv += 2
elif Q2 == 4:
  Gr += 2
else:
  print('Wrong input')

print(' ')

print('Q3) Which kind of instrument most pleases your ear?')
print('1) The violin')
print('2) The trumpet')
print('3) The piano')
print('4) The drum')

print(' ')

Q3 = int(input('Type 1, 2, 3, or 4: '))

if Q3 == 1:
  Sl += 4
elif Q3 == 2:
  Hf += 4
elif Q3 == 3:
  Rv += 4
elif Q3 == 4:
  Gr += 4
else:
  print('Wrong input')

print(' ')
print(' ')

house = max(Gr, Rv, Hf, Sl)
if house == Gr:
  print("You're a 🦁 Gryffindor!")
elif house == Rv:
  print("You're a 🦅 Ravenclaw!")
elif house == Hf:
  print("You're a 🦡 Hufflepuff!")
else:
  print("You're a 🐍 Slytherin!")
