import random

# The random module allows Python to generate random values.

# random.randint()
# Generate a random integer within a range
num = random.randint(1,10)
print(num)

# random.choice()
# selects a randon items from list
fruits = ["apple", "banana", "cherry"] # List
print(random.choice(fruits))


# random.random()
# Generates a random decimal number between 0 and 1
print(random.random())

# random.shuffles()
# Shuffles items in a list

cards = ["Kings","Queen","Jack"]
random.shuffle(cards)
print(cards)


# random.uniform()
# Generate a random decimal number between two values.
print(random.uniform(1,10))

# Mini Game: Coin Toss
result = random.choice(["Head","Tail"])
print(result)

# Guessing Game
number = random.randint(1,20)
print(number)
guess = int(input("Guess the lucky number (1-20)"))
if guess == number:
    print("Congrats you just won a Trip to Paris ")
else:
    print("Go back home buddy")

# 5 trails (Loops)
# Hints (Conditional statement)
# prize and Attempts deduction (assigment operator)

number = random.randint(1,20)
attempt = 5
prize = 1000000
guess = int(input("Guess the lucky number (1-20)"))

while attempt != 1:
    attempt -= 1
    if number == guess:
        print(f"Congratulations you just won ${prize:,}")
        break
    elif guess > number:
        prize -= 100000
        print("Too high")
        print(f"You have {attempt} attempts left and your prize has been reduced to ${prize:,}")
        guess = int(input("Try again:"))
    elif guess < number:
        prize -= 100000
        print("Too low")
        print(f"You have {attempt} attempts and your prize has been reduced to ${prize:,}")
        guess = int(input("Try again:"))

print("Game ended")














