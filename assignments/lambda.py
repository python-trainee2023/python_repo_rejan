from functools import reduce

user_input = input("Enter the start & end for a range with delimiter ','");
start,end = list(user_input.split(','))

num_list = list(range(int(start), int(end)))
print(num_list)

even_sum = reduce(lambda x, y: x + y, list(filter(lambda item: item % 2 == 0, num_list)))
odd_sum = reduce(lambda x, y: x + y, list(filter(lambda item: item % 2 != 0, num_list)))

print(f"Odd even sum in the range {start},{end}: {even_sum + odd_sum}")


