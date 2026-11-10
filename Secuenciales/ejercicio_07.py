"""
Ejercicio 7: Determinar el cobro de un estacionamiento.
El pago por hora es de S/ 5.00 y el pago por los minutos restantes es de S/ 0.10 por minuto.
(También se muestra el cálculo tomando la fracción de hora como hora completa).
"""

TARIFA_HORA: float = 5.00
TARIFA_MINUTO: float = 0.10

def main() -> None:
    horas: int = int(input("Ingrese las horas completas de estacionamiento: "))
    minutos: int = int(input("Ingrese los minutos restantes (0-59): "))

    # Cálculo exacto con tarifa por hora (S/5.00) + minutos restantes (S/0.10)
    cobro_detallado: float = (horas * TARIFA_HORA) + (minutos * TARIFA_MINUTO)

    # Cálculo redondeando fracción de hora a hora completa
    horas_completas: int = horas + (1 if minutos > 0 else 0)
    cobro_hora_completa: float = horas_completas * TARIFA_HORA

    print(f"\nCobro (S/5.00/h + S/0.10/min restante) : S/ {cobro_detallado:.2f}")
    print(f"Cobro (Fracción tomada como h completa): S/ {cobro_hora_completa:.2f}")

if __name__ == "__main__":
    main()