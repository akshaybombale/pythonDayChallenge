# rock, paper, scissors
import random
user_choice = int(input("choose from below: \n1.Rock \n2.paper \n3.Scissors: \n"))
print(f"You have choose: {user_choice}")
computer_choice = random.randint(1,3)
print("computer choice")
print(computer_choice)
if user_choice ==  computer_choice:
    print("its draw")
elif computer_choice > user_choice:
    print("computer win")
elif user_choice > computer_choice:
    print("user win")        
elif user_choice == 0 and computer_choice == 2:
    print("user win") 
elif user_choice == 2 and computer_choice == 0:
    print ("computer win")    