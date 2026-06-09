stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 300
}

total_investment = 0

print("===== Stock Portfolio Tracker =====")

while True:
    stock_name = input("Enter Stock Name : ").upper()

    if stock_name == "DONE":
        break

    if stock_name in stocks:
        quantity = int(input("Enter Quantity: "))
        investment = stocks[stock_name] * quantity
        total_investment += investment

        print("Investment Added:", investment)
    else:
        print("Stock not available in database.")

print("\n===== Portfolio Summary =====")
print("Total Investment Value =", total_investment)

file = open("portfolio.txt", "w")
file.write("Total Investment Value = " + str(total_investment))
file.close()

print("Result saved in portfolio.txt")