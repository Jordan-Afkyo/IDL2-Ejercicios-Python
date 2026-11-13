"""
Ejercicio 4: Un vendedor recibe su sueldo base más 25% extra por comisión de sus
tres ventas en el mes. Calcular comisiones y el total a recibir.
"""

def main() -> None:
    # --- 1. INICIO ---
    
    # --- 2. DECLARACIÓN E INICIALIZACIÓN DE VARIABLES ---
    TASA_COMISION: float = 0.25  # Constante real (25%)
    sueldo_base: float = 0.0     # Almacena el sueldo fijo mensual
    venta_1: float = 0.0         # Almacena el monto de la primera venta
    venta_2: float = 0.0         # Almacena el monto de la segunda venta
    venta_3: float = 0.0         # Almacena el monto de la tercera venta
    total_ventas: float = 0.0    # Acumula la suma de las 3 ventas
    comision: float = 0.0        # Almacena la ganancia por comisión
    sueldo_total: float = 0.0    # Almacena el pago final del mes

    # --- 3. CUERPO DEL ALGORITMO (Entrada, Proceso y Salida) ---
    sueldo_base = float(input("Ingrese el sueldo base del vendedor (S/): "))
    venta_1 = float(input("Ingrese el monto de la venta 1 (S/): "))
    venta_2 = float(input("Ingrese el monto de la venta 2 (S/): "))
    venta_3 = float(input("Ingrese el monto de la venta 3 (S/): "))
    
    total_ventas = venta_1 + venta_2 + venta_3
    comision = total_ventas * TASA_COMISION
    sueldo_total = sueldo_base + comision

    print(f"\nTotal de ventas realizadas : S/ {total_ventas:,.2f}")
    print(f"Comisión por ventas (25%)  : S/ {comision:,.2f}")
    print(f"Sueldo total a recibir     : S/ {sueldo_total:,.2f}")
    
    # --- 4. FIN ---

if __name__ == "__main__":
    main()
