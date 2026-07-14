# Treasure hunt 
print("Welcome to Treasure island")
print("Your mission is to find the treasure." )
choice1 = input("Choose 'Left' or 'Right'?").lower()

if choice1 == "left":
    print("You reached the lake.")

    choice2 =input("Swim or Wait?").lower()
    if choice2 == "wait":
        print("You reached the island")

        choice3 = input("choose a color 'Red' , 'Yellow', 'Blue'").lower()
        if choice3 == "yellow":
            print("You got the the treasure!You win")
        else:
            print("Game over")
    else:
        print("Game over")
else:
    print("Game over")