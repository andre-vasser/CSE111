from datetime import datetime
from multiprocessing.managers import BaseManager
from tkinter.tix import INTEGER


gender = int (input("Please enter your gender (M or F):"))
age = datetime (input("Enter your birthdate (YYYY-MM-DD):"))
weight = float(input("Enter your weight in U.S. pounds:"))
height = float(input("Enter your height in U.S. inches:"))
bmr = weight + height - age 
bmi = weight / height
print = bmr
print = bmr
