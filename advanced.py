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
            