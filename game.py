#!/usr/bin/env python3
"""
Number Guessing Game
A simple interactive game where you guess a random number between 1 and 100.
"""

import random


def play_game():
    """Main game function."""
    print("=" * 50)
    print("Welcome to the Number Guessing Game!")
    print("=" * 50)
    print("\nI'm thinking of a number between 1 and 100.")
    print("Can you guess what it is?\n")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        try:
            # Get user input
            guess = input(f"Attempt {attempts + 1}/{max_attempts} - Enter your guess: ")
            guess = int(guess)
            
            # Validate input range
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100!")
                continue
            
            attempts += 1
            
            # Check the guess
            if guess < secret_number:
                print("📈 Too low! Try a higher number.\n")
            elif guess > secret_number:
                print("📉 Too high! Try a lower number.\n")
            else:
                print(f"\n🎉 Congratulations! You guessed it!")
                print(f"The number was {secret_number}")
                print(f"It took you {attempts} attempt(s)!")
                
                # Rating based on attempts
                if attempts <= 3:
                    print("⭐⭐⭐ Amazing! You're a guessing master!")
                elif attempts <= 6:
                    print("⭐⭐ Great job! You're pretty good at this!")
                else:
                    print("⭐ Good work! You got it!")
                return True
                
        except ValueError:
            print("Invalid input! Please enter a valid number.\n")
            continue
        except KeyboardInterrupt:
            print("\n\nGame interrupted. Thanks for playing!")
            return False
    
    # Out of attempts
    print(f"\n😔 Game Over! You've used all {max_attempts} attempts.")
    print(f"The number was {secret_number}. Better luck next time!")
    return False


def main():
    """Main entry point for the game."""
    while True:
        won = play_game()
        
        # Ask if player wants to play again
        print("\n" + "-" * 50)
        play_again = input("Would you like to play again? (yes/no): ").lower()
        
        if play_again not in ['yes', 'y']:
            print("\nThanks for playing! Goodbye! 👋")
            break
        print("\n")


if __name__ == "__main__":
    main()
