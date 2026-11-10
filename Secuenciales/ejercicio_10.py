"""
Ejercicio 10: Desglose de cajero automático en denominaciones de:
200, 100, 50, 20, 10, 5, 1 entregando la menor cantidad de billetes/monedas.
"""

DENOMINACIONES: tuple[int, ...] = (200, 100, 50, 20, 10, 5, 1)

def main() -> None:
    monto: int = int(input("Ingrese la cantidad entera a retirar (S/): "))
    restante: int = monto

    print(f"\nDesglose óptimo para S/ {monto}:")
    for billete in DENOMINACIONES:
        cantidad, restante = divmod(restante, billete)
        if cantidad > 0:
            tipo: str = "Billetes" if billete >= 10 else "Monedas"
            print(f"- {cantidad} {tipo} de S/ {billete}")

if __name__ == "__main__":
    main()