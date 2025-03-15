import random

def guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0

    print("Welcome to the Guessing Game!")
    print("Try to guess the number between 1 and 100.")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            if user_guess < 1 or user_guess > 100:
                print("Please guess a number between 1 and 100.")
            elif user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    guessing_game()
