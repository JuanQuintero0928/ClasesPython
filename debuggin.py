from pickle import TRUE


def divisor(num):
    try:
        if num < 0:
            raise ValueError("Debe ingresar un numero mayor a cero.")
        divisor = []
        for i in range(1, num + 1):
            if num % i == 0:
                divisor.append(i)
        return divisor
    except ValueError as ve:
        print(ve)
        return False

def run():
    try:
        num = int(input("Ingresa un numero : "))
        num = divisor(num)
        if num != False:
            print(num)
            print("termino el programa")
    except ValueError:
        print("Debes Ingresar un numero")

if __name__=='__main__':
    run()