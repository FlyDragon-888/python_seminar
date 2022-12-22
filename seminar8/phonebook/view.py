def main_menu():
    print()
    print('Телефонный справочник')
    n = input('1. Добавить контакт\n2. Все контакты\n3. Поиск\n4. Закрыть\nВыберите команду: ')
    if n in '1234':
        print()
        return int(n)
    else:
        print('Введите 1, 2, 3 или 4')

def write_contact():
    contact = [input('Введите имя: ').title(), input('Введите фамилию: ').title()]
    phone = input('Введите номер телефона: ')
    contact.append(phone)
    description = input('Введите описание: ')
    contact.append(description)
    print(f'Контакт добавлен: {str.join(", ", contact)}')
    return contact

def search():
    return input('Поиск: ')

def show_contact(data):
    print(f'Найдено записей: {len(data)}')
    for line in data:
        print(line)

def show_ext_contact(data):
    print(f'Найдено записей: {len(data)}\n')
    for line in data:
        for text in line:
            print(text)