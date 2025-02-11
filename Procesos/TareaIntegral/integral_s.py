import math
import sys


def integral(a, b, n):
    if n > 0 and a <= b:
        dx = (b-a)/n
        x = a
        integral = 0
        for i in range(1, n+1):
            valorFx = x*x
            integral = integral + valorFx *dx
            x += dx
        print(f"La integral bajo la curva es: {integral}")
    else:
        print("Error, los limites del intervalo o el numero de particiones es incorrecto")

def main():
    if len(sys.argv) != 4:
        print("Error, numero de argumentos incorrecto")
        return
    
    a = float(sys.argv[1])
    b = float(sys.argv[2])
    n = int(sys.argv[3])

    print(f"El valor de la integral bajo la curva en el intervalo [{a}, {b}] usando {n} intervalos es:")
    integral(a, b, n)

if __name__ == "__main__":
    main()