# List


# convert str to list
string_to_list = list("supertest")
print(string_to_list)


# list concat
list_1  = ["list", "one"]
list_2  = ["list", "two"]
concat_list  = list_1 + list_2
print(concat_list)


list_cpy = concat_list.copy()
print(f"Copy List: {list_cpy}")



# iteration
for item in list_cpy:
    print(item)


# a[start: stop: step]
new_list = list(range(10))

# Slicing
print("******************* List *****************")
print(new_list)
print(new_list[1:5])
print(new_list[2:])
print(new_list[:3])
print(new_list[::2])
print(new_list[::-1])


new_list_cpy = new_list[:]
print("******************* LIST COPY ***************")
print(new_list_cpy)
new_list_cpy[0:3] = ["apple", "banana", "mangoes"]
print(new_list_cpy)


# tuple
# roles = ("user", "admin", "superadmin ")
# print(roles)
# print(len(roles))
# ADMIN_ROLE = 'admin'
# print(f"{ADMIN_ROLE} count: {roles.count(ADMIN_ROLE)}")


# Unpack tuple
roles = ("user", "admin", "superadmin ")
# USER_ROLE, ADMIN_ROLE, SUPER_ADMIN_ROLE = roles
# print(USER_ROLE)
#

USER_ROLE, *OTHER_ROLE =  roles
print(OTHER_ROLE)
OTHER_ROLE[0] = "TEST ROLE"
print(OTHER_ROLE)


# A dictionary is a collection which is unordered, changeable and indexed.
# A dictionary consists of a collection of key-value pairs

person = {"name": "username", "email": "username@test.com", "address": "user address"}
hobbies = {"hobbies": ["coding", "coding", "coding"]}

person.update(hobbies)