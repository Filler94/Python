secret_number = 777

print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")
number_guess = int(input("Ener your guess: "))

while number_guess != 777:
    print("Ha ha! You're stuck in my loop!")
    number_guess = int(input("Enter another guess: "))

else:
    print("Well done, muggle! You are free now.", number_guess)