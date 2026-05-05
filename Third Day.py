import random 
a = random.randint(1,100)
b = int(input("Enter your guess !: "))
if b > a:
    print ("Higher")
elif b < a:
    print ("Lower")
else: 
    print ("Your guess was correct ! The number is: ", a)