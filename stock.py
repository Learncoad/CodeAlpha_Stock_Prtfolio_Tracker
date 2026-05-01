# stock_portfolio_tracker.py

import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 2700,
    "MSFT": 300,
    "AMZN": 3300
}

portfolio = {}


def add_stock():
    stock = input("Enter stock name (e.g., AAPL): ").upper()

    if stock not in stock_prices:
        print("Stock not available in price list!")
        return

    try:
        qty = int(input("Enter quantity: "))
    except ValueError:
        print("Invalid quantity!")
        return

    if stock in portfolio:
        portfolio[stock] += qty
    else:
        portfolio[stock] = qty

    print(f"{stock} added successfully.\n")


def calculate_total():
    total = 0
    print("\n----- Portfolio Summary -----")

    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        total += value
        print(f"{stock} -> Qty: {qty}, Price: {price}, Value: {value}")

    print(f"\nTotal Investment: {total}")
    return total


def save_to_txt(total):
    with open("portfolio.txt", "w") as f:
        f.write("Stock Portfolio Summary\n\n")

        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            f.write(f"{stock} -> Qty: {qty}, Value: {value}\n")

        f.write(f"\nTotal Investment: {total}")

    print("Saved to portfolio.txt")


def save_to_csv():
    with open("portfolio.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Value"])

        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            writer.writerow([stock, qty, price, value])

    print("Saved to portfolio.csv")


def menu():
    while True:
        print("\n1. Add Stock")
        print("2. View Portfolio")
        print("3. Save to File")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_stock()
        elif choice == "2":
            calculate_total()
        elif choice == "3":
            total = calculate_total()
            save_to_txt(total)
            save_to_csv()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    menu()