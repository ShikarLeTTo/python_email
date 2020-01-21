from __future__ import print_function
import io

word = input()
with io.open('C:/Users/letunovda/Desktop/Email/email.txt') as file:
    for line in file:
        if word in line:
            print(line, end='')
        else:
            print('Not found')
