import random
while True:
    print("How many pencils would you like to use:")
    try:
        pencils = int(input())
    except ValueError:
        print("The number of pencils should be numeric")
        continue
    if pencils <= 0:
        print("The number of pencils should be positive")
        continue
    break
print("Who will be the first (John, Jack):")
first_player = input()
while first_player not in ["John", "Jack"]:
    print("Choose between 'John' and 'Jack'")
    first_player = input()
print("|" * pencils)
current_player = first_player
while pencils > 0:
    print(current_player + "'s turn!")
    if current_player == "Jack":
        if pencils == 1:
            taken = 1
        elif pencils % 4 == 0:
            taken = 3
        elif pencils % 4 == 3:
            taken = 2
        elif pencils % 4 == 2:
            taken = 1
        else:
            taken = random.randint(1, min(3, pencils))
        print(taken)
    else:
        while True:
            try:
                taken = int(input())
            except ValueError:
                print("Possible values: '1', '2' or '3'")
                continue
            if taken not in [1, 2, 3]:
                print("Possible values: '1', '2' or '3'")
                continue
            if taken > pencils:
                print("Too many pencils were taken")
                continue
            break
    pencils -= taken
    if pencils == 0:
        winner = "Jack" if current_player == "John" else "John"
        print(winner + " won!")
        break
    print("|" * pencils)
    if current_player == "John":
        current_player = "Jack"
    else:
        current_player = "John"
