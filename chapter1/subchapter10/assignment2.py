a = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# A dict with keys 0-9 and the value is the corresponding number written with letters.
print_dict = dict(zip(range(len(a)), a))

b = range(len(a))
ind = int(input('Enter index: '))
print(print_dict[ind])