"""
Ejercicio 1: Calcular el total a pagar en una llantera.
El precio de cada llanta es S/150 si se compran menos de 5, y S/120 si se compran 5 o más.
"""

def main() -> None:
    cantidad: int = int(input("Ingrese la cantidad de llantas a comprar: "))
    precio_unitario: float = 150.0 if cantidad < 5 else 120.0
    total: float = cantidad * precio_unitario

    print(f"\nPrecio por llanta aplicado: S/ {precio_unitario:.2f}")
    print(f"Total a pagar por {cantidad} llantas: S/ {total:.2f}")

if __name__ == "__main__":
    main()