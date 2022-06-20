from torch import div


def divisor(num):
    divisor=[]
    for i in range(1, num+1):
        if num % i == 0: # revisando el código se cambio de 1 a 0 
            divisor.append(i)
    return divisor 


def run():
    num = (input("Ingresa in número: "))
    assert num.isnumeric() and int(num) > 0, "Debes ingresar un número entero positivo"
    print(divisor(int(num)))
    print("Terminó el programa")


if __name__=='__main__':
    run()