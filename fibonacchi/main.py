import fibonacchi_digitos
import fibonacchi_secuencia
from os import system
system("cls")
operacion = input("""1-mostrar solo un digito un digito
2-mostrar toda la secuencia \n""")
match operacion:
    case "1":
        system("cls")
        digito = input("Ingrese el numero de digito a buscar \n")
        digito = int(digito)
        print(fibonacchi_digitos.fibonacci_d(digito))
    case "2":
        digitos = input("Ingrese la cantidad de digitos deseada \n")
        digitos = int(digitos)
        system("cls")
        fibonacchi_secuencia.fibonacci_s(digitos)
