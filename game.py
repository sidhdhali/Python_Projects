name = input("Enter your name:")
print("Hello " + name + " Welcome to my game!")

should_we_play = input("Do you want to play? (yes/no) ").lower()


if should_we_play == "yes":    # or should_we_play=="y":
    print("we are gonna Play!")

    direction = input("do you want to go left or right? (left/right)").lower()
    if direction=="left":
        print("you went left and fell of a cliff , game over , try again.")

    elif direction=="right":
        choice = input("Okay , you now see a bridge , do you want to swim under it or cross it? (swim/cross) ")
        if choice == "swim":
            print("you got eaten by an alligator , you die , the End!")
        else:
            print(" you found the money and gold. You won!")
    
    else:
        print("Sorry not a valid reply , you die!")

else:
    print("we are not playing!")



