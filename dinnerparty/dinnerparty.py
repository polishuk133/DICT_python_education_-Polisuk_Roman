import random
def main():
    print("Enter the number of friends joining (including you):")
    try:
        count = int(input("> "))
    except ValueError:
        print("\nNo one is joining for the party")
        return
    if count <= 0:
        print("\nNo one is joining for the party")
        return
    print("\nEnter the name of every friend (including you), each on a new line:")
    friends = {}
    for _ in range(count):
        name = input("> ")
        friends[name] = 0
    print("\nEnter the total amount:")
    total = float(input("> "))
    share = round(total / count, 2)
    for name in friends:
        friends[name] = share
    print('\nDo you want to use the "Who is lucky?" feature? Write Yes/No:')
    answer = input("> ")
    print()
    if answer == "Yes":
        lucky = random.choice(list(friends))
        print(f"{lucky} is the lucky one!")
        print()
        # Суму ділять на n - 1, щасливчик не платить
        share = round(total / (count - 1), 2) if count > 1 else 0
        for name in friends:
            friends[name] = share
        friends[lucky] = 0
    else:
        print("No one is going to be lucky")
        print()
    print(friends)
if __name__ == "__main__":
    main()