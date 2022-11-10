from cmath import sqrt
import math
def getInput(type):
    if type == "w":
        return input("Enter the width of the tire in mm: ")
    elif type == "a":
        return input("Emter the aspect of Ratio: ")
    elif type == "d":
        return input("Enter diameter of the tire: ")
if __name__ == '__main__':
    w=int(getInput("w"))
    a=int(getInput("a"))
    d=int(getInput("d"))

    part1 = (w*a) + (2540*d)
    part2 = (math.pi * ((w**2)*a))
    part3 = (round(part1*part2/10000000000,2))

print (part3)