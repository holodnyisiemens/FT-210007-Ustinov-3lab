# a = ord('а')
# alphabet=''.join([chr(i) for i in range(a,a+6)] + [chr(a+33)] +
#     [chr(i) for i in range(a+6,a+32)])
# создание русского алфавита с добавлением буквы ё

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'    # строка из букв русского алфавита

def line_change (solution):
    new_string=''
    for i in range(len(string)):
        try:
            index = alphabet.index(string[i]) # поиск индекса символа строки (если это буква)
            new_string+=alphabet[(index+int(solution)*num)%33] # внесение в новую строку закодированного символа (33-число букв в русском алфавите)
        except ValueError:
            try:
                index = alphabet.index(string[i].lower()) # обработка ввода заглавной буквы
                new_string+=alphabet[(index+int(solution)*num)%33].upper() #возврат регистра буквы
            except ValueError:
                new_string+=string[i] # внесение символа не из русского алфавита
    return 'Расшифровка: '+ new_string + '\n'

def check_line(string):
    count=0 # счетчик кол-ва нерусских символов
    for char in string:
        if char.lower() in alphabet: # поиск хотя бы 1-го русского символа
            break
        else:
            count+=1
    return count

print('Программа шифрует/дешифрует строку (через шифр Цезаря)\n'
      'Сначала напишите строку, а потом выберете, что с ней сделать\n'
      'Для завершения работы программы введите 0')

while True: # бесконечный цикл (до отмены работы самим пользователем)
    string = input('Введите строку на русском языке (другие символы не изменятся) или 0: ')
    if string=='0':
        input('Работа программы завершена. Нажмите Enter для выхода из консоли')
        break    # введя 0 пользователь остановит работу программы
    else:
        if check_line(string) == len(string): # все символы в строке нерусские, выводится ошибка
            print ('Ошибка. Введите хотя бы 1 русский символ\n')
            continue
        
    while True:
        try: # обработка ввода
            num = int(input('Введите целое число смещений по алфавиту: '))
            break
        except ValueError:
            print('Ошибка ввода. Попробуйте еще раз')
            
    while True: # обработка ввода
        solution = input('Для расшифровки введите -1, для шифровки 1:')
        if solution=='-1' or solution == '1':
            print(line_change(solution))
            break # цикл обработки ввода обрывается при правильном вводе
        else:   # обработка ввода
            print('Ошибка. Попробуйте еще раз\n')
