import math
Items_Number = float (input("Enter Quantity of Items"))
Box_Capacity = float (input("Enter Capacity Items per Box"))
Quantity_Boxes = math.ceil(Items_Number / Box_Capacity)
print ("For" ,Items_Number,"Items, and",Box_Capacity, "Boxes, are necessary", Quantity_Boxes, "Boxes." )
