#### DATA TYPES ####
age = 33
fname = "Adam"
lname = "Davidson"
canDrink = True
lists = ["Sarah", 31, "Davidson", 33]
sets = {"Stranger Things", "LOTR", "Matrix"}
dicts = {
    "golfer": "Tiger Woods",
    "majors": 15
}
kidages = [11,20,11,23,10,14,15,16,25,24,23]
abletodrink = []
cantdrink =[]
#### VARIABLES ####

fullname = f'{fname} {lname}'
print(fullname)


print(f'{fullname}s age is {age}')

if age > 21:
    print("You can drink!")
else:
    print("You can't drink yet!")
    
print(dicts)

#### FOR LOOPS ####

for i in lists:
    print(i)

for i in kidages:
    if i > 21:
        abletodrink.append(i)
    else:
        cantdrink.append(i)

print(abletodrink)
print(cantdrink)