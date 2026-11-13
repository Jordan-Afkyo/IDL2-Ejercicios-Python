"""
Ejercicio 9: Calcular el total a pagar por la compra de N camisas:
- De 1 a 4 camisas: 12.5% de descuento.
- De 5 a 8 camisas: 20% de descuento.
- Más de 8 camisas: 31.5% de descuento.
"""

def main() -> None:
    # --- 1. INICIO ---
    
    # --- 2. DECLARACIÓN E INICIALIZACIÓN DE VARIABLES ---
    cantidad: int = 0               # Cantidad de camisas (Entero)
    precio_unitario: float = 0.0    # Precio por cada camisa (Real)
    tasa_dscto: float = 0.0         # Porcentaje de descuento aplicable (Real)
    compra_sin_dscto: float = 0.0   # Subtotal bruto de la compra (Real)
    monto_dscto: float = 0.0        # Dinero descontado (Real)
    compra_con_dscto: float = 0.0   # Total neto a pagar (Real)

    # --- 3. CUERPO DEL ALGORITMO ---
    cantidad = int(input("Ingrese la cantidad de camisas compradas: "))
    precio_unitario = float(input("Ingrese el precio unitario de la camisa (S/): "))

    match cantidad:
        case n if 1 <= n <= 4:
            tasa_dscto = 0.125
        case n if 5 <= n <= 8:
            tasa_dscto = 0.20
        case n if n > 8:
            tasa_dscto = 0.315
        case _:
            tasa_dscto = 0.0

    compra_sin_dscto = cantidad * precio_unitario
    monto_dscto = compra_sin_dscto * tasa_dscto
    compra_con_dscto = compra_sin_dscto - monto_dscto

    print(f"\nCompra final sin descuento : S/ {compra_sin_dscto:.2f}")
    print(f"Monto del descuento ({tasa_dscto*100:.1f}%): S/ {monto_dscto:.2f}")
    print(f"Compra final con descuento : S/ {compra_con_dscto:.2f}")
    
    # --- 4. FIN ---

if __name__ == "__main__":
    main()
