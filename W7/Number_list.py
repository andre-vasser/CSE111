import random
import random


def main ():
    numbers = [16.2, 75.1, 52.3]
    print(numbers) 
    append_random_numbers (numbers)
    append_random_numbers (numbers,3)
     


def append_random_numbers(num_list,quantity=1):
    for x in range (quantity):
        num_list.append(random.uniform(0,100))
    
    
    print(num_list)
    #print(quantity)

#     print(numbers)
#     append_random_numbers (y,z)
# print(numbers)
main()
