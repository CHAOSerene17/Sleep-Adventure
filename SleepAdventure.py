x = "Yes"
y = "Maybe"
z = "No"

def print_lyrics():
  print("Så rå, lille mann,")
  print("Nå er dagen over.")

print("Are you sleepy?")
Answer1 = input()

if Answer1 == x:
  print("Would you like to read a song?")
  Answer2 = input()
  print_lyrics()

if Answer1 == y:
  print("Would you like a glass of milk?")
  Answer = input()
  if Answer == x:
    print("Let me make you some milk.")
  if Answer == y:
    print("I'll make my special Xanax milk.")
  if Answer == z:
    print("This isn't working out. I'll call you a UHAUL.")

if Answer1 == z: 
  print("Then leave me alone.")
  Answer3 = input()
  if Answer3 == z:
    print("Fine, we can watch a movie.")
  else:
    print("Okay, how about we get some dinner?")
