import csv
import re


def format_name(contacts):
    for i, j in enumerate(contacts[1:]):
        # форматировние ФИО
        name = (" ".join(j[:2])).split()
        k = 0
        while k < len(name):
            contacts[i + 1][k] = name[k]
            k += 1
    return contacts


def format_phone(contacts):
    i = 1
    while i < len(contacts):
        contacts[i][5] = re.sub(r"(\+7|8)\s*\(?(\d{3})\)?[-\s]?(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})", r"+7(\2)\3-\4-\5",
                                contacts[i][5])
        contacts[i][5] = re.sub(r"\(?(доб.)\s(\d+)\)?", r"\1\2", contacts[i][5])
        i += 1
    return contacts


def match_merge(contacts):
    i = 1
    while i<len(contacts):
        j = len(contacts)-1
        while j>i:
            if contacts[i][0]==contacts[j][0] and contacts[i][1]==contacts[j][1]:
                k=3
                while k<7:
                    if contacts[j][k]!='':
                       contacts[i][k] = contacts[j][k]
                    k += 1
                contacts.pop(j)
            j -= 1
        i += 1
    return contacts


if __name__ == "__main__":
    with open("phonebook_raw.csv") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    # TODO 1: выполните пункты 1-3 ДЗ
    contacts_list = format_name(contacts_list)
    contacts_list = format_phone(contacts_list)
    contacts_list = match_merge(contacts_list)

    # TODO 2: сохраните получившиеся данные в другой файл
    with open("phonebook.csv", "w") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list)


