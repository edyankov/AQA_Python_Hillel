"""
Задание #2:
Права доступа
Вирус повредил систему прав доступа к файлам. Известно, что над каждым файлом можно производить определенные действия:
запись – W;
чтение – R;
запуск – X.
На вход программе подается:
число n – количество файлов;
n строк с именами файлов и допустимыми операциями;
число m – количество запросов к файлам;
m запросов вида «операция файл».
Для каждого допустимого запроса программа должна возвращать OK, для недопустимого – Access denied.
"""

file_permissions = {}
access_permissions = {
    'W': 'write',
    'R': 'read',
    'X': 'execute'
}
for i in range(int(input("Enter amount of files: "))):
    x = input("Enter name of file: ").split()
    file_permissions[x[0]] = [access_permissions[i] for i in x[1:]]
for i in range(int(input("Enter amount of actions on files: "))):
    comm, n = input("Enter action on file: ").split()
    print('OK' if comm in file_permissions[n] else 'Access denied')

print("End")
