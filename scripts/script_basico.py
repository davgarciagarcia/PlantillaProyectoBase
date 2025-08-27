"""Uso:
    python scripts/script_basico.py --nombre "Ana" --repeticiones 2
"""
import argparse

def saludar(nombre: str, n: int = 1) -> None:
    for _ in range(n):
        print(f"Hola, {nombre}. Bienvenida a VS Code + Python.")

def parse_args():
    parser = argparse.ArgumentParser(description="Ejemplo de script con argumentos")
    parser.add_argument("--nombre", type=str, required=True, help="Nombre a saludar")
    parser.add_argument("--repeticiones", type=int, default=1, help="Número de repeticiones")
    return parser.parse_args()

if __name__ == "__main__":
    args = parse_args()
    saludar(args.nombre, args.repeticiones)
