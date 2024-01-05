import random
import words
lives = 6
chosen_word = random.choice(words.word).lower() #AKshay
print(chosen_word)
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
    
    if  guessed_letter not in chosen_word:
        lives-=1
        if lives == 0:
            game_over = True
            print("you lost...")
    if '_' not in display:
        game_over = True
        print("you won...")       

            
          
