#Clase para un nodo de árbol binario de búsqueda. 

class Nodo: 
    def __init__(self, dato):
        self.izquierda = None
        self.derecha = None
        self.dato = dato

def insertar(raiz, nodo):
    if raiz is None:
        raiz = nodo
    else:
        if raiz.dato < nodo.dato:
            if raiz.derecha is None: 
                raiz.derecha = nodo
            else:
                insertar(raiz.derecha, nodo)
        else:
            if raiz.izquierda is None:
                raiz.izquierda = nodo
            else:
                insertar(raiz.izquierda, nodo)

def inOrden(raiz):
    if raiz is not None: 
        inOrden(raiz.izquierda)
        print(raiz.dato)
        inOrden(raiz.derecha)

def preOrden(raiz):
    if raiz is not None:
        print(raiz.dato)
        preOrden(raiz.izquierda)
        preOrden(raiz.derecha)

def postOrden(raiz):
    if raiz is not None: 
        postOrden(raiz.izquierda)
        postOrden(raiz.derecha)
        print(raiz.dato)

def buscar_dato(raiz, dato):
    if raiz is None:
        return False;
    elif raiz.dato == dato:
        return True
    elif dato < raiz.dato:
        return buscar_dato(raiz.izquierda, dato)
    else:
        return buscar_dato(raiz.derecha, dato)


raiz = Nodo(['BORUSSIIGUADOS', 17529])
insertar(raiz, Nodo(['HOLA', 1450]))
insertar(raiz, Nodo(['EN', 1]))
insertar(raiz, Nodo(['DOS', 22570]))
insertar(raiz, Nodo(['MEXICO', 1580]))
insertar(raiz, Nodo(['ADIOS', 16758]))


import re

patron = re.compile('[0-9]+')

print("inOrden")
inOrden(raiz)
print()
print("preOrden")
preOrden(raiz)

print()
print("postOrden")
postOrden(raiz)

print()
print(buscar_dato(raiz, ['HOLA', patron]))

