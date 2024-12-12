import random
from hangman_words import word_list
from hangman_art import stages,logo


lives=6

print(logo)

chosen_word=random.choice(word_list)
# print(chosen_word)

placeholder=""
word_length=len(chosen_word)

for positing in range(word_length):
    placeholder+="_ "
print(placeholder)

game_over = False
correct_letters=[]

while not game_over:

    print(f"****************************** {lives}/6 left ******************************")
    guess=input("Guess a letter ").lower()
    # print(guess)
    if guess in correct_letters:
        print(f"You've already guessed the letter {guess}")

    display=""

    for letter in chosen_word:
        if letter==guess:
            display+=letter
            correct_letters.append(letter)
        elif letter in correct_letters:
            display+=letter
        else:
            display+="_ "
    print(display)

    if guess not in chosen_word:
        lives-=1
        print(f"You've guessed {guess}, that's not in the word . You lose a life")
        if lives==0:
            game_over=True
            print(f"****************************** IT WAS {chosen_word}! **** YOU LOSE ******************************")

    if "_ " not in display:
        game_over=True
        print("****************************** YOU WIN ******************************")
    print(stages[lives])
