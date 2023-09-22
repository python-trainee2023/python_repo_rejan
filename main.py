# student = ['ram', 'hari', 'shyam']
# student_tuple = tuple(student)
# student_list = list(student_tuple)
# print(student_tuple)
# print(student_list)
#
# student_dict={
#     "name": "rejan",
#     "age": 22,
#     "hobbies": ["coding", "coding", "coding"]
# }
#
# keys_list = list(student_dict.keys())
# values_list = list(student_dict.values())
# print(keys_list)
# print(values_list)
#
#
# print(student_dict.items())



# print(student_dict)

#
# user_input = input("what's your good name?")
# print("hi ", user_input)

# import sys
#
# if(len(sys.argv) < 2):
#     print('usage: python <script> <user_input>')
# else:
#     print(sys.argv[1])
#
#
# print(sys.argv)

#
# holiday = 'false'
#
# if not bool(holiday):
#     pass
# else:
#     print('holiday')
#
#
# def pallindrome(str):
#     return str
#
# res = pallindrome('hello world')

# def reverse(string):
#     string = string[::-1]
#     return string
#
#
# user_input = input('user string ?')
# reversed = reverse(user_input)
#
# if(user_input == reversed):
#     print('pallindrome string !')
# else:
#     print('not pallindrome stirng!')


# for i in range(5):
#     if(i == 3):
#         print('found')
#         break
#         print('not found!')
# else:
#     pass
#
#
#
# def checkPrime(num):
#     input = int(num)
#     counter = 0
#     for i in range(2,input):
#         if (input % i == 0):
#             counter += 1
#     if counter == 0:
#         return True
#
#     return False
#


# user_input = input('user input ?')
# res = checkPrime(user_input)
# if(res):
#     print('Prime number')
# else:
#     print('Composite number')


# list = [1,2,3,4,5,6,7,8,9]
# new_list = []
# for i in list:
#     if(i%2==0):
#         new_list.append(i)
#
# print(new_list)
#
# updated_list = [num for num in list if num % 2 == 0]
# print(updated_list)
#
#
# new_list = [x for x in range(10)]
# print(new_list)
#
#
# fruits_list = ['apple', 'banana', 'mangoes', 'grapes', 'cherries']
# fruits_update = [item if item != 'apple' else 'test' for item in fruits_list]
# print(fruits_update)

# list = [1,2,3,4,5,6,7,8,9]
# num_update = [x if x%2 == 0 else '' for x in list]
# print(num_update)

# values = [1,2.5, 6, 2.21, 2.45, 3.5, 8]
#
# int_list  = [x for x in values if isinstance(x, int)]
# print(int_list)
#
#
# def checkEven(n):
#     if(n % 2 == 0):
#         return n

# using lambda
# list_num = range(10)
# list_even = list(filter(lambda x: x % 2 == 0, list_num))
# print(list_even)


# user_input = input('Enter 3 numbers')
# input_list = list(user_input.split(','))
#
# num_list = [int(x) for x in input_list]
#
# num_list.sort()
#
#
# print(num_list[len(num_list)-1])

#
# user_input = input('Enter user inputs with delimiter ","')
# input_list = list(user_input.split(','))
#
# num_list = [item for item in input_list if isinstance(item, int) or isinstance(item,float)]
# string_list = [item for item in input_list if isinstance(item,str)]
# print(num_list)
# print(string_list)

# num_list = []
# string_list = []
# for item in input_list:
#     if(isinstance(item, int) or isinstance(item, float)):
#         num_list.append(item)
#     elif(isinstance(item, str)):
#         string_list.append(item)
#     else:
#         continue
#
# print(num_list)
# print(string_list)

user_input = input('Enter user inputs with delimiter ","')
input_list = list(user_input.split(','))

num_list = [item for item in input_list if item.isnumeric()]
string_list = [item for item in input_list if not item.isnumeric()]
print(num_list)
print(string_list)











