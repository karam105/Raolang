# Author: Rao Hamza Ali, who should be doing his Math homework right now.
# Co-author: Kevin Lisbin
# Version: 0.1

import dictionary as p
import Kevin
import runpy

strList = []
varList = []


def readProgramFile(filename):
    f = open(filename, 'r')
    print("Reading code file...")
    code = f.read()
    return code


# adding pipe sign between each rao term to separate
# them out easily in later functions
def tokenize(code):
    #print("Removing spaces...")
    #code = code.replace(" ", "") # taking this out, doesn't work with comments. Needs fix or removal 4/8
    print("Tokenizing code...")
    code = code.replace("roa", "rao")  # small spell checker
    code = code.replace("rao", "|rao")
    code = code.replace("kevin", "|kevin")
    tokens = code.split("|")
    return tokens


# making it a habit that all checks are withing their separate functions
# so there is no need for additional changes to the main checker.

# check if header exists or not
def checkHeader(tokens):
    if tokens[1][:5] != "rao:)":
        print("Invalid code format, header not found")
        return False
    else:
        print("Header found")
        return True


# check if footer exists or not
def checkFooter(tokens):
    a = len(tokens)
    if tokens[a - 1][:5] != "rao:(":
        print("Invalid code format, code has no end")
        return False
    else:
        print("Footer found")
        return True


# check if user has asked for help; as in what commands are in the dictionary
# probably not implemented correctly but the idea is there
# do not use invoke function, not working 4/8
def checkHelp(tokens):
    if tokens[2][:4] == "raoH":
        for token in tokens:
            print(p.parseDictionary)
            return


# checks each command in code file against commands from dictionary
def syntaxChecker(tokens):
    linenumber = 0
    quote = 0
    for token in tokens:

        if 'rao"' in token:
            if quote == 0:
                quote = 1
            else:
                quote = 0

        if '\n' in token:
            linenumber += 1
            if quote == 1:
                print("missing closing quotation mark at line {}".format(linenumber))
                quit(0)
        if token == '':
            continue
        if token[:8] not in p.checkList:
            if token[:4] not in p.checkList:
                print("line:", linenumber, " following command not found:", token)
                return

    print("Syntax seems okay...")

    # what's left:
    # add more commands


# no idea how this will work, generate dictionary of all variables maybe?
def lexicalChecker(tokens):
    return 1
    # this can be built more
    # still not sure about usage at the moment 2/11


# puts all indices with rao" in a separate list
# used to parse literal strings
def stringList(tokens):
    for i in range(len(tokens)):
        if 'rao"' in tokens[i]:
            strList.append(i)


# main parse method calling all other sub functions
def parser(tokens):
    parseDictionaryCommands(tokens)
    parseStringLiterals(tokens)
    parseVariables(tokens)
    parsePrint(tokens)
    parseLoop(tokens)
    addIndentation(tokens)
    parseKeyboardIn(tokens)
    parseNumbers(tokens)
    Kevin.parseFileOpen(tokens)
    Kevin.parseFileClose(tokens)
    parseFunctions(tokens)
    cpy = tokens  # making copy for reasons unbestknown to us all
    # print(tokens)


def parseLoop(tokens):
    print("Unlooping loops...")
    for i in range(len(tokens)):
        a, b = 0, 0
        if tokens[i] == 'rao&':
            print("Found a while loop")
            a = i + 1
            for j in range(a, len(tokens)):
                if '\n' in tokens[j]:
                    b = j
                    break
            tokens[i] = 'while'
            tokens[a] = '(' + tokens[a]
            tokens[b] = tokens[b].replace('\n', '') + '):\n'

def parseFunctions(tokens):
    print("Decompressing functions...")
    for i in range(len(tokens)):
        a,b =0,0
        if tokens[i] == 'def ':
            a = i+1
            for j in range(a,len(tokens)):
                if tokens[j] == ')\n':
                    tokens[j] = '):\n'
                    break

def addIndentation(tokens):
    print("Tabbing the untabbed...")
    for i in range(len(tokens)):
        a,b = 0,0
        if tokens[i] == 'raoo\n':
            tokens[i+1] = '\t' + tokens[i+1]
            tokens[i] = ''
            a = i+1
            for j in range(a,len(tokens)):
                if 'raooo' in tokens[j]:
                    b = j-1
                    tokens[j] = ''
                    break
            for k in range(a,b):
                if('\n' in tokens[k]):
                    tokens[k+1] = '\t' + tokens[k+1]


