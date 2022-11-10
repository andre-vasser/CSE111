#print(int(input(abs(float(5)))))
#str(int(float((input(print("Enter a number: "))))))
#print(type(len(list(round(math.sqrt(abs(float(str(int(input("Enter and Integer: ")))))), 1)))))
#print("Hello, I", 20, sep=" am " end = "How old are you?", flush=true")
#print("hello", "world", sep="\n")
#import math
#import cmath
#x = (math.ceil((17**9)/3)) -6

#import math
#def random_math():
#    return (math.ceil(math.pow(17, 9)/3) -6) % 2 == 0
#print(random_math())

#import random
#random_number_list = []
#while len (random_number_list) < 100:
#    random_number_list.append(random.randint(0, 1000))
#random_number_list.sort(reverse=True)
#print(random_number_list)

from datetime import datetime
# initialize the odd numbers
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
       21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
       41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
# get current minute
current_minute = datetime.today().minute
# check the odd minute
if current_minute in odds:
    print("Odd minute.")
else:
    print("Even minute.")