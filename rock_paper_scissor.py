import random
!pip install emoji
import emoji


# Define choices with emojis
choices = [
    ('r', emoji.emojize(':rock:', language='alias')),
    ('p', emoji.emojize(':page_facing_up:', language='alias')),
    ('s', emoji.emojize(':scissors:', language='alias')),
]

# Main game loop
while True:
    user_choice = input("Rock, Paper, or Scissors? (r/p/s): ").lower()
    if user_choice not in [choice[0] for choice in choices]:
        print("Invalid choice!")
        continue

    # Get computer's choice
    computer_choice = random.choice(choices)

    # Display choices
    user_emoji = next(emoji for key, emoji in choices if key == user_choice)
    print(f"You chose {user_emoji}")
    print(f"Computer chose {computer_choice[1]}")

    # Determine the winner
    if user_choice == computer_choice[0]:
        print("It's a draw!")
    elif (
        (user_choice == 'r' and computer_choice[0] == 's') or
        (user_choice == 'p' and computer_choice[0] == 'r') or
        (user_choice == 's' and computer_choice[0] == 'p')
    ):
        print("You win!")
    else:
        print("You lose!")

    # Ask if the user wants to continue
    should_continue = input("Do you want to continue? (y/n): ").lower()
    if should_continue == 'n':
        print("Thanks for playing!")
        break
