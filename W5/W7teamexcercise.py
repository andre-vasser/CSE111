

empty_list = []
def main():
    new_fruit = input('What fruit do you want add to the list? ')
    add_list(new_fruit)
    print(add_list(empty_list))
    # for item in range(len(empty_list)):
    #     print(empty_list[item])
    #     add_list(empty_list)
    #     remove_list(empty_list)
    #     insert_list(empty_list)
        
def add_list(new_fruit):
    
    empty_list.append(new_fruit)

# def remove_list(empty_list):
#     empty_list.pop[2]
    

# def insert_list(empty_list):
#     other_fruit = input("What other fruit would you like to add to the list? ")
#     empty_list.insert(0, other_fruit)


# if __name__ == "__main__":
#     main()
    

print ()