import random
computer_choices = ["Rock","Paper","Scssior"]
user_choice = int(input("press \n0 for Rock \n1 for Paper \n2 for Scssior\n"))

if user_choice != 0 and user_choice !=1 and user_choice !=2:
    print("Please enter a valid choice from 0,1,2")
else:
    print(f"user choose : {computer_choices[user_choice]} ")
    computer_choice= random.choice(computer_choices)
    print(f"computer choose : {computer_choice}")

    if(computer_choice=="Rock" and user_choice == 0) or (computer_choice=="Paper" and user_choice == 1) or (computer_choice=="Scssior" and user_choice == 2):
        print("match draw")

    elif (computer_choice =="Rock" and user_choice==2) or (computer_choice == "Paper" and user_choice == 0 ) or (computer_choice == "Sc2ssior" and user_choice ==1):
        print("You win this match")
    else:
         print("Computer win this match")
