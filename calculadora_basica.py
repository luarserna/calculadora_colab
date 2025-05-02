def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    if b == 0:
        raise ValueError("No se puede dividir entre cero.")
    return a / b

def main():
    while True:
        print("\nCalculadora Básica")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")

        opcion = input("Selecciona una opción (1-5): ")

        if opcion == "5":
            print("Saliendo de la calculadora.")
            break

        try:
            a = float(input("Ingrese el primer número: "))
            b = float(input("Ingrese el segundo número: "))

            if opcion == "1":
                print("Resultado de la suma:", suma(a, b))
            elif opcion == "2":
                print("Resultado de la resta:", resta(a, b))
            elif opcion == "3":
                print("Resultado de la multiplicación:", multiplicacion(a, b))
            elif opcion == "4":
                try:
                    resultado = division(a, b)
                    print("Resultado de la división:", resultado)
                except ValueError as e:
                    print("Error:", e)
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese números válidos.")

if __name__ == "__main__":
    main()in()