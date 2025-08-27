"""Funciones de distancia para problemas en rejilla y grafos simples."""
from math import sqrt
from typing import Tuple

Punto = Tuple[int, int]

def manhattan(a: Punto, b: Punto) -> int:
    """Distancia Manhattan para estados en rejilla."""
    return abs(a[0]-b[0]) + abs(a[1]-b[1])

def euclidea(a: Punto, b: Punto) -> float:
    """Distancia Euclídea estándar."""
    return sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

if __name__ == "__main__":
    print("manhattan((0,0),(3,4)) =", manhattan((0,0),(3,4)))
    print("euclidea((0,0),(3,4))  =", euclidea((0,0),(3,4)))
