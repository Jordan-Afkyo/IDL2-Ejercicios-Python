"""
Ejercicio 4: Un vendedor recibe su sueldo base más 25% extra por comisión de sus
tres ventas en el mes. Calcular comisiones y el total a recibir.
"""

TASA_COMISION: float = 0.25

def main() -> None:
    sueldo_base: float = float(input("Ingrese el sueldo base del vendedor (S/): "))
    ventas: list[float] = [
        float(input(f"Ingrese el monto de la venta {i} (S/): "))
        for i in range(1, 4)
    ]

    total_ventas: float = sum(ventas)
    comision: float = total_ventas * TASA_COMISION
    sueldo_total: float = sueldo_base + comision

    print(f"\nTotal de ventas realizadas : S/ {total_ventas:,.2f}")
    print(f"Comisión por ventas (25%)  : S/ {comision:,.2f}")
    print(f"Sueldo total a recibir     : S/ {sueldo_total:,.2f}")

if __name__ == "__main__":
    main()