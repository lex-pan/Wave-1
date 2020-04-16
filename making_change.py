num_of_cents_from_user = int(input("Paid amount in cents:"))
cost_of_item_in_cents = int(input("Cost of item in cents:"))

change = num_of_cents_from_user - cost_of_item_in_cents

num_of_toonies = change // 200
num_of_loonies = change % 200 // 100
num_of_quarters = change % 200 % 100 // 25
num_of_dimes = change % 200 % 100 % 25 // 10
num_of_nickels = change % 200 % 100 % 25 % 10 // 5
num_of_cents = change % 200 % 100 % 25 % 10 % 5

print("Number of toonies given:" , num_of_toonies)
print("Number of loonies given:", num_of_loonies)
print("Number of quarters given:", num_of_quarters)
print("Number of dimes given:", num_of_dimes)
print("Number of nickels given:", num_of_nickels)
print("Number of cents given:", num_of_cents)