def parseNumbers(tokens):
    print("Replacing numbers...")
    a, b = 0, 0  # lower upper range values of inner list
    # check all tokens, if any of them is a variable command
    # initialize lower range, find all rao@s to go with the variable name
    # and then initialize the upper range. Replace. Continue to find more.
    for i in range(len(tokens)):
        if tokens[i][:4] == 'rao~':
            a = i + 1
            numberList = []
            for j in range(a, len(tokens)):
                if tokens[j][:4] == 'rao@':
                    numberList.append(tokens[j])
                else:
                    b = j
                    break
            ind = 0
            for k in range(a, b):
                if '\n' in tokens[k]:
                    tokens[k] = toString(numberList[ind].replace("rao@", "")) + '\n'
                else:
                    tokens[k] = toString(numberList[ind].replace("rao@", ""))
                ind += 1
            tokens[i] = ''


# checks all variable commands (rao$) and replaces their
# names with ascii char alternatives
def parseVariables(tokens):
    print("Replacing variable names...")
    a, b = 0, 0  # lower upper range values of inner list
    # check all tokens, if any of them is a variable command
    # initialize lower range, find all rao@s to go with the variable name
    # and then initialize the upper range. Replace. Continue to find more.
    for i in range(len(tokens)):
        if tokens[i][:4] == 'rao$':
            a = i + 1
            varcharList = []
            for j in range(a, len(tokens)):
                if tokens[j][:4] == 'rao@':
                    varcharList.append(tokens[j])
                else:
                    b = j
                    break
            ind = 0
            for k in range(a, b):
                if '\n' in tokens[k]:
                    tokens[k] = toString(varcharList[ind].replace("rao@", "")) + '\n'
                else:
                    tokens[k] = toString(varcharList[ind].replace("rao@", ""))
                ind += 1
            tokens[i] = ''


# replaces rao# with a print function
# main concern here was adding () appropriately
def parsePrint(tokens):
    print("Adding python friendly Print function...")
    # check all tokens, initialize lower range
    # look for a newline and stop there. Replace. Continue
    for i in range(len(tokens)):
        a, b = 0, 0
        if tokens[i][:4] == 'rao#':
            a = i + 1
            for j in range(a, len(tokens)):
                if '\n' in tokens[j]:
                    b = j
                    break
            tokens[i] = 'print'
            tokens[a] = '(' + tokens[a]
            tokens[b] = tokens[b].replace('\n', '') + ')\n'


def parseKeyboardIn(tokens):
    print("Adding keyboard input function...")
    # check all tokens, initialize lower range
    # look for a newline and stop there. Replace. Continue
    for i in range(len(tokens)):
        a, b = 0, 0
        if tokens[i][:4] == 'rao_':
            a = i + 1
            for j in range(a, len(tokens)):
                if '\n' in tokens[j]:
                    b = j
                    break
            tokens[i] = 'input'
            tokens[a] = '(' + tokens[a]
            tokens[b] = tokens[b].replace('\n', '') + ')\n'


# this function does a direct replacement of one to one commands
# rao" to ", rao= to = etc.
def parseDictionaryCommands(tokens):
    print("Converting basic commands...")
    for t in range(len(tokens)):
        if tokens[t][:5] == 'rao:(' or tokens[t][:5] == 'rao:)':
            tokens[t] = '\n'
        if p.parseDictionary.get(tokens[t][:4], 'undefined') != 'undefined':
            tokens[t] = tokens[t].replace(tokens[t][:4], p.parseDictionary[tokens[t][:4]])


# parses literal string characters to their acsii alternates
def parseStringLiterals(tokens):
    # check for even length of strList
    # otherwise there is syntax error (potentially move to syntaxChecker)

    # keep a list of token indices of rao" occurrences
    # starting in reverse, pop the indexes a and b that
    # are the range for a string literal. Convert. Replace. Repeat
    print("Parsing string literals...")
    while len(strList) != 0:
        b = strList.pop()
        a = strList.pop()
        stringList = tokens[a + 1:b]
        for i in range(len(stringList)):
            stringList[i] = stringList[i].replace("rao@", "")
            stringList[i] = toString(stringList[i])
        # print(stringList)
        k = 0
        for j in range(a + 1, b):
            if '\n' in tokens[j]:
                tokens[j] = stringList[k] + '\n'
            else:
                tokens[j] = stringList[k]
            k += 1


# takes a rao character and converts to ascii character
def toString(value):
    h = value.count('!')
    t = value.count(',')
    u = value.count('.')
    dcml = h * 100 + t * 10 + u * 1
    return chr(dcml)


# creates output.py with converted code file
def generateOutput(tokens):
    print("Generating output.py file...")
    f = open("output.py", "w", newline="")
    for token in tokens:
        f.write(token)
    f.close()



# main execution of the parser
code = readProgramFile("helloworld.rao")
tokens = tokenize(code)
checkHeader(tokens)
checkFooter(tokens)
syntaxChecker(tokens)
stringList(tokens)
parser(tokens)
Kevin.fileCheck(tokens)
generateOutput(tokens)
print("Testing your patience...")
print("Executing output.py...\n")
runpy.run_path('output.py')  # desperate times, desperate measures
