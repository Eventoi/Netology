import csv
import re
import os

def format_phone(phone):
    # Форматируем телефон в формат +7(999)999-99-99
    if 'доб' in phone:
        phone_parts = phone.split()
        phone = '+7(' + phone_parts[0] + ') ' + phone_parts[1] + '-' + phone_parts[2].replace('-', '') + ' доб.' + phone_parts[3]
    else:
        phone = '+7(' + phone[:3] + ') ' + phone[3:6] + '-' + phone[6:8] + '-' + phone[8:10]
    return phone

def process_contacts(contacts_list):
    # Группируем записи по ФИО
    contacts_dict = {}
    for contact in contacts_list:
        full_name = ' '.join(contact[:3])
        if full_name not in contacts_dict:
            contacts_dict[full_name] = []
        contacts_dict[full_name].append(contact)

    # Объединяем дублирующиеся записи о человеке в одну
    processed_contacts = []
    for full_name, contacts in contacts_dict.items():
        if len(contacts) == 1:
            processed_contacts.append(contacts[0])
        else:
            merged_contact = contacts[0]
            for contact in contacts[1:]:
                if len(merged_contact[4]) > 0 and len(contact[4]) > 0 and merged_contact[4] != contact[4]:
                    raise ValueError("Duplicate contacts with different phone numbers")
                if len(merged_contact[5]) > 0 and len(contact[5]) > 0 and merged_contact[5] != contact[5]:
                    raise ValueError("Duplicate contacts with different email addresses")
                merged_contact[4] = merged_contact[4] or contact[4]
                merged_contact[5] = merged_contact[5] or contact[5]
            processed_contacts.append(merged_contact)

    # Форматируем телефоны и разбиваем ФИО на фамилию, имя и отчество
    for contact in processed_contacts:
        contact[4] = format_phone(contact[4])
        name_parts = contact[0].split()
        if len(name_parts) == 2:
            contact[0], contact[1], contact[2] = name_parts[0], name_parts[1], ''
        else:
            contact[0], contact[1], contact[2] = name_parts[0], ' '.join(name_parts[1:-1]), name_parts[-1]

    return processed_contacts

# Получаем текущий рабочий каталог
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "phonebook_raw.csv")

# Читаем адресную книгу в формате CSV в список contacts_list
with open(file_path, encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# Выполняем пункты 1-3 ДЗ
processed_contacts = process_contacts(contacts_list)

# Сохраняем в текущий рабочий каталог
current_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_dir, "phonebook.csv")

# Сохраняем получившиеся данные в другой файл
with open("phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(processed_contacts)