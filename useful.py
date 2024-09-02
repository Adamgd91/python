def double(x): 

    return x * 2 

numbers = [1, 2, 3, 4, 5] 

doubled_numbers = map(double, numbers) 

print(list(doubled_numbers))  # Output: [2, 4, 6, 8, 10] 
############################################
# Converting strings to integers 

str_nums = ['1', '2', '3', '4', '5'] 

int_nums = list(map(int, str_nums)) 

print(int_nums)  # Output: [1, 2, 3, 4, 5]
############################################
# Finding the length of strings 

words = ['apple', 'banana', 'cherry'] 

word_lengths = list(map(len, words)) 

print(word_lengths)  # Output: [5, 6, 6] 