# x = 5

# if x <= 2:
#   print("This is printed")
# if x <= 4:
#   print("This is also printed")
# if x <= 6:
#   print("Is this printed?")
# if x <= 8:
#   print("This might be printed.")
  
# import random

# name = "Adam"
# question = input("Ask a question! ")
# answer = ""
# random_number = random.randint(1, 9)
# #print(random_number)

# if random_number == 1:
#   answer = "Yes - definitely"
# elif random_number == 2:
#   answer = "It is decidedly so"
# elif random_number == 3:
#   answer = "Without a doubt"
# elif random_number == 4:
#   answer = "Reply hazy, try again"
# elif random_number == 5:
#   answer = "Ask again later"
# elif random_number == 6:
#   answer = "Better not tell you now"
# elif random_number == 7:
#   answer = "My sources say no"
# elif random_number == 8:
#   answer = "Outlook not so good"
# elif random_number == 9:
#   answer = "Very doubtful"
# else:
#   answer = "Error"

# print(f'{name} asks: {question}?')
# print(f'8-Ball answer: {answer}')

def shipping():
    types = input("You want ground or drone? ").strip().lower()
    
    if types not in ['ground', 'drone']:
        print("Invalid shipping type.")
        return
    
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