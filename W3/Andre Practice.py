import math
end_odometer = float (input("Enter the first odometer reading (miles):"))
start_odometer = float (input("Enter the second odometer reading (miles):"))
gallons = float(input("Enter the amount of fuel used (gallons):"))
miles_per_gallon = (end_odometer - start_odometer)/gallons
kilometer_per_liter = (235.215/miles_per_gallon)
print ("The car consume " ,miles_per_gallon, "miles per mile")
print ("The car consume" ,kilometer_per_liter, "Km per liter")
print ("Congratulations Andre Vasser!!!! You wrote a correct alone program by yourself")