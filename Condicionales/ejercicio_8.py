"""
Ejercicio 8: Solicite al usuario 3 números enteros (validar que sean diferentes)
y mostrarlos ordenados de manera ascendente o descendente según indique el usuario.
"""

def main() -> None:
    while True:
        n1: int = int(input("Ingrese el primer número entero: "))
        n2: int = int(input("Ingrese el segundo número entero: "))
        n3: int = int(input("Ingrese el tercer número entero: "))

        if len({n1, n2, n3}) == 3:
            break
        print(" Error: Los 3 números deben ser diferentes. Intente de nuevo.\n")

    orden: str = input("¿En qué orden desea verlos? (A = Ascendente / D = Descendente): ").strip().upper()
    descendente: bool = (orden == "D")

    ordenados: list[int] = sorted([n1, n2, n3], reverse=descendente)
    tipo_orden: str = "Descendente" if descendente else "Ascendente"
    print(f"\nNúmeros en orden {tipo_orden}: {ordenados}")

if __name__ == "__main__":
    main()