def run():
    my_list=[1, "hello", True, 4.5]
    my_dict = {"first name": "Facundo", "last name": "García"}

    super_list=[
        {"first name": "Facundo", "last name": "García"},
        {"first name": "Miguel", "last name": "Torres"},
        {"first name": "Pepe", "last name": "Rodelo"},
        {"first name": "Susana", "last name": "Martinez"},
        {"first name": "José", "last name": "García"}
    ]

    super_dict={
        "natural_nums" : [1, 2, 3, 4, 5],
        "integer_nums" : [-2, -1, 0, 1, 2],
        "floating_nums" : [1.1, 4.5, 6.43]
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    for i in super_list:
        for key, value in i.items():
            print(key, "-", value)

if __name__ == '__main__':
    run()