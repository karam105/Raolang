
code = "a"
tokens = []


def readProgramFile(filename):
    f = open(filename,'r')
    print("here")
    code = f.read()
    return code

# adding pipe sign between each rao term to separate
# them out easily in later functions
def tokenize(code):
    code = code.replace("rao","|rao")
    print(code)
    tokens = code.split("|")
    return tokens

# making it a habit that all checks are withing their separate functions
# so there is no need for additional changes to the main checker.

def checkHeader(tokens):
    if tokens[1][:5] != "rao:)":
        print("Invalid code format")
        return false
    else:
        return true

def syntaxChecker(tokens):
    # this function needs to check all token signatures with pre existing
    # ones to check if they are correct or not.

    # for token in tokens:
    #   if token[:5] != any existing signature from the list
    #       raise flag, return false, and possibly print line no.
    # return true if all correct

def lexicalChecker(tokens):
    # this can be built more
    # not sure about usage at the moment 2/6


code = readProgramFile("helloworld.rao")
tokens = tokenize(code)
if checkHeader(tokens):
    #do other things

