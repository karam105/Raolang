import dictionary as p
code = ""
tokens = []
strList = []



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


def parser(tokens):
    print(tokens)
    cpy = tokens # making copy for reasons unbestknown to us all
    for token in cpy:
        if token == 'rao:(' or token == 'rao:)':
            token = ''
        if p.parseDictionary.get(token[:4],'undefined') != 'undefined':
            token = token.replace(token[:4],p.parseDictionary[token[:4]])
            #token[:4] = p.parseDictionary[token[:4]]
        #print(token)
    # check for even length of strList
    # otherwise there is syntax error (move to syntaxChecker)
    while len(strList) != 0:
        b = strList.pop()
        a = strList.pop()
        
    print(tokens)

def stringList(tokens):
    for i in range(len(tokens)):
        if 'rao"' in tokens[i]:
            strList.append(i)

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

#if checkHeader(tokens):
    #do other things

