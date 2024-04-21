import re

from collections import defaultdict

from pprint import pprint

# читаем адресную книгу в формате CSV в список contacts_list
import csv

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
pattern_phone = re.compile(r"(\+?7|8).*(495)\D*(\d{3})\D*(\d{2})\D*(\d{2})")
pattern_ext = re.compile(r"\s*.(доб\.).(\D*)(\d*).*", re.IGNORECASE)

for row in contacts_list:
    fio = ' '.join(row[:3]).replace('  ', ' ').rstrip().split(' ')
    row[0] = fio[0]
    row[1] = fio[1]
    row[2] = fio[2] if len(fio) > 2 else ''

    # print(row[5])
    if row[5]:
        row[5] = pattern_phone.sub(r"+7(\2)\3-\4-\5", row[5])
        row[5] = pattern_ext.sub(r" доб.\3", row[5])\

data = defaultdict(list)

for row in contacts_list:
    key = row[0], row[1]
    for i in row:
        if i not in data[key]:
            data[key].append(i)

contacts_list_2 = list(data.values())
pprint(contacts_list_2)


# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list_2)
