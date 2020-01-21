package = 'email.txt'
try:
    file = open(package, 'r+')
    pos = 0
    line = file.readlines()
    file.seek(pos)
    sort_text = sorted(line)
    for new_line in sort_text:
        file.write(new_line)
        pos = file.tell()
    file.close()
except IOError:
    print("Повторите пожалуйста!")
