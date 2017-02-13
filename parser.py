import dictionary as p
code = ""
tokens = []
strList = []
varList = []


def readProgramFile(filename):
    f = open(filename,'r')
    print("reading code file...")
    code = f.read()
    return code

# adding pipe sign between each rao term to separate
# them out easily in later functions
def tokenize(code):
    code = code.replace("rao","|rao")
    print("tokenized code...")
    #print(code)
    tokens = code.split("|")
    #print(tokens)
    return tokens

# making it a habit that all checks are withing their separate functions
# so there is no need for additional changes to the main checker.

def checkHeader(tokens):
    if tokens[1][:5] != "rao:)":
        print("Invalid code format, header not found")
        return False
    else:
        print("Header found")
        return True

def checkFooter(tokens):
    a = len(tokens)
    if tokens[a-1][:5] != "rao:(":
        print("Invalid code format, code has no end")
        return False
    else:
        print("Footer found")
        return True


def syntaxChecker(tokens):
    linenumber = 0
    for token in tokens:
        if '\n' in token:
            linenumber+=1
        if  token == '':
            continue
        if token[:4] not in p.checkList:
            print("line:",linenumber," following command not found:",token)
            break
    print("Syntax seems okay...")
    
    # what's left:
        # add more commands
        # if space in code, that's an error. This is a space free environment

def lexicalChecker(tokens):
    return 1
    # this can be built more
    # still not sure about usage at the moment 2/11


def stringList(tokens):
    for i in range(len(tokens)):
        if 'rao"' in tokens[i]:
            strList.append(i)


def parser(tokens):
    parseDictionaryCommands(tokens)
    parseStringLiterals(tokens)
    parseVariables(tokens)
    cpy = tokens # making copy for reasons unbestknown to us all
    #print(tokens)

def parseVariables(tokens):
    for i in range(len(tokens)):
        if tokens[i][:4] == 'rao$':
            varList.append(i)
    print(varList)

def parseDictionaryCommands(tokens):
    for t in range(len(tokens)):
        if tokens[t][:5] == 'rao:(' or tokens[t][:5] == 'rao:)':
            tokens[t] = '\n'
        if p.parseDictionary.get(tokens[t][:4],'undefined') != 'undefined':
            tokens[t] = tokens[t].replace(tokens[t][:4],p.parseDictionary[tokens[t][:4]])

def parseStringLiterals(tokens):
    # check for even length of strList
    # otherwise there is syntax error (move to syntaxChecker)
    while len(strList) != 0:
        b = strList.pop()
        a = strList.pop()
        stringList = tokens[a+1:b]
        for i in range(len(stringList)):
            stringList[i] = stringList[i].replace("rao@","")
            stringList[i] = toString(stringList[i])
        #print(stringList)
        k = 0
        for j in range(a+1,b):
            tokens[j] = stringList[k]
            k+=1

def toString(value):
    h = value.count('!')
    t = value.count(',')
    u = value.count('.')

    dcml = h*100 + t*10 + u*1
    return(chr(dcml))
    
def generateOutput(tokens):
    f = open("output.py","w",newline="")
    for token in tokens:
        f.write(token)
    f.close()

a = 'rao='
print(a[:4])
b = p.parseDictionary.get("",'undefined')
print(b)
code = readProgramFile("helloworld.rao")
tokens = tokenize(code)
checkHeader(tokens)
checkFooter(tokens)
syntaxChecker(tokens)
stringList(tokens)
parser(tokens)
generateOutput(tokens)

#if checkHeader(tokens):
    #do other things

