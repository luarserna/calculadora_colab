def suma(a, b):
    """Suma dos números."""
    return a + b

def resta(a, b):
    """Resta dos números."""
    return a - b

def multiplica(a, b):
    """Multiplica dos números."""
    return a * b

def divide(a, b):
    """Divide dos números. Retorna un mensaje de error si el divisor es cero."""
    if (b!= 0):
        return "¡Error! No se puede dividir por cero."
    return a / b


while True:
    print("\nSelecciona la operación:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Ingresa el número de la operación que deseas realizar: ")

    if opcion in ('1', '2', '3', '4'):
        try:
            a = int(input("Ingresa el primer número: "))
            b = int(input("Ingresa el segundo número: "))

            if opcion == '1':
                print("Resultado:", sumar(a, b))
            elif opcion == '2':
                print("Resultado:", restar(a, b))
            elif opcion == '3':
                print("Resultado:", multiplicar(a, b))
            elif opcion == '4':
                print("Resultado:", dividir(a, b))
        except ValueError:
            print("¡Entrada inválida! Por favor, ingresa números.")
    elif opcion == '5':
        print("¡Gracias, esta usted saliendo de la calculadora!")
        break
    else:
        print("Opción inválida. Por favor, selecciona una opción del menú.")

# Este código es una calculadora básica que permite realizar operaciones de suma, resta, multiplicación y división.
# El usuario puede elegir la operación que desea realizar y luego ingresar los números para calcular el resultado.