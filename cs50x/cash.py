def get_coins(value, cents):
    coins = 0
    while cents >= value:
        cents -= value
        coins += 1
    return coins

coins = 0
cents = int(input("Enter amount of cents due: "))
while cents < 0:
            cents = int(input("Enter a positive number: "))

quarters = get_coins(25, cents)
cents -= (quarters * 25)

dimes = get_coins(10, cents)
cents -= (dimes * 10)

nickels = get_coins(5, cents)
cents -= (nickels * 5)

pennies = get_coins(1, cents)

total = quarters + dimes + nickels + pennies

print(f"You owe {total} coins.")
