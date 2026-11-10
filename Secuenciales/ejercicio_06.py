"""
Ejercicio 6: Ingrese la edad de una persona para determinar aproximadamente
cuántos meses, semanas, días y horas ha vivido.
"""

def main() -> None:
    edad_anios: int = int(input("Ingrese la edad de la persona en años: "))

    meses: int = edad_anios * 12
    semanas: int = edad_anios * 52
    dias: int = edad_anios * 365
    horas: int = dias * 24

    print(f"\nUna persona de {edad_anios} años ha vivido aproximadamente:")
    print(f"- Meses   : {meses:,}")
    print(f"- Semanas : {semanas:,}")
    print(f"- Días    : {dias:,}")
    print(f"- Horas   : {horas:,}")

if __name__ == "__main__":
    main()