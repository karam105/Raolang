# Converts strings to raolang strings
def convert(string):
    converted = ''

    for char in string:
        converted += 'rao@'
        val = ord(char)
        valstr = str(val)
        place = 100 if len(valstr) == 3 else 10 if len(valstr) == 2 else 1

        # each iteration is 1 place in the ascii value
        for i in range(len(valstr)):
            num = int(valstr[i])
            for n in range(num):
                if place == 100:
                    converted += '!'
                elif place == 10:
                    converted += ','
                else:
                    converted += '.'
            # advance to the next place
            place = place / 10

    return converted

f = open('rao_converted.txt', 'a')
running = True

while running:
    user_input = input('Convert: ')

    if user_input == 'rao(:':
        running = False
        f.close()
        break

    print('Success!')
    f.write('{0} => {1}\n'.format(user_input, convert(user_input)))
