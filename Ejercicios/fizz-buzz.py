import numpy as np

numeros = np.array(range(1,101))

for numero in numeros:
    if numero %3 == 0 and numero %5 == 0:
        print(f'{numero} fizz-buzz')
    elif numero %3 == 0:
        print(f'{numero} fizz')
    elif numero %5 == 0:
        print(f'{numero} buzz')