import random
print("I am thinking of a number between 1 and 100...")
a = random.randint(1,100)
attempts = 0
while True:
    b = int(input("Enter your guess!: "))
    attempts = attempts + 1
    
    if b == a:
        print("Correct! The number was:", a)
        print("You guessed it in", attempts, "attempts!")
        break

    if attempts > 7:
        print("Game Over! The number was:", a)
        break

    if b > a:
        print("Too high!")
    else:
        print("Too low!")