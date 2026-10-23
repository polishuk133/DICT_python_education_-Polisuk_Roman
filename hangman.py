import random
words = ['python', 'java', 'javascript', 'php']
secret_word = random.choice(words)
guessed_letters = set()
def get_mask():
    return "".join(c if c in guessed_letters else "-" for c in secret_word)
print("HANGMAN")
print(get_mask())
for _ in range(8):
    letter = input("Input a letter: > ")
    if letter in secret_word:
        guessed_letters.add(letter)
    else:
        print("That letter doesn't appear in the word")
    print(get_mask())
print("Thanks for playing!")
print("We'll see how well you did in the next stage")