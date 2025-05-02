def suma(a,b):
    return a + b

def resta(a,b):
    return a - b


def multiplicacion(a , b):
    return a * b


def division(a,b):
    return a/b

def main():
    print("Calculadora Basica")
    print("1. Sumar")
    print("2. Restar")
    print("3. multiplicacon")
    print("4. division")
    print("5. Salir")

    # solicitar al usuario que ingrese la opcion
    opcion = input("ingresa una opcion (1/2/3/4/5):")
    a = float(input("Ingresa el primer numero: "))
    b = float(input("Ingresa el segundo numero: ")) 
    # realizar las operaciones que estan relacionadas
    if opcion == "1":
        print(f"La suma de el numero {a}, {b} es {suma(a, b)}")
    elif opcion == "2":
        print(f"La resta de el numero {a}, {b} es {resta(a, b)}")
    elif opcion == "3":
         print(f"La multiplicacion de el numero {a} por el numero {b} es {multiplicacion(a, b)}")
    elif opcion == "4":
         print(f"La Division de el numero {a} dividido {b} es {division(a, b)}")
    elif opcion == "5":
        print("Saliendo de la calculadora...")
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.")

main()