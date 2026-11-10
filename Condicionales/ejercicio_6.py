"""
Ejercicio 6: Leer la hora (HH MM SS) y mostrar por pantalla la hora N segundos después.
"""

def main() -> None:
    hh: int = int(input("Ingrese las horas (0-23): "))
    mm: int = int(input("Ingrese los minutos (0-59): "))
    ss: int = int(input("Ingrese los segundos (0-59): "))
    n_segundos: int = int(input("Ingrese los N segundos a sumar: "))

    total_segundos: int = (hh * 3600 + mm * 60 + ss + n_segundos) % 86400
    nueva_hh, resto = divmod(total_segundos, 3600)
    nueva_mm, nueva_ss = divmod(resto, 60)

    print(f"\nHora inicial  : {hh:02d}:{mm:02d}:{ss:02d}")
    print(f"Hora +{n_segundos} seg : {nueva_hh:02d}:{nueva_mm:02d}:{nueva_ss:02d}")

if __name__ == "__main__":
    main()