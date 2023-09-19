import string as letras

abc = list(letras.ascii_uppercase)
abc_reemplazo = ['4','I3','[',')','3','|=',
                 '&','#','1',',_|','>|','1',
                 '/\\/\\','^/','Ø','|*','(_,)',
                 'I2','5','7','(_)','\/','\/\/',
                 '><','Ч','-|_']

palabra = input(str('Ingrese la palabra: '))
palabra = palabra.upper()


reemplazo_abc = {abc[i]: abc_reemplazo[i] for i in range(len(abc))}
palabra_reemplazada = ' '.join([reemplazo_abc.get(letra, letra) for letra in palabra])

print(palabra_reemplazada)