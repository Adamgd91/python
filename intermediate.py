#### DICTS ####
europe = { 'spain': { 'capital':'madrid', 'population':46.77 },
           'france': { 'capital':'paris', 'population':66.03 },
           'germany': { 'capital':'berlin', 'population':80.62 },
           'norway': { 'capital':'oslo', 'population':5.084 } }


# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = {'capital' : 'rome' , 'population': 59.83}
print(type(data))
# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)
print(europe.keys())
print(europe.values())

######################################################################################
#### LISTS ####
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

front_display_list.insert(0,"Pineapple")
print(front_display_list)

my_list = [1, 2, 3, 4, 5]

print(len(my_list))
######################################################################################
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

beginning = suitcase[0:4]
print(beginning)
######################################################################################
votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

count_votes = votes.count("Jake")
print(count_votes)
######################################################################################
# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]
addresses.sort()
print(addresses)
######################################################################################
# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()
######################################################################################
# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort(reverse=True)
print(sorted_cities)
print(cities)
######################################################################################
games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]
games_sorted = sorted(games)

print(games)
print(games_sorted)

######################################################################################
ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
length = len(ingredients)
index = 0

while index < length:
  print(ingredients[index])
  index += 1
######################################################################################
items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]

print("Checking the sale list!")

for item in items_on_sale:
  print(item)
  if item == "knit dress":
    break

print("End of search!")
######################################################################################
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]

for age in ages:
  if age < 21:
    continue
  print(age)
  ######################################################################################
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0

for location in sales_data:
  print(location)
  for i in location:
    scoops_sold += i
print(scoops_sold)
######################################################################################
user_name = "Dave"  
match user_name:  
    case "Dave":  
        print("Get off my computer Dave!")  
    case "angela_catlady_87":  
        print("I know it is you, Dave! Go away!")   
    case "Codecademy":  
        print("Access Granted.")  
    case default:  
        print("Username not recognized.")  