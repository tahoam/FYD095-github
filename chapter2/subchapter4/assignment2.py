import numpy as np
import math

while True:
    a = input('\'Spela Sten, sax, påse\'! För att spela skriv in \'sten\', \'sax\' eller \'påse\'. Skriv \'stop\' för att avbryta. ' )
    if a == 'stop':
        print('Spelet avbryts.')
        break

    sign = math.ceil(np.random.rand()*3)
    
    if sign == 1: # sten
        if a == 'sten':
            print('Sten! Ingen vann. Spela igen!')
        elif a == 'sax':
            print('Sten! Du förlorade!')
            break
        elif a == 'påse':
            print('Sten! Du vann!')
            break
    elif sign == 2: # sax
        if a == 'sten':
            print('Sax! Du vann!')
            break
        elif a == 'sax':
            print('Sax! Ingen vann. Spela igen!')
        elif a == 'påse':
            print('Sax! Du förlorade!')
            break
    elif sign == 3: # påse
        if a == 'sten':
            print('Påse! Du förlorade!')
            break
        elif a == 'sax':
            print('Påse! Du vann!')
            break
        elif a == 'påse':
            print('Påse! ingen vann. Spela igen!')