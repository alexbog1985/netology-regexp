from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
cs = []
for row in contacts_list:
    fio = ' '.join(row[:3]).replace('  ', ' ').rstrip().split(' ')
    row[0] = fio[0]
    row[1] = fio[1]
    row[2] = fio[2] if len(fio) > 2 else ''
    print(row)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list)
