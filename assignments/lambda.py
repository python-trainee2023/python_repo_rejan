from functools import reduce

user_input = input("Enter the start & end for a range with delimiter ','");
start,end = list(user_input.split(','))

num_list = list(range(int(start), int(end) + 1))
print(num_list)

even_sum = reduce(lambda x, y: x + y, list(filter(lambda item: item % 2 == 0, num_list)))
odd_sum = reduce(lambda x, y: x + y, list(filter(lambda item: item % 2 != 0, num_list)))

print(f"Even sum in a range: {even_sum}")
print(f"Odd sum in a range: {odd_sum}")
print(f"Total sum in a range {start},{end}: {even_sum + odd_sum}")


