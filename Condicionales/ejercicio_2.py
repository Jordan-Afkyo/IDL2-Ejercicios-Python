"""
Ejercicio 2: Determinar cuál de los 3 números brindados por el usuario
es el menor y el mayor de todos ellos.
"""

def main() -> None:
    numeros: list[float] = [
        float(input(f"Ingrese el número {i}: "))
        for i in range(1, 4)
    ]

    menor: float = min(numeros)
    mayor: float = max(numeros)

    print(f"\nDe los números ingresados {numeros}:")
    print(f"- El número MENOR es: {menor}")
    print(f"- El número MAYOR es: {mayor}")

if __name__ == "__main__":
    main()