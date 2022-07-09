import math

def run():
    # dicc = {}
    # for i in range(1,101):
    #     if i % 3 != 0:
    #         dicc[i] = i**3

    # print(dicc)

    dicc = {i: i**3 for i in range(1,101) if i % 3 != 0}
    print(dicc)

    # Reto
    # crear, con un dictionary comprehensions, un diccionario cuyas llaves sean los 1000 primeros numreos naturales con sus racies cuadradas como valores.
    # Con marh.sqrt se tiene la raiz cuadrada de dicho numero
    
    dicc_2 = {i: math.sqrt(i) for i in range (1,1001)}
    print(dicc_2)

if __name__=='__main__':
    run()