def main():
    family = get_family()
    print(family)
    save_my_family(family)
def get_family():
    continue_bool = 'Y'
    family = []
    while continue_bool == 'Y':
        name = input('\nEnter Name: ')
        age = input('\nEnter Age ')
        person = {'name': name, 'age':age}
        family.append(person)
        user_input = input('Continue? (Y/n)')
        continue_bool = 'n' if user_input == 'n' else 'Y'
    return family
def save_my_family(family):
    file = open('family.txt', 'w')
    file.write('Here is a list of your family members.\n\n')
    for person in family:
        file.write(person['name'] + ' is ' + person['age'] + 'years.old\n')
