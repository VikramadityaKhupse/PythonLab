def pattern(num):
    # Upper part
    spaces = num*2 + 2
    space = 3
    for i in range(num):
        if i == 0:
            print(' '*spaces + '+' + ' '*spaces)
            spaces -= 2
        elif i == num-1:
            print(' '*spaces + '+' + ' '*(space // 2) + '' + ' '*(space // 2) + '+')
            spaces -= 2
            space += 4
        else:
            print(' '*spaces + '+' + ' '*space + '+')
            spaces -= 2
            space += 4
    # Lower part
    spaces = 2
    nextspaces =(num*2 - 1)*2
    for i in range(num):
        if i == num - 1:
            spaces += 2
            print(' '*spaces + '-' + ' '*nextspaces)
        else:
            print(' '*spaces + '+' + ' '*nextspaces + '+')
            spaces += 2
            nextspaces -= 3

pattern(3)