# -*- coding: utf-8 -*-
"""
Selection sort.

@author: Rogerio
"""
import random


def selection_sort(lista):
    """
    Sort selection algorithm.

    Parameters
    ----------
    lista : list
        Number list.

    Returns
    -------
    None.

    """
    tam_lista = len(lista)
    for i in range(tam_lista - 1):
        # Indice do menor número
        menor_idx = i
        for j in range(i, tam_lista):
            if lista[j] < lista[menor_idx]:
                menor_idx = j
        if lista[i] > lista[menor_idx]:
            aux = lista[i]
            lista[i] = lista[menor_idx]
            lista[menor_idx] = aux


def main():
    """
    Principal function.

    Returns
    -------
    None.

    """
    numeros = random.sample(range(1, 25), 10)
    print(f"Numeros desordenados: {numeros}")
    selection_sort(numeros)
    print(f"Números ordenados...: {numeros}")


if __name__ == "__main__":
    main()
