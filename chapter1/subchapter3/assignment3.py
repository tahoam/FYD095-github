clean_input = []
input_str = input('Enter a string. Will check if it is a palindrome. Only letters will be considered. ')

clean_input = [i for i in input_str if i.isalpha()]

# Compare list with reversed list.
if clean_input == clean_input[::-1]:
    print('It is a palindrome.')
else:
    print('It is not a palindrome.')