# 1: loan eligibility checker
# ask the user for monthly income
# current debt amount
# check if:
# income > 100,000 and debt = 0
# store result in is_eligible
# monthly_income = float(input("what is your monthly income: "))
# debtAmt = float(input("what is your debt amount: "))
# if monthly_income >= 100000.00 and debtAmt == 0:
#     is_eligible = True
# else:
#     is_eligible = False
# print(is_eligible)


# Exercise 2: online shopping total
# step 1: ask the user for item, price, quantity
# step 2: calculate total cost
# step 3: check if total cost is greater than 50000 or quantity is greater than 5
# if true, give a discount of 10%
# else, no discount
# calculate grand total

# item = input("Enter your item")
# price = float(input("Enter the price"))
# qty = int(input("Enter the quantity"))
# total = price * qty
# if total >= 50000 or qty > 5:
#     total -= total * (10/100)
# print("Total:",total)

# Gym Membership Access
# Ask the user for age:
# Ask for membership payment status (True or False)
# Check if : age is greater than or equal to 18 and membership
# is active
# Print Access Granted or Access denied at the end of the program

age = int(input("Enter your age:"))
status = input("what is your membership status (Paid/Outstanding):")
if status == "Paid":
    status = True
else:
    status = False
if age >= 18 and status:
    print("Access Granted")
else:
    print("Access denied")

# BANK WITHDRAWAL SYSTEM
# Ask the user for acct bal, withdrawal amt,
# check if withdrawal amt is less or equal to balance..."print withdrawal success
# else insufficient funds

balance = float(input("Account balance is: "))
withAmt = float(input("how much do you want to withdraw: "))
if withAmt <= balance:
    print("withdrawal sufficient")
else:
    print("insufficient funds")

# STUDENT RESULT ANALYSIS
# Ask the user for maths score, Eng score
# check if:
# at least one score is above 80..print("pass")
# else print ("fail")

math = int(input("what is your maths score: "))
eng = int(input("what is your eng score: "))
if math and eng > 50:
    if math or eng > 80:
        print("pass")
    else:
        print("fail")


# SALARY INCREMENT SYSTEM
# Ask the user for current salary
# ask for their bonus amt
# increase salary using +=

salary = float(input("How much is your total salary:"))
bonus = float(input("How much is your bonus amount:"))
print("salary += bonus")

# FUEL CONSUMPTION TRACKER
# Ask the user for fuel in tank:
# Ask for fuel used
# check if remaining fuel is less than 10 litres
# print ("low on fuel")

fuel = int(input("How many litres of fuel in tank: "))
fuelUsed = int(input("How mant litres of fuel used: "))
if fuelUsed < 10
    print("low on fuel")


# LAPTOP PURCHASE TRACKER CHECKER
# Ask the user for laptop price,
# Ask the customer budget:
# Ask the discount availability (True or False)
# check if budget is enough or discount is available

LapPrice = float(input("How much is laptop: "))
CusBudget = float(input("what is the customer budget: "))
DisAva =



