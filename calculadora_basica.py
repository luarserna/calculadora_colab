def suma(a,b):
    return a + b

def resta(a,b):
    return a - b

def multiplicacion(a,b):
    return a * b

def division(a, b): 
    if b != 0:
        return a / b
    else:
        return "No se puede dividir entre cero"

def main():
    opcion = '1'
    while ((opcion== '1') or (opcion== '2') or (opcion== '3') or (opcion== '4')):
        print("Calculadora Básica")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")	
        if opcion == "1":
            a = int(input("Ingresa el primer número: "))
            b = int(input("Ingresa el segundo número: "))
            print("Resultado:", suma(a, b))
        elif opcion == "2":
            a = int(input("Ingresa el primer número: "))
            b = int(input("Ingresa el segundo número: "))
            print("Resultado:", resta(a, b))
        elif opcion == "3":
            a = int(input("Ingresa el primer número: "))
            b = int(input("Ingresa el segundo número: "))
            print("Resultado:", multiplicacion(a, b))
        elif opcion == "4":
            a = int(input("Ingresa el primer número: "))
            b = int(input("Ingresa el segundo número: "))
            print("Resultado:", division(a, b))
        elif opcion == "5":
            print("Saliendo de la calculadora...")
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.")

main()