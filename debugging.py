from torch import div


def divisor(num):
    divisor=[]
    for i in range(1, num+1):
        if num % i == 0: # revisando el código se cambio de 1 a 0 
            divisor.append(i)
    return divisor 


def run():
    try:
        num = int(input("Ingresa in número: "))
        if num <= 0:
            raise ValueError
        print(divisor(num))
        print("Terminó el programa")
    except ValueError:
        print("Debes escribir un número entero positivo")

if __name__=='__main__':
    run()