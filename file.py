# file handling

# emp_file = open("files/employees.txt", "r")
# print(emp_file.read())
# print(emp_file.readline())


# file pointers
# print(emp_file.read(5))
# print(emp_file.read(2))


# list
# content = emp_file.readlines()
# print(content)

# print names
# for names in emp_file.readlines():
#     print(names)
#
# emp_file.close()


# append file
emp_file = open("files/employees.txt", "a+")
emp_file.write('\n Supertest Test Department')

emp_list = emp_file.readlines()
print(emp_list)
emp_file.close()