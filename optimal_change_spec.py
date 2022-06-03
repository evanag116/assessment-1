from optimal_change import optimal_change


print("1:", optimal_change(62.13, 100) == "The optimal change for an item that costs $62.13 with an amount paid of $100 is 1 $20 bill, 1 $10 bill, 1 $5 bill, 2 $1 bills, 3 quarters, 1 dime, and 2 pennies.")
print("2:", optimal_change(31.51, 50) == "The optimal change for an item that costs $31.51 with an amount paid of $50 is 1 $10 bill, 1 $5 bill, 3 $1 bills, 1 quarter, 2 dimes, and 4 pennies.")
print("3:", optimal_change(50, 31.51) == "Error: please provide sufficient payment.")
print("4:", optimal_change(49.91, 192) == "The optimal change for an item that costs $49.91 with an amount paid of $192 is 1 $100 bill, 2 $20 bills, 2 $1 bills, 1 nickel, and 4 pennies.")
print("5:", optimal_change(10.72, 10.72) == "For an item that costs $10.72 with an amount paid of $10.72, there is no change required.")
print("6:", optimal_change(9.99, 10) == "The optimal change for an item that costs $9.99 with an amount paid of $10 is 1 penny.")
