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

exit = False

while not exit:

    print()
    action = input("Write action (buy, fill, take, remaining, exit)\n")

    if action == "buy":
        print()
        choose = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")

        if choose == "1":
            if water_inside < e_water:
                print("Sorry, not enough water!")
            elif beans_inside < e_beans:
                print("Sorry, not enough coffee beans!")
            elif cups_inside < 1:
                print("Sorry, not enough disposable cups!")
            else:
                water_inside -= e_water
                beans_inside -= e_beans
                cups_inside -= 1
                money_inside += e_price
                print("I have enough resources, making you a coffee!")

        elif choose == "2":
            if water_inside < l_water:
                print("Sorry, not enough water!")
            elif beans_inside < l_beans:
                print("Sorry, not enough coffee beans!")
            elif cups_inside < 1:
                print("Sorry, not enough disposable cups!")
            elif milk_inside < l_milk:
                print("Sorry, not enough milk!")
            else:
                water_inside -= l_water
                beans_inside -= l_beans
                milk_inside -= l_milk
                cups_inside -= 1
                money_inside += l_price
                print("I have enough resources, making you a coffee!")

        elif choose == "3":

            if water_inside < c_water:
                print("Sorry, not enough water!")

            elif beans_inside < c_beans:
                print("Sorry, not enough coffee beans!")

            elif cups_inside < 1:
                print("Sorry, not enough disposable cups!")

            elif milk_inside < c_milk:
                print("Sorry, not enough milk!")
            else:
                water_inside -= c_water
                beans_inside -= c_beans
                milk_inside -= c_milk
                cups_inside -= 1
                money_inside += c_price
                print("I have enough resources, making you a coffee!")

        elif choose == "back":
            print()
            continue

    elif action == "fill":
        print()
        add_water = int(input("Write how many ml of water do you want to add:\n"))
        add_milk = int(input("Write how many ml of milk do you want to add:\n"))
        add_beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
        add_cups = int(input("Write how many disposable cups do you want to add:\n"))

        water_inside += add_water
        milk_inside += add_milk
        beans_inside += add_beans
        cups_inside += add_cups

    elif action == "take":
        print(f'I gave you ${money_inside}')
        money_inside = 0

    elif action == "remaining":
        print()
        print(f'The coffee machine has:')
        print(f'{water_inside} of water')
        print(f'{milk_inside} of milk')
        print(f'{beans_inside} of coffee beans')
        print(f'{cups_inside} of disposable cups')
        print(f'${money_inside} of money')

    elif action == "exit":
        exit = True

