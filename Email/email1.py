import sys
import os
import string
from random import *

def new():
    return start()


def clr():
    os.system('cls')


def menu():
    print('Список пользователей почты домена @csdalzavod.ru')
    print('1. Внести новую почту')
    print('2. Найти')
    print('3. Генератор пароля')
    print('4. Выход')
    pick = int(input())
    if pick == 1:
        clr()
        return new_email()
    elif pick == 2:
        clr()
        return find()
    elif pick == 3:
        clr()
        return genpass()
    elif pick == 4:
        sys.exit()
    else:
        print('Некорректно!')
        input('Нажмите клавишу для продолжения...')
        clr()
        return menu()


def new_email():
    email = input('Введите email: ')
    password = input('Введите password: ')
    name = input('Ввдеите ФИО: ')
    mail = [email, password, name]
    inputfile = 'email.txt'
    myfile = open(inputfile, 'a')
    myfile.write(', '.join(mail) + '\n')
    myfile.close()
    array()
    start()


def start():
    while True:
        try:
            cont = input('Продолжить? y/n, Ctrl + C для выхода: ')
            if cont in ('y', 'Y', 'yes', 'Yes'):
                clr()
                return new_email()
            elif cont in ('n', 'N', 'no', 'No'):
                print('Выход!')
                clr()
                return menu()
            else:
                print('Некорректно')
                return new()
        except (KeyboardInterrupt, ValueError, UnicodeError, EOFError, Exception):
            print("ERROR!")
            # sys.exit(0)


def find():
    find_word = input('Введите имя для поиска: ')

    file = 'email.txt'
    myfile = open(file, mode='r')
    for num, line in enumerate(myfile, 1):
        if find_word.lower() in line.lower():
            print('Find №' + str(num) + ': ' + line)
            input('Нажмите клавишу для продолжения...')
            clr()
            return menu()
        # else:
        #     print('Пользователь не найден!')
        #     input('Нажмите клавишу для продолжения...')
        #     clr()
        #     return find()
    myfile.close()


def array():
    package = 'email.txt'
    try:
        file = open(package, 'r+')
        pos = 0
        line = file.readlines()
        file.seek(pos)
        sort_text = sorted(line)
        for new_line in sort_text:
            file.write(new_line)
        file.close()
    except IOError:
        print("Повторите пожалуйста!")


def genpass():
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation
    chars = letters + digits + symbols

    min_length = 8
    max_length = 8
    password = ''.join(choice(chars)
    for _ in range(randint(min_length, max_length)))
    print(password)
    input('Нажмите клавишу для продолжения...')
    clr()
    return menu()


menu()