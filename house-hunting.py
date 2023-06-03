# # Part A

# portion_down_payment = 0.25 # Down payment portion
# current_savings = 0 # Money saved so far
# r = 0.04 # Annual return rate
# number_of_months = 0 # Number of months it will take to save to down payment

# annual_salary = float(input("Enter your annual salary: "))
# portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
# total_cost = float(input("Enter the cost of your dream home: "))

# # Calculate the down payment for the house
# down_payment = total_cost * portion_down_payment


# while current_savings < down_payment:
#     # Calculate the savings for each month
#     monthly_savings = annual_salary / 12 * portion_saved
#     # Calculate the monthly returns from investment
#     monthly_return = current_savings * r / 12
#     # Increment the savings for each month
#     current_savings = current_savings + monthly_savings + monthly_return
#     number_of_months += 1

# print("Number of months:", number_of_months)

# Part B

# portion_down_payment = 0.25  # Down payment portion
# current_savings = 0  # Money saved so far
# r = 0.04  # Annual return rate
# number_of_months = 0  # Number of months it will take to save to down payment

# annual_salary = float(input("Enter your annual salary: "))
# portion_saved = float(
#     input("Enter the percent of your salary to save, as a decimal: "))
# total_cost = float(input("Enter the cost of your dream home: "))
# semi_annual_raise = float(input("Enter the semi annual raise, as a decimal: "))

# # Calculate the down payment for the house
# down_payment = total_cost * portion_down_payment


# while current_savings < down_payment:
#     # Calculate the savings for each month
#     monthly_savings = annual_salary / 12 * portion_saved
#     # Calculate the monthly returns from investment
#     monthly_return = current_savings * r / 12
#     # Increment the savings for each month
#     current_savings = current_savings + monthly_savings + monthly_return
#     number_of_months += 1

#     # Calculate the semi annual raise
#     if number_of_months % 6 == 0:
#         # annual_salary = annual_salary + (annual_salary * semi_annual_raise)
#         annual_salary += (annual_salary * semi_annual_raise)

# print("Number of months:", number_of_months)

# Part C


# portion_down_payment = 0.25  # Down payment portion

# number_of_months = 36  # Number of months it will take to save to down payment

# annual_salary = float(input("Enter the starting salary: "))

# # The down payment for the house
# down_payment = total_cost * portion_down_payment

# # Money saved so far
# current_savings = 0

# while abs(current_savings - down_payment) > 100:
#     low_portion_saved = 0  # Lowest portion saved rate
#     high_portion_saved = 625  # Highest portion saved rate
#     middle_ground = (high_portion_saved + low_portion_saved) / 2

#     portion_saved = middle_ground / 100  # Best savings rate

#     for n in range(number_of_months + 1):
#         # Skip the first month if 0
#         if n == 0:
#             continue

#         # Calculate the savings for each month
#         monthly_savings = annual_salary / 12 * portion_saved
#         # Calculate the monthly returns from investment
#         monthly_return = current_savings * r / 12
#         # Increment the savings for each month
#         current_savings += monthly_savings + monthly_return

#         # Calculate the semi annual raise
#         if n % 6 == 0:
#             annual_salary += (annual_salary * semi_annual_raise)

#     if abs(current_savings - down_payment) > 100:
#         high_portion_saved = middle_ground
#     else:
#         low_portion_saved = middle_ground

# print("Portion saved: ", portion_saved)
# print("Current savings:", current_savings)
# print("Difference: ", current_savings - down_payment)


# Part C

num_of_months = 36
semi_annual_raise = .07
annual_return_rate = 0.04
total_cost = 1000000
down_payment = total_cost * 0.25

starting_salary = int(input("Enter the starting salary: "))

high = 10000
low = 0
guess = (high + low) / 2
num_of_searches = 0
current_savings = 0

while abs(down_payment - current_savings) >= 100:
    current_savings = 0
    portion_saved = guess / 100
    annual_salary = starting_salary

    # Calculate the current savings after 36 months
    for n in range(1, num_of_months + 1):
        # Calculate the monthly savings
        monthly_savings = annual_salary / 12 * portion_saved
        # Calculate return from our monthly investment
        investment_returns = current_savings * (annual_return_rate / 12)
        # Calculate the current savings
        current_savings += monthly_savings + investment_returns

        # Calculate the semi annual raise
        if n % 6 == 0:
            annual_salary += annual_salary * semi_annual_raise

    if current_savings > down_payment:
        high = guess
    else:
        low = guess

    guess = (high + low) / 2
    num_of_searches += 1

if portion_saved > 1:
    print("It is not possible to pay the down payment in three years.")
else:
    print("Best savings rate:", portion_saved)
    print("Steps in bisection search:", num_of_searches)
