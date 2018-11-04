def grid():
    print(
'''
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
|         |         |
|         |         |
|         |         |
|         |         |
+ - - - - + - - - - +
''')

def row():
    print(('+' + '-'* 4 ) * 2 + '+')

def column():
    print('|    '* 3)

def draw():
    row()
    column()
    column()
    column()
    column()
    row()
    column()
    column()
    column()
    column()
    row()

draw()

grid()

