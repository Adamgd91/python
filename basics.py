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
#### VARIABLES ####

fullname = f'{fname} {lname}'
print(fullname)


print(f'{fullname}s age is {age}')

if age > 21:
    print("You can drink!")
else:
    print("You can't drink yet!")
    

print(dicts)