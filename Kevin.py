def parseFileOpen(tokens):
    for i in range(len(tokens)):
        a,b = 0,0
        if tokens[i][:8] == 'kevin:^)':
            a = i+1
            for j in range(a,len(tokens)):
                if '\n' in tokens[j]:
                    b = j
                    break
            tokens[i] = 'open'
            tokens[a] = '('+tokens[a]
            tokens[b] = tokens[b].replace('\n','')+',\'r\')\n'



def parseFileClose(tokens):
    for i in range(len(tokens)):
        a,b = 0,0
        if tokens[i][:8] == 'kevin:^(':
            a = i+1
            for j in range(a,len(tokens)):
                if '\n' in tokens[j]:
                    b = j
                    break
            tokens[i] = ''
            tokens[a] = tokens[a]
            tokens[b] = tokens[b].replace('\n','')
            tokens.insert(b+1,'.close()')
            tokens.insert(b+2, '\n')


def fileCheck(tokens):
    fileList = []
    for i in range(len(tokens)):
        if (tokens[i] == 'open') and (tokens[i-1] == '='):
            x = i-2
            tempList =[]
            while(tokens[x] != ''):
                tempList.append(tokens[x])
                x = x-1
            tempList.reverse()
            fileList.append(''.join(tempList))
        elif (tokens[i] == '.close()'):
            x = i-1
            tempList =[]
            while(tokens[x] != ''):
                tempList.append(tokens[x])
                x = x-1
            tempList.reverse()
            fileList.remove(''.join(tempList))
    if len(fileList) > 0:
        print("{} file(s) opened that are never closed! Variable name for file is:".format(len(fileList)))
        for file in fileList:
            print(file)
