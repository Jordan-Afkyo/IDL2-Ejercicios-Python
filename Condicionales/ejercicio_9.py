"""
Ejercicio 9: Calcular el total a pagar por la compra de N camisas:
- De 1 a 4 camisas: 12.5% de descuento.
- De 5 a 8 camisas: 20% de descuento.
- Más de 8 camisas: 31.5% de descuento.
Imprimir compra sin descuento, monto del descuento y compra con descuento.
"""

def obtener_tasa_descuento(cantidad: int) -> float:
    match cantidad:
        case n if 1 <= n <= 4:
            return 0.125
        case n if 5 <= n <= 8:
            return 0.20
        case n if n > 8:
            return 0.315
        case _:
            return 0.0

def main() -> None:
    cantidad: int = int(input("Ingrese la cantidad de camisas compradas: "))
    precio_unitario: float = float(input("Ingrese el precio unitario de la camisa (S/): "))

    compra_sin_dscto: float = cantidad * precio_unitario
    tasa: float = obtener_tasa_descuento(cantidad)
    monto_dscto: float = compra_sin_dscto * tasa
    compra_con_dscto: float = compra_sin_dscto - monto_dscto

    print(f"\nCompra final sin descuento : S/ {compra_sin_dscto:.2f}")
    print(f"Monto del descuento ({tasa*100:.1f}%): S/ {monto_dscto:.2f}")
    print(f"Compra final con descuento : S/ {compra_con_dscto:.2f}")

if __name__ == "__main__":
    main()