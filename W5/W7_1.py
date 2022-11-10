student1 = {
    "age":20,
    "name":"Fred",
    "phone_number":"555-5555"
}
student2 = {
    "age":30,
    "name":"Jenny",
    "phone_number":"777-7777"
}
print("The name of the student is" + student2 ['name'])

student_list = [
    student1, student2
]
#print(student_list)

#print(len(student_list))
#i = 0
#while (i < len(student_list)):
#    print(student_list[i])
#    i += 1
total_age = 0
for student in student_list:
    total_age += student['age']

average_age = total_age / len(student_list)
#print(average_age)

student_names=["Jed","Jen","Sandy"]
#for student_name in student_names:
#    print(student_name)

#print(student_names)
#print(student_names[0], student_names[1],student_names[2])

