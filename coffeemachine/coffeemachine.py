class CoffeeMachine:
    COFFEES = {
        "1": {"water": 250, "milk": 0, "beans": 16, "price": 4},
        "2": {"water": 350, "milk": 75, "beans": 20, "price": 7},
        "3": {"water": 200, "milk": 100, "beans": 12, "price": 6},
    }
    PROMPTS = {
        "choosing_action": "Write action (buy, fill, take, remaining, exit): ",
        "choosing_coffee": (
            "What do you want to buy? 1 - espresso, 2 - latte, "
            "3 - cappuccino, back – to main menu: "
        ),
        "filling_water": "Write how many ml of water do you want to add: ",
        "filling_milk": "Write how many ml of milk do you want to add: ",
        "filling_beans": "Write how many grams of coffee beans do you want to add: ",
        "filling_cups": "Write how many disposable cups of coffee do you want to add: ",
    }
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.state = "choosing_action"
    def ask(self):
        """Виводить запрошення відповідно до поточного стану."""
        if self.state not in ("filling_milk", "filling_beans", "filling_cups"):
            print()
        print(self.PROMPTS[self.state], end="")
    def process(self, user_input):
        """Єдина точка входу: обробляє рядок залежно від поточного стану."""
        if self.state == "choosing_action":
            self.process_action(user_input)
        elif self.state == "choosing_coffee":
            self.process_coffee(user_input)
        elif self.state == "filling_water":
            self.water += int(user_input)
            self.state = "filling_milk"
        elif self.state == "filling_milk":
            self.milk += int(user_input)
            self.state = "filling_beans"
        elif self.state == "filling_beans":
            self.beans += int(user_input)
            self.state = "filling_cups"
        elif self.state == "filling_cups":
            self.cups += int(user_input)
            self.state = "choosing_action"
    def process_action(self, action):
        if action == "buy":
            self.state = "choosing_coffee"
        elif action == "fill":
            self.state = "filling_water"
        elif action == "take":
            self.take()
        elif action == "remaining":
            self.print_state()
        elif action == "exit":
            self.state = "exit"
        else:
            print("Unknown action!")
    def process_coffee(self, choice):
        self.state = "choosing_action"
        if choice == "back":
            return
        if choice not in self.COFFEES:
            print("Unknown option!")
            return
        coffee = self.COFFEES[choice]
        missing = self.check_resources(coffee)
        if missing is None:
            print("I have enough resources, making you a coffee!")
            self.make_coffee(coffee)
        else:
            print(f"Sorry, not enough {missing}!")
    def check_resources(self, coffee):
        """Повертає назву інгредієнта, якого не вистачає, або None."""
        if self.water < coffee["water"]:
            return "water"
        if self.milk < coffee["milk"]:
            return "milk"
        if self.beans < coffee["beans"]:
            return "coffee beans"
        if self.cups < 1:
            return "disposable cups"
        return None
    def make_coffee(self, coffee):
        self.water -= coffee["water"]
        self.milk -= coffee["milk"]
        self.beans -= coffee["beans"]
        self.cups -= 1
        self.money += coffee["price"]
    def take(self):
        print()
        print(f"I gave you {self.money}")
        self.money = 0
    def print_state(self):
        print()
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.beans} of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"{self.money} of money")
def main():
    machine = CoffeeMachine()
    while machine.state != "exit":
        machine.ask()
        machine.process(input())
if __name__ == "__main__":
    main()