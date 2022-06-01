coke_price = 50
total = 0
while True:
    money = int(input("Enter the coin please"))
    if not ((money == 5) or (money == 10) or (money == 25)):
        print(f"Amount due: {coke_price}")
        break
    else:
        total = total + money
        if (total >= coke_price):
            print(f"Change owed: {total-coke_price}")
            break
        else:
            print(f"Amount due: {coke_price-total}")

