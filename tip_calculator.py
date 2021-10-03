## Customer enters total cost of the meal
## Input will be converted to a float
cost_of_food = float(input('Enter total cost of meal: '))
## Customer enters number of people splitting the final bill
## Input will be converted to a float
number_of_people = float(input('Enter number of people splitting the bill: '))
## Customer enters what percent they want to tip
## Input will be converted to a float
percentage_of_tip = float(input('Enter what percent you want to tip: '))
## Convert customer tip percent into a percentage by dividing by 100
tip_percent = percentage_of_tip / 100
## Set variable at fixed percent as a float
sales_tax = 1.10

##Calculate the total bill from customer including the tip
total_bill = (cost_of_food * sales_tax) + (tip_percent * cost_of_food)
## Amount each person owes including tip
total_per_person = total_bill / number_of_people

print(f'The total bill including tip is {total_bill} and each person owes {total_per_person}')