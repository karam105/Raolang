from tokenize import tokenize, untokenize, NUMBER, STRING, NAME, OP
import sys
import string2rao.py

def c_name(token, string):
    return 

def c_op(token, string):
    return 

def c_string(token, string):
    return string2rao.convert(string)

def c_comment(token, string):
    newstring = 'rao?' + string2rao.convert(string.lstrip('#'))
    return newstring

def c_dedent(token, string):
    return 'raooo'

def c_indent(token, string):
    return 'raoo'

def c_newline(token, string):
    return '\n'

def convert(ttype, token string):
    if ttype == 'ENCODING':
        return
    elif ttype == 'ENDMARKER':
        return
    elif ttype == 'NAME':
        return c_name(token, string)
    elif ttype == 'OP':
        return 
    elif ttype == 'STRING':
        return 
    elif ttype == 'COMMENT':
        return c_comment(token, string)
    elif ttype == 'DEDENT':
        return c_dedent(token, string)
    elif ttype == 'INDENT':
        return c_indent(token, string)
    elif ttype == 'NL' or ttype == 'NEWLINE':
        return c_newline(token, string)
    else:
        fin.close()
        fout.close()
        message = 'Unexpected token type \'' + ttype + '\''
        raise RuntimeError(message)
        

print('Converting \'', sys.argv[1], 'to rao')

fin = open(sys.argv[1], 'rb')

if !fin.name.endswith('.py'):
    print('Expected .py file')
    fin.close()
    return

name = fin.name[:-3] + '.rao'
fout = open(name, 'w')

for token in tokenize(fin.readline):
    print(token)
##    print(token.type)
##    print(token.string)
##    print(token.start)
##    print(token.end)
##    print(token.line)

fin.close()
fout.close()
