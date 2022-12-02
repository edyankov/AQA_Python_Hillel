"""
Задание #1:
Дано два множества A и B
В множестве А находятся имена должников за Сентябрь
В множестве B находятся имена должников за Октябрь
Найти:
* Вывести имена людей которые должны за Сентябрь и Октябрь
* Вывести должников за Октябрь у которых нет долга за Сентябрь
"""

A = {"Steven", "Lucas", "Emillio", "Sophie", "Mario", "Jason", "Anna", "Zarrin"}  # Names of debtors for September
B = {"Weldon", "Sophie", "Richard", "Anna", "Kumar", "Alfonso", "Emillio", "Mario"}  # Names of debtors for October

print("Names of debtors for September:", A.union(B))  # (A | B)

print("Names of debtors for September:", B.difference(A))  # (B - A)

print("End")
