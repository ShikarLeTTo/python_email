#myfile=('email.txt', 'w')

inputfile = '../email.txt'
outputfile = '../email.txt'
myfile1 = open(inputfile, mode='r', encoding='latin_1')
myfile2 = open(outputfile, mode='w', encoding='latin_1') # perezapisivaet fail

for num, line in enumerate(myfile1, 1):
    if find_mail in line:
        print('Line № ' + str(num) + ' : ' + line.strip())
        myfile2.write('found password: ' + line)
myfile1.close()
myfile2.close()