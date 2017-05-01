def parseBessie(tokens):
    print("Generating cow figures...")
    for i in range(len(tokens)):
        if tokens[i] == 'bessie\n':
            tokens[i] = 'bessie.moo()'
        tokens[0] = tokens[0]+'import bessie\n'
def moo():
    a = '         (    )'
    b = '          (oo)'
    c = ' )\.-----/(O O)'
    d = '# ;       / u'
    e = ' (  .   |} )'
    f = '  |/ `.;|/;'
    g = '  "     " "'

    print(a+"\n"+b+"\n"+c+"\n"+d+"\n"+e+"\n"+f+"\n"+g)
