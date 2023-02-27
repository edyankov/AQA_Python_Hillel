""""Arg-parser": Створити python-програму, звпустивши яку з аргументом -h або --help в консоль буде виведено текст:
"Тут могла бути ваша... допомога =)", а якщо передати аргумент -n або --name та ввести ім'я "Валєнтін",
то в консоль буде надруковано: "Валєнтін, японскій бог, ти зачєм у ката яйца-та аткрутіл?!",
а якщо буде введено інше ім'я, то в консоль надрукується "Welcome," та це ім'я."""

import argparse

parser = argparse.ArgumentParser(description='my_parser_prog', add_help=False)

parser.add_argument('--name', '-n', type=str)
parser.add_argument('--help', '-h', action='store_true')

arguments = parser.parse_args()

if arguments.help:
    print("Тут могла бути ваша... допомога =)")
    parser.print_help()
elif arguments.name:
    if arguments.name == 'Валєнтін':
        print("Валєнтін, японскій бог, ти зачєм у ката яйца-та аткрутіл?!")
    else:
        print(f'Welcome, {arguments.name}!')
