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
