file = 'email.txt'
myfile = open(file)
for num, line in enumerate(myfile, 1):
    print(str(num) + ': ' + line)
myfile.close()
