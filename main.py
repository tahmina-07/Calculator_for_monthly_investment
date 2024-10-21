# !/usr/bin/env python3

import locale  # Model for currency exchange
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')  # Set the currency formating to US Doller

print("Future Investment Calculator")
print()

choice = 'y' # Use this variable to control the loop

while choice.lower() == 'y':
    # Get input from user
    monthly_investment = float(input("Enter monthly investment:\t"))
    interest_rate = float(input("Enter yearly interest rate:\t"))
    years = int(input("Enter the numbers of years: "))

    # Change yearly values to monthly values
    interest_rate = interest_rate/12/100
    months = years*12

    # Calculating the future value of investment
    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest_amount = future_value*interest_rate
        future_value += monthly_interest_amount
    print("Future Value: \t" + locale.currency(future_value, grouping=True))
    print()

    choice = input("Do you want to continue? (y/n) ")
    print()
print("Thank you! Bye!")



