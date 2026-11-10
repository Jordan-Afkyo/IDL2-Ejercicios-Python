"""
Ejercicio 9: Calcular el producto utilizando arrays: 100 x 98 x 96 x 94 x ... x 1 en este orden.
"""
import math

def main() -> None:
    arreglo: list[int] = [*range(100, 1, -2), 1]
    producto: int = math.prod(arreglo)

    secuencia_str: str = " x ".join(map(str, arreglo[:5])) + " x ... x " + " x ".join(map(str, arreglo[-2:]))
    print(f"Arreglo generado ({len(arreglo)} elementos): {secuencia_str}")
    print(f"\nProducto Total Exacto:\n{producto}")

if __name__ == "__main__":
    main()