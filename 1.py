a = int(input('input 1 number: '))
b = int(input('input 2 number: '))

z = str(input('input need act: '))

if z == '+':
    print(a+b)

elif z == '-':
    print(a-b)

elif z == '/':
    print(a/b)

elif z == '*':
    print(a*b)

elif z == 'mod':
    print(a%b)

elif z == 'div':
    print(a//b)

else:
    print('select one of the possible operations: "+" "-", "/", "*", "mod", "div" ')

