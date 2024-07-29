
import random

words = ['alegbra', 'python', 'terraform', 'hunger', 'phone', 'pizza']

# Chooses a word from the list at random
chosen_word = random.choice(words)
word_display = ['_' for _ in chosen_word] #makes a list of underscores
print(word_display)
attempts = 10

print('Welcome to Hangman!')

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                word_display[index] = guess #reveals the letter
    else:
        print("That letter doesn't appear in the word. Try Again!")
        attempts -= 1

# Game Ending
if '_' not in word_display:
    print("You guess the word!")
    print('_'.join(word_display))
    print("You completed the challenge!")
else:
    print("You ran out of attempts. The word was : " + chosen_word)
    print("You lost... Whomp Whomp")