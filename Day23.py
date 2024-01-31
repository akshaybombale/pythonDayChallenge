import random
HARD_LEVEL = 5
EASY_LEVEL = 10

def set_level(choosen_level):
    if choosen_level=="Hard":
        return HARD_LEVEL 
    else:
        return EASY_LEVEL

def check_answer(guess_number, system_no, your_attempt):
    if  guess_number < system_no:
        print("your Guess is too low")
        return your_attempt -1 
    
    elif guess_number > system_no:
        print("your Guess is too High")
        return your_attempt -1
    
    else:
        print(f"your Guess is correct... the Answer is {system_no} ")



def game():

    system_no = random.randint(1,50)
    print (system_no)
    difficulty_level = input("choose difficulty level from Hard and Easy: ")
    # if difficulty_level !="Hard" or difficulty_level !="Easy":
    #     print("you have Enter Wrong choice ... please Enter Right Difficulty Level") 
    your_attempt=set_level(difficulty_level)
    guess_number = 0

    while guess_number != system_no:

        print(f"you have {your_attempt} remaining to guess the number ")
        guess_number = int(input("please guess your number: "))

        your_attempt= check_answer(guess_number, system_no, your_attempt) 
        if your_attempt == 0:
            print("you are out of guesses.... you lose !")
            return
        elif guess_number != system_no:
            print("Guess Again..")    

game()