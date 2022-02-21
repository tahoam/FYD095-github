from multiprocessing import Condition


clean_input = []
input_str = input('Enter a string. Will check if it is a palindrome. Only letters will be considered. ')

clean_input = [i for i in input_str if i.isalpha()]

# Compare list with reversed list.
cond = True
for i in range(len(clean_input)//2):
    if clean_input[i].lower() != clean_input[-i-1].lower():
        cond = False
        break

if cond:
    print('It is a palindrome.')
else:
    print('It is not a palindrome.')