input_str = input('Enter a string. The number of letters and digits will be counted. ')
letters = 0
digits = 0
for i in input_str:
    if i.isdigit():
        digits += 1
    elif i.isalpha():
        letters += 1
    else:
        pass
print(f'The amount of letters are {letters} and the amount of digits are {digits}.')