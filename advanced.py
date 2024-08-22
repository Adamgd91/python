#### FUNCTIONS ####
def even_nums(num):
    evens = []
    for i in num:
        if i % 2 == 0:
            evens.append(i)
    return evens

print(even_nums([10,2,4,5,3,8]))

#####################################################################
def shipping():
    types = input("You want ground or drone? ").strip().lower()
    
    if types not in ['ground', 'drone']:
        print("Invalid shipping type. Choose ground or drone!")
        return shipping()
    
    weight = float(input("How much does your package weigh? "))
    
    if types == 'ground':
        flat_charge = 20
        if weight <= 2:
            total = weight * 1.50 + flat_charge
        elif weight <= 6:
            total = weight * 3.00 + flat_charge
        elif weight <= 10:
            total = weight * 4.00 + flat_charge
        else:
            total = weight * 4.75 + flat_charge
        print(f'You are charged based on weight. Total: ${total:.2f}')

    if types == 'drone':
        drone_flat_charge = 0
        if weight <= 2:
            total = weight * 4.50 + drone_flat_charge
        elif weight <= 6:
            total = weight * 9.00 + drone_flat_charge
        elif weight <= 10:
            total = weight * 12.00 + drone_flat_charge
        else:
            total = weight * 14.25 + drone_flat_charge
        print(f'You are charged based on weight. Total: ${total:.2f}')
shipping()              
#####################################################################
def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = car_rental_rate * trip_time
  hotel_total = hotel_rate * trip_time - 10
  trip_total = car_rental_total + hotel_total + plane_ticket_price

  return trip_total

print(calculate_expenses(200, 100, 100, 5))
#######################################################################
current_budget = 3500.75

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

# Write your code below: 
def deduct_expense(budget, expense):
  return budget - expense

shirt_expense = 9

new_budget_after_shirt = deduct_expense( current_budget, shirt_expense )

print_remaining_budget(new_budget_after_shirt)