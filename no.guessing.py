import random

number_to_guess= random.randint(1,100) 
while True:
 try:
  guess= int(input("Guess the number between 1 to 100: ") )   
  if guess < number_to_guess:
   print("Too Low!")
  elif guess > number_to_guess:
   print("Too High!")
  else:
   print("Congrats you guessed the correct number!")
   break
 except ValueError:    
  print("please enter a valid Number")