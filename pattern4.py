def pattern(num):
    spaces = num * 2 + 2
    space = 3
    for i in range(num - 1):
        if i == 0:
            print(' ' * spaces + '+' + ' ' * spaces)
            spaces = spaces - 2
        if i == num - 2:
            print(' '*spaces + '+' + ' '*(space // 2) + '' + ' '*(space // 2) + '+')
            spaces = spaces - 2
            space += 4
        else:
            print(' ' * spaces + '+' + ' ' * space + '+')
            spaces = spaces - 2
            space += 4

    spaces = 3
    space = (num * 4) - 2
    for i in range(num):
        if i == num - 1:
            spaces += 1
            print(' ' * spaces + '-' + ' ' * space)

            space = space - 4
        else:
            print(' ' * spaces + '-' + ' ' * space + '-')
            spaces += 2
            space = space - 4



pattern(3)