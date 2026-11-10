"""
Ejercicio 7: Pida dos números, calcule el factorial de cada número con su desarrollo
e indique hasta qué múltiplo son iguales.
"""
import math

def formatear_factorial(n: int) -> str:
    cadena_factores: str = "x".join(str(i) for i in range(1, n + 1)) or "1"
    resultado: int = math.factorial(n)
    return f"{n}! > {cadena_factores} = {resultado:,}"

def main() -> None:
    num1: int = int(input("Ingrese el primer número entero positivo: "))
    num2: int = int(input("Ingrese el segundo número entero positivo: "))

    print(f"\n{formatear_factorial(num1)}")
    print(f"{formatear_factorial(num2)}")
    print(f">> Son iguales hasta el múltiplo {min(num1, num2)}")

if __name__ == "__main__":
    main()