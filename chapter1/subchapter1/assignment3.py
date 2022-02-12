print('Create table. Type "stop" to end inputs.')
age = []
name = []
adress = []

while True:
    name.append(input('Enter name: '))
    age.append(input('Enter age: '))
    adress.append(input('Enter adress: '))
    if name[-1] == 'stop' or age[-1] == 'stop' or adress[-1] == 'stop':
        break

if 'stop' in name:
    name.remove('stop')
if 'stop' in age:
    age.remove('stop')
if 'stop' in adress:
    adress.remove('stop')

for i, j, k  in zip(name, age, adress):
    print(f'{i:<15} {j:>10} {k:>10}')