import random

def start_game():
    print("\t\tGUESS THE NUMBER!! (0 TO 20)")
    number = random.randint(0, 20)
    ask_user(number, 4)  
    

def ask_user(num, chances):
    if chances == 0:
        print(f"Game Over! You've used all your chances. The correct number was {num}.")
        return
    
    user_input = int(input(f"\nYou have {chances} chance(s) left. Guess the number: "))
    
    if user_input != num:
        if user_input < num:
            print("Your guess is low!")
        else:
            print("Your guess is high!")
        
        ask_user(num, chances - 1)
    else:
        print(f"You guessed it right!! The number was {num}.")
        return


start_game()
