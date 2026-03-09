import random

class Guesser:
    def __init__(self, low=1, high=20):
        self.secret = random.randint(low, high)
        self.low = low
        self.high = high
        self.guesses_left = 4
        self.hints_left = 3
    
    def get_hint_a(self):
        factors = [i for i in range(1, self.secret +1) if self.secret % i == 0]
        multiple = self.secret * random.randint(2, 5)
        choice = random.choice(["factor", "multiple"])
        if choice == "factor" and factors:
            return f"A factor of the number is {random.choice(factors)}."
        else:
            return f"A multiple of the number is {multiple}."

    def get_hint_b(self): 
        options = []
        if self.secret > self.low:
            options.append(("smaller", random.randint(self.low, self.secret - 1)))
        if self.secret < self.high:
            options.append(('larger', random.randint(self.secret + 1, self.high)))
        hint_type, val = random.choice(options)
        return f"A number {hint_type} than the secret is {val}."

    def get_hint_c(self): 
        result = "even" if self.secret % 2 == 0 else "odd"
        return f"The number is {result}."

# chatbot
def start_chatbot():
    game = Guesser(1, 20)
    print(f"Hi! I've guessed a number between {game.low} and {game.high}.")
    print(f"You have {game.guesses_left} guesses. Good luck!")

    while game.guesses_left > 0:
        user_input = input("\nEnter your guess (or type 'hint'): ").lower().strip()

        if user_input == "hint":
            if game.hints_left > 0:
                category = random.choice(['a', 'b', 'c'])
                if category == 'a': print(game.get_hint_a())
                elif category == 'b': print(game.get_hint_b())
                else: print(game.get_hint_c())
                game.hints_left -= 1
            else:
                print("Sorry, you are out of hints!")
        else:
            try:
                guess = int(user_input)
                if guess == game.secret:
                    print("Congratulations! You guessed it right!")
                    return
                else:
                    game.guesses_left -= 1
                    if game.guesses_left > 0:
                        print(f"Wrong! Remember: you can request a hint by typing 'hint'.")
            except ValueError:
                print("Please enter a valid number or 'hint'.")

        print(f"Status: {game.guesses_left} guesses and {game.hints_left} hints remaining.")

    print(f"\nGame Over! The number was {game.secret}.")

if __name__ == "__main__":
    start_chatbot()
