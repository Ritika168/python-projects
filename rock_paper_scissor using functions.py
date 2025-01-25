import random
import emoji

def define_choices():
    #Define the game choices with emojis
    return [
        ('r', emoji.emojize(':rock:', language='alias')),
        ('p', emoji.emojize(':page_facing_up:', language='alias')),
        ('s', emoji.emojize(':scissors:', language='alias')),
    ]

def get_user_choice(choices):
    #Prompt the user to make a choice
    while True:
        user_choice = input("Rock, Paper, or Scissors? (r/p/s): ").lower()
        if user_choice in [choice[0] for choice in choices]:
            return user_choice
        print("Invalid choice! Please select 'r', 'p', or 's'.")

def get_computer_choice(choices):
    #Randomly select a choice for the computer
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    #Determine the outcome of the game
    if user_choice == computer_choice[0]:
        return "draw"
    elif (
        (user_choice == 'r' and computer_choice[0] == 's') or
        (user_choice == 'p' and computer_choice[0] == 'r') or
        (user_choice == 's' and computer_choice[0] == 'p')
    ):
        return "win"
    else:
        return "lose"

def display_choices(user_choice, computer_choice, choices):
    #Display the choices of the user and the computer
    user_emoji = next(emoji for key, emoji in choices if key == user_choice)
    print(f"You chose {user_emoji}")
    print(f"Computer chose {computer_choice[1]}")

def play_game():
    #Main function to play the game
    choices = define_choices()
    while True:
        user_choice = get_user_choice(choices)
        computer_choice = get_computer_choice(choices)

        display_choices(user_choice, computer_choice, choices)

        result = determine_winner(user_choice, computer_choice)
        if result == "draw":
            print("It's a draw!")
        elif result == "win":
            print("You win!")
        else:
            print("You lose!")

        # Ask if the user wants to play again
        should_continue = input("Do you want to continue? (y/n): ").lower()
        if should_continue == 'n':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_game()
