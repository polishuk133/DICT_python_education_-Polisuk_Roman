import random
words = ['python', 'java', 'javascript', 'php']
secret_word = random.choice(words)
print("HANGMAN")
answer = input("Guess the word: > ")
if answer == secret_word:
    print("You survived!")
else:
    print("You lost!")

