import sys

print('Vending Machine:')
print('1. Water : $1.00')
print('2. Cola : $1.50')
print('3. Gatorade: $2.00')

price = 0
choice = int(input ('Please choose your drink:'))

if choice == 1:
    price = 1.00
elif choice == 2:
    price = 1.50
elif choice == 3:
    price = 2.00
else:
    sys.exit("Please try again!")

quarters = int(input("How many quarters do you have?"))
dimes = int(input("How many dimes do you have?"))
nickels = int(input("How many nickels do you have?"))
pennies = int(input("How many pennies do you have?"))

total = (quarters*.25)+(dimes*.10)+(nickels*.05)+(pennies*.01)

if total >= price:
    print("Your change is $" + "%.2f"% (total - price) + ". Have a nice day.")
else:
    sys.exit("Please try again.")

