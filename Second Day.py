n = input("Enter your name:")
a = int(input("Enter your age:"))
t = int(input("How many years in the future ?:"))
na = a + t
if 100 > na > 60 or na == 60:
    print ("You wil be very wise.")
elif na > 100 or na == 100:
    print ("Are you an immortal ?")