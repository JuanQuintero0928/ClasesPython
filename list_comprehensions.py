def run():
    # lista_1 = []

    # for i in range (1,11):
    #     lista_1.append(i**2)

    # print(lista_1) 
    
    # lista_2 = []

    # for i in range(1,101):
    #     dato = i**2
    #     if dato % 3 != 0:
    #         lista_2.append(dato)

    # print(lista_2)

    # list comprehensions --------------------------------------------------------------
    # el codigo de arriba se resume en las list comprehensions, utilizando el siguiente formato

    # ------------------------------------Esta es la solucion------------------------------------------ 

    # lista = [i**2 for i in range(1,101) if i % 3 != 0]  
    # print(lista)
    

    # actividad de la clase
    # Crear, con un list comprehensions, una lista de todos los multiplos de 4 que a la vez tambien son multiplos de 6 y de 9, hasta 5 digitos.

    lista = [i for i in range(1,99999) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]

    print(lista)

if __name__ =='__main__':
    run()