pencils = int(input("How many pencils would you like to use:\n"))
print("Who will be the first (John, Jack):")
first_player = input()
while first_player not in ["John", "Jack"]:
    print("Choose between 'John' and 'Jack'")
    first_player = input()
print("|" * pencils)
current_player = first_player
while pencils > 0:
    print(current_player + "'s turn:")
    taken = int(input())
    pencils -= taken
    print("|" * pencils)
    if pencils == 0:
        break
    if current_player == "John":
        current_player = "Jack"
    else:
        current_player = "John"
