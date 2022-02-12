numbers = input('Input numbers separated by blankspace! ')

numbers_split = numbers.split()
numbers_list = [int(i) for i in numbers_split]

avg_val = sum(numbers_list)/len(numbers_list)
max_val = max(numbers_list)
min_val = min(numbers_list)

print(f'Högsta talet är {max_val}\nLägsta talet är {min_val}\nMedelvärdet är {avg_val}')