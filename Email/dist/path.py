def ReplaceLineInFile(fileName, sourceText, replaceText):
    file = open(fileName, 'r')
    text = file.read()
    file.close()
    file = open(fileName, 'w')
    file.write(text.replace(sourceText, replaceText))
    file.close()
    print('All went well, the modifications are done')