import random


class GuessNumberGame:
    def __init__(self, low=1, high=100):
        self.low = low
        self.high = high
        self.target = random.randint(low, high)
        self.attempts = 0

    def get_user_input(self):
        while True:
            try:
                guess = int(input(f"Enter a number ({self.low}-{self.high}): "))
                if self.low <= guess <= self.high:
                    return guess
                else:
                    print("Out of range. Try again.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def check_guess(self, guess):
        self.attempts += 1
        if guess < self.target:
            return "low"
        elif guess > self.target:
            return "high"
        else:
            return "correct"

    def play(self):
        print("🎯 Welcome to Guess Number Game!")
        print(f"I'm thinking of a number between {self.low} and {self.high}.")

        while True:
            guess = self.get_user_input()
            result = self.check_guess(guess)

            if result == "low":
                print("Too low!")
            elif result == "high":
                print("Too high!")
            else:
                print(f"🎉 Correct! You guessed it in {self.attempts} attempts.")
                break


if __name__ == "__main__":
    game = GuessNumberGame()
    game.play()
