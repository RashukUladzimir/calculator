if __name__ == '__main__':

    a = int(input('Input first number:'))
    b = int(input('Input second number:'))
    sign = input('Input operation:')

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
