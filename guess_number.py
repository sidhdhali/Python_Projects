# guess the number



import random

randNum = random.randint(1,100)
#print(randNum)

while True:
    userNum = int(input("enter a number or to Quit , enter a Q : "))

    if(userNum == "Q"):
        break
    
    userNum = int(userNum)

    if(randNum == userNum):
        print("you guess it correct.....")
        break

    elif(userNum < randNum):
        print("you have guessed it too small , guess bigger one")

    else:
        print("you have guessed it too big , guess it smaller ")

print("---game over-----")
