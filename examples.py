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

python_topics = ["variables", "control flow", "loops", "modules", "classes"]

length = len(python_topics)
index = 0

while index < length:
  print(f'I am learning about {python_topics[index]}')
  index += 1
