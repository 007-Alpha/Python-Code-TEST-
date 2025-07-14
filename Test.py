import random
numbers = rtandom.randint(1,100)
attempts=0
while True:
  Guess=input("Guess a number between 1 and 100: ")
  if not guess.sidigit():
    print("Print enter a valid number.")
continue
guess=int(guess)
attempts +=1

if guess<number:
  print("Too Low")
elif guess>number:
  print("Too High")
else:
  print(f"Congrats! You have guessed it right in {attempts}")
  break
