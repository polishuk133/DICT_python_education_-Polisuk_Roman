import random
words = ['python', 'java', 'javascript', 'php']
secret_word = random.choice(words)
hint = secret_word[:3] + "-" * (len(secret_word) - 3)
print("HANGMAN")
answer = input(f"Guess the word {hint}: > ")
if answer == secret_word:
    print("You survived!")
else:
    print("You lost!")
