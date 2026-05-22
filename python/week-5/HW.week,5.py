price = 50
amount_due = price

while amount_due > 0:

    print("Amount Due:", amount_due)

    coin_input = input("Insert Coin: ")

    try:
        coin = int(coin_input)

    except ValueError:
        print("Please insert a valid integer coin")
        continue

    if coin not in [5, 10, 25]:
        print(f"Coin not accepted. Returning {coin} cents")
        continue

    amount_due -= coin

change_owed = abs(amount_due)

print("Change Owed:", change_owed)