"""
Ejercicio 5: Determinar cuánto ahorrará una persona en un año si al final de cada mes
deposita cantidades variables de dinero. Mostrar el acumulado mes a mes y el ahorro final.
"""

MESES: tuple[str, ...] = (
    "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
)

def gestionar_ahorro_anual() -> None:
    ahorro_acumulado: float = 0.0

    for mes in MESES:
        deposito: float = float(input(f"Depósito de {mes:<10} (S/): "))
        ahorro_acumulado += deposito
        print(f"  -> Ahorro acumulado hasta {mes}: S/ {ahorro_acumulado:,.2f}")

    print(f"\n Ahorro total al finalizar los 12 meses: S/ {ahorro_acumulado:,.2f}")

if __name__ == "__main__":
    gestionar_ahorro_anual()