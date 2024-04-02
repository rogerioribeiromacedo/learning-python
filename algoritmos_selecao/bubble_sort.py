# -*- coding: utf-8 -*-
"""
Bubble sort.

@author: Rogerio
"""
import random


def bubble_sort(lista):
    """
    Bubble sort algorithm.

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
        for j in range(tam_lista - 1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]


def main():
    """
    Principal function.

    Returns
    -------
    None.

    """
    numeros = random.sample(range(1, 25), 10)
    print(f"Numeros desordenados: {numeros}")
    bubble_sort(numeros)
    print(f"Números ordenados...: {numeros}")


if __name__ == "__main__":
    main()
