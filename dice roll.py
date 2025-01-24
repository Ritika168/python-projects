import random 

while True:  #loop
 choice = input("roll a dice(y/n): ").lower()
 if choice == "y"    :#ask roll a dice

   die1= random.randint(1,6)  #if users enter y generate 2 random nos.
   die2= random.randint(1,6)
   print(f'({die1},{die2})')   #print them

 elif choice=="n":  #if users enter n print thank you message

    print("Thanks for playing!")

    break  #terminate

 else:    #else print invalid choice

    print("Invalid choice!")