
def read_txt(filename):

    phone_book= []
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.strip().split(',')))
            phone_book.append(record)
    return phone_book




def write_txt(filename, phone_book):
    with open(filename,'w',encoding='utf-8') as phout:

        for i in range(len(phone_book)):
            s=' '
            for v in phone_book[i].values():
                s+=v+','
            phout.write(f'{s[:-1]}\n')



def show_menu():
    print('1. Распечатать справочник',
          '2. Найти телефон по фамилии',
          '3. Изменить номер телефона',
          '4. Удалить запись',
          '5. Найти абонента по номеру телефона',
          '6. Добавить абонента в справочник',
          '7. Закончить работу', sep = '\n')
    choice=int(input("Введите номер команды: "))
    return choice


def find_by_lastname(phone_book,last_name):
    listA = []
    for i in range(len(phone_book)):
        if last_name in phone_book[i]['Фамилия']:
            listA.append(phone_book[i]['Телефон']+ ' ' + phone_book[i]['Фамилия'] + ' ' + phone_book[i]['Имя'] )
    return listA
    
def change_number(phone_book,last_name,new_number):
    for i in range(len(phone_book)):
        if last_name in phone_book[i]['Фамилия']:
            phone_book[i].update({'Телефон':new_number})
    return phone_book
    
def delete_by_lastname(phone_book,last_name):
    new_phone_book = []
    for i in range(len(phone_book)):
        if last_name != phone_book[i]['Фамилия']:
            new_phone_book.append(phone_book[i])
    return new_phone_book


def find_by_number(phone_book,number):
    listB = []
    for i in range(len(phone_book)):
        if number == phone_book[i]['Телефон']:
            listB.append(phone_book[i]['Фамилия'] + ' ' + phone_book[i]['Имя'])
    return listB


def add_user(phone_book):
    new_data = {}

    last_name = input('Фамилия: ')
    new_data.update({'Фамилия': last_name})

    first_name = input('Имя: ')
    new_data.update({'Имя': first_name})

    number = input('Введите номер: ')
    new_data.update({'Телефон': number})

    description =input('Введите описание: ')
    new_data.update({'Описание': description})

    phone_book.append(new_data)
    return phone_book
    


def work_with_phonebook():
    choice=show_menu()
    phone_book= read_txt('phonebook.csv')
    while (choice!=7):

        if choice==1:
            print(phone_book)

        elif choice==2:
            last_name = input('Введите фамилию:  ')
            print(find_by_lastname(phone_book,last_name))

        elif choice==3:
            last_name=input('Введите фамилию: ')
            new_number=input('Введите новый номер: ')
            print(change_number(phone_book,last_name,new_number))

        elif choice==4:
            lastname=input('Введите фамилию: ')
            print(delete_by_lastname(phone_book,lastname))

        elif choice==5:
            number=input('Введите телефон: ')
            print(find_by_number(phone_book,number))

        elif choice==6:
            add_user(phone_book)
            write_txt('phonebook.csv',phone_book)

        choice=show_menu()
    

work_with_phonebook()



    