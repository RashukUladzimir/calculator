if __name__ == '__main__':

    a = float(input('Input first number: '))
    b = float(input('Input second number: '))
    sign = input('Input operation: ')

    if sign == '+':
        print(a + b)
    elif sign == '-':
        print(a - b)
    elif sign == '*':
        print(a * b)
    elif sign == '//':
        print(a // b)
    else:
        print('unknown operation')
