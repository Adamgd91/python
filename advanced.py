#### FUNCTIONS ####
def even_nums(num):
    evens = []
    for i in num:
        if i % 2 == 0:
            evens.append(i)
    return evens

print(even_nums([10,2,4,5,3,8]))
            