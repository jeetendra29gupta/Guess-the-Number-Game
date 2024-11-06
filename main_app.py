import random


class GuessNumberGame:
    def __init__(self):
        # Generate a random number between 1 and 100
        self.target_number = random.randint(1, 100)
        self.attempts = 0

    def check_guess(self, guess):
        """Check if the user's guess is correct."""
        if guess < self.target_number:
            return "Your guess is too low."
        elif guess > self.target_number:
            return "Your guess is too high."
        else:
            return f"Congratulations! You guessed the correct number in {self.attempts} attempts!"

    def start_game(self):
        """Start the game loop."""
        print("Welcome to the Guess the Number Game!")
        print("I have selected a number between 1 and 100.")
        print("Can you guess what it is?")

        while True:
            try:
                # Get the user's guess
                guess = int(input("Enter your guess: "))
                self.attempts += 1

                # Check if the guess is correct
                result = self.check_guess(guess)
                print(result)

                # If the guess is correct, break the loop and end the game
                if guess == self.target_number:
                    break
            except ValueError:
                print("Invalid input! Please enter a valid integer.")


# Running the game
if __name__ == "__main__":
    game = GuessNumberGame()
    game.start_game()
