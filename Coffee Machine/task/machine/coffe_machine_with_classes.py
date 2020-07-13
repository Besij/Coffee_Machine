class Coffemachine:
    running = False

    money_inside = 550
    water_inside = 400
    milk_inside = 540
    beans_inside = 120
    cups_inside = 9

    e_water = 250
    e_beans = 16
    e_price = 4

    l_water = 350
    l_milk = 75
    l_beans = 20
    l_price = 7

    c_water = 200
    c_milk = 100
    c_beans = 12
    c_price = 6

    def __init__(self, money_inside, water_inside, milk_inside, beans_inside, cups_inside):
        self.money_inside = money_inside
        self.water_inside = water_inside
        self.milk_inside = milk_inside
        self.beans_inside = beans_inside
        self.cups_inside = cups_inside

        if not Coffemachine.running:
            self.start()

    def start(self):
        self.running = True
        print()
        action = input("Write action (buy, fill, take, remaining, exit)\n")
        if action == "buy":
            self.buy()
        elif action == "fill":
            self.fill()
        elif action == "take":
            self.take()
        elif action == "remaining":
            self.remaining()
        else:
            self.exit()

    def buy(self):
        print()
        choose = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")

        if choose == "1":
            if self.water_inside < self.e_water:
                print("Sorry, not enough water!")
                self.start()
            elif self.beans_inside < self.e_beans:
                print("Sorry, not enough coffee beans!")
                self.start()
            elif self.cups_inside < 1:
                print("Sorry, not enough disposable cups!")
                self.start()
            else:
                self.water_inside -= self.e_water
                self.beans_inside -= self.e_beans
                self.cups_inside -= 1
                self.money_inside += self.e_price
                print("I have enough resources, making you a coffee!")
                self.start()

        elif choose == "2":
            if self.water_inside < self.l_water:
                print("Sorry, not enough water!")
                self.start()
            elif self.beans_inside < self.l_beans:
                print("Sorry, not enough coffee beans!")
                self.start()
            elif self.cups_inside < 1:
                print("Sorry, not enough disposable cups!")
                self.start()
            elif self.milk_inside < self.l_milk:
                print("Sorry, not enough milk!")
                self.start()
            else:
                self.water_inside -= self.l_water
                self.beans_inside -= self.l_beans
                self.milk_inside -= self.l_milk
                self.cups_inside -= 1
                self.money_inside += self.l_price
                print("I have enough resources, making you a coffee!")
                self.start()

        elif choose == "3":

            if self.water_inside < self.c_water:
                print("Sorry, not enough water!")
                self.start()
            elif self.beans_inside < self.c_beans:
                print("Sorry, not enough coffee beans!")
                self.start()
            elif self.cups_inside < 1:
                print("Sorry, not enough disposable cups!")
                self.start()

            elif self.milk_inside < self.c_milk:
                print("Sorry, not enough milk!")
                self.start()
            else:
                self.water_inside -= self.c_water
                self.beans_inside -= self.c_beans
                self.milk_inside -= self.c_milk
                self.cups_inside -= 1
                self.money_inside += self.c_price
                print("I have enough resources, making you a coffee!")
                self.start()

        elif choose == "back":
            self.start()

    def fill(self):
        add_water = int(input("Write how many ml of water do you want to add:\n"))
        add_milk = int(input("Write how many ml of milk do you want to add:\n"))
        add_beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
        add_cups = int(input("Write how many disposable cups do you want to add:\n"))
        self.water_inside += add_water
        self.milk_inside += add_milk
        self.beans_inside += add_beans
        self.cups_inside += add_cups
        self.start()

    def take(self):
        print(f'I gave you ${self.money_inside}')
        self.money_inside = 0
        self.start()

    def remaining(self):
        print()
        print(f'The coffee machine has:')
        print(f'{self.water_inside} of water')
        print(f'{self.milk_inside} of milk')
        print(f'{self.beans_inside} of coffee beans')
        print(f'{self.cups_inside} of disposable cups')
        print(f'${self.money_inside} of money')
        self.start()

    def exit(self):
        self.running = False


machine1 = Coffemachine(550, 400, 540, 120, 9)
