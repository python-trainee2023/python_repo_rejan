# lambda fn example
lists = list(range(10))
filtered_list = list((filter(lambda item : item < 5, lists)))
print(filtered_list)



# mapped list
mapped_list = list(map(lambda item: item * 2, lists))
print(mapped_list)