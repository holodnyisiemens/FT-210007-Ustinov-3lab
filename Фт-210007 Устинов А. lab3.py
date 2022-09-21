a = ord('а')
alphabet=''.join([chr(i) for i in range(a,a+6)] + [chr(a+33)] +
    [chr(i) for i in range(a+6,a+32)])
print('Программа шифрует/дешифрует строку (через шифр Цезаря)\n'
      'Сначала напишите строку, а потом выберете, что с ней сделать\n'
      'Для завершения работы программы введите 0')
while True:
    string = input('Введите строку на русском (другие символы не изменятся) или 0: ')
    if string=='0':
        print('Работа программы завершена')
        break
    num = int(input('Введите целое число смещений по алфавиту: '))
    solution = input('Для расшифровки введите -1, для шифровки 1:')
    new_string=''
    if solution=='-1':
        for i in range(len(string)):
            try:
                index = alphabet.index(string[i])
                new_string+=alphabet[(index-num)%33]
            except ValueError:
                try:
                    index = alphabet.index(string[i].lower())
                    new_string+=alphabet[(index-num)%33].upper()
                except ValueError:
                    new_string+=string[i]
        print('Расшифровка: '+ new_string + '\n')
    elif solution=='1':
        for i in range(len(string)):
            try:
                index = alphabet.index(string[i])
                new_string+=alphabet[(index+num)%33]
            except ValueError:
                try:
                    index = alphabet.index(string[i].lower())
                    new_string+=alphabet[(index+num)%33].upper()
                except ValueError:
                    new_string+=string[i]
        print('Шифровка: '+new_string+'\n')
    else:
        print('Ошибка. Попробуйте еще раз\n')
