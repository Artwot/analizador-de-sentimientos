"""def agruparElementos(lista):
    agrupados = []
    cont = 1
    print('Tamaño de la lista: ' +str(len(lista)))
    for i in range(len(lista)):
        print(i)
        if(i < len(lista) - 1):
            if(lista[i] == lista[i + 1]):
                cont += 1
            else:
                agrupados.append([lista[i], cont])
                cont = 1
        else:
            agrupados.append([lista[i], cont])
    print(agrupados)



#l = [7, 7, 32, 126, 128, 287, 287, 287, 287, 287, 287, 287, 287, 301, 301, 301, 301, 450]
l = [7]
agruparElementos(l)"""

import numpy as np

def prueba():
    for i in range(1, 2500):
        arr1 = np.arange()
    return arr1

prueba()
array = prueba()
print(array)

arr_prb = np.array(rdd_agrupados.collect())

np.savetxt('palabras', arr_prb, delimiter=',', header='string', comments='', fmt='%s')
