quantity = input ("How many members of your family do you want to add? ")
#name = input ("Whats the name: ")
#age = input ("Whats the age: ")

def getinput():
    list=[]
    for i in range (0,int(quantity)):
        name = input("Whats the name? ")
        age = input("Whats Age? ")
    list.append ([name,age])
    return list
    
def main ():
    getinput()

main()
print(list)
    






