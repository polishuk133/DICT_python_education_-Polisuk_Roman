pencils = int(input("How many pencils would you like to use:\n"))
print("Who will be the first (John, Jack):")
first_player = input()
while first_player not in ["John", "Jack"]:
    print("Choose between 'John' and 'Jack'")
    first_player = input()
print("|" * pencils)
print(first_player + " is going first!")
