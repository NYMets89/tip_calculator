## Customer enters total cost of the meal
## Input will be converted to a float
cost_of_food = float(input('Enter total cost of meal: '))

## User cannot enter a negative cost for the meal
while cost_of_food < 0.0:
    cost_of_food = float(input('Please enter a positive number for cost of meal: '))

## Customer enters number of people splitting the final bill
number_of_people = float(input('Enter number of people splitting the bill: '))

## User cannot enter fractional number of people
while number_of_people != int(number_of_people):
    number_of_people = float(input('Enter a whole number for amount of people splitting the bill: '))

## Customer enters what percent they want to tip
## Input will be converted to a float
percentage_of_tip = float(input('Enter what percent you want to tip: ')) / 100

## Set sales tax at fixed percent as a float
sales_tax = 1.10

## Calculate the total bill from customer including the tip
## Value will be rounded to 2 decimal places
total_bill = round((cost_of_food * sales_tax) + (percentage_of_tip * cost_of_food), 2)

## Amount each person owes including tip
## Value rounded to 2 decimal places
total_per_person = round(total_bill / number_of_people, 2)

print(f'The total bill including tip is {total_bill} and each person owes {total_per_person}')