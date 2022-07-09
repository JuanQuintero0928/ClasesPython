def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"nombre": "juan jose", "Apellido":"Quintero"}

    super_list = [
        {"nombre":"juan jose", "Apellido":"Quintero"},
        {"nombre":"laura", "Apellido":"suarez"},
        {"nombre":"manuela", "Apellido":"velez"},
        {"nombre":"santiago", "Apellido":"morales"}       
    ]

    super_dict = {
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for i in super_list:
        print(i["nombre"],"-",i["Apellido"])

if __name__ == '__main__':
    run()