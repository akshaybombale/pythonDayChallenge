import random
word = ["Akshada", "Akshay","pranalee"]
lives = 6
chosen_word = random.choice(word).lower() #AKshay
display = []
for i in range(len(chosen_word)):
    display+= '_'
print(display)
game_over = False
while not game_over:
    guessed_letter = input("Guess the letters: ").lower()
    for pos in range(len(chosen_word)):
        letter = chosen_word[pos]
        if letter == guessed_letter:
            display[pos]  = guessed_letter
    print(display)        
        #     print("match")
        # else:
        #     print("not match")
    if  guessed_letter not in chosen_word:
        lives-=1
        if lives == 0:
            game_over = True
            print("you lost...")
    if '_' not in display:
        game_over = True
        print("you won...")       

            
          
