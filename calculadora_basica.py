def suma(a,b):
    return a + b

def multiplicacion(a,b):
    return a * b

def division(a,b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero no permitida."
    
def resta(a,b):
    return a - b

def main():
    while True:
        print("\nCalculadora Básica")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "5":
            print("Saliendo de la calculadora...")
            break

        if opcion in ["1", "2", "3", "4"]:
            try:
                a = float(input("Ingresa el primer número: "))
                b = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Error: Por favor, ingresa valores numéricos válidos.")
                continue

            if opcion == "1":
                print("Resultado de la suma: ", suma(a, b))
            elif opcion == "2":
                print("Resultado de la resta: ", resta(a, b))
            elif opcion == "3":
                print("Resultado de la multiplicación: ", multiplicacion(a, b))
            elif opcion == "4":
                print("Resultado de la división: ", division(a, b))
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

main()