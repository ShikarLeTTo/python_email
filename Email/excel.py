import sys

# задаём функцию выхода, первым аргументом будем передавать сообщение при выходе
def exit(exit_message):
        print exit_message
        sys.exit(0)

'''Собственно - функция диалога.
Первым аргументом принимаем ответ пользователя,
вторым - выдаём сообщение при неверном вводе'''
def answer(prompt, choice='Yes or no, please!'):
        while True:
                result = raw_input(prompt)
                if result in ('y', 'Y', 'yes', 'Yes'):
                        print 'nAs you choice "YES" - exiting now.n'
                        '''тут можно использовать оператор break вместо return
                        так же и в ответе No'''
                        return False
                elif result in ('n', 'N', 'no', 'No'):
                        print 'nAs your choice "NO" - I'll stay here...n'
                        a = 1
			'''тут просто цикл для демонстрации
                        использования оператора else в циклах'''
                        while a < 10:
                                print 'I'm number ' + str(a) + ' :-)'
                                a = a + 1
                        else:
                                exit('nExiting.n')
                else:
                        print(choice)

'''
используем операторы try и except, что бы корректно и красиво завершить скрипт при Ctrl+C (KeyboardInterrupt - SIGINT)
или Ctrl+D (EOFError - SIGQUIT) командах
'''
try:
        answer('nAre you sure to quite? ('y' or 'n', Ctrl+C for exit) ')
except (KeyboardInterrupt, EOFError):
        exit('nnExiting.n')
finally:
        print 'Tha's all folks.n'