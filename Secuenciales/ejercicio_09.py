"""
Ejercicio 9: Cuánto pagaría un cliente por una compra con descuento y cuánto sería
el cambio que recibiría en un pago en efectivo.
"""

def main() -> None:
    monto_base: float = float(input("Ingrese el monto base de la compra (S/): "))
    porcentaje_dscto: float = float(input("Ingrese el porcentaje de descuento (%): "))
    efectivo_entregado: float = float(input("Ingrese con cuánto dinero paga el cliente (S/): "))

    descuento: float = monto_base * (porcentaje_dscto / 100)
    total_pagar: float = monto_base - descuento
    vuelto: float = efectivo_entregado - total_pagar

    print(f"\nDescuento aplicado : S/ {descuento:.2f}")
    print(f"Total a pagar      : S/ {total_pagar:.2f}")
    print(f"Cambio / Vuelto    : S/ {vuelto:.2f}")

if __name__ == "__main__":
    main()