from Dict import *


def menu():
    with open('input.txt', 'r', encoding='ascii') as file:
        text = file.read()
    case = input('Ввод с клавиатуры? y/n\n>>>\t')

    if case == 'y':
        text = input('Ввод:\t')

    choose = input('1 - BASE64\n2 - BASE32\n>>>\t')

    if choose == '1':
        flag = input('1 - encode\n2 - decode\n>>>\t')
        base_64(text, flag)

    elif choose == '2':
        flag = input('1 - encode\n2 - decode\n>>>\t')
        base_32(text, flag)


def text_to_bin(text):
    return ''.join(format(x, '08b') for x in bytearray(text, 'ascii'))


def base_64(text, flag):
    if flag == '1':
        var1 = text
        temp_list = []
        text = text_to_bin(text)
        count = 0

        while len(text) % 24 != 0:
            text = text + '00000000'
            count += 1

        for i in range(len(text)):
            if i % 6 == 0:
                var = text[i:i + 6]
                temp_list.append(var)

        for i in range(len(temp_list)):
            temp_list[i] = alf_dict[temp_list[i]]

        encode = ''.join(temp_list)

        if count == 1:
            encode = encode[:-1] + '='
        elif count == 2:
            encode = encode[:-2] + '=='

        with open("output.txt", "a", encoding='utf-8') as file:
            file.write('BASE64:\t\t\tисходное сообщение: {} ---> вывод: {}\n'.format(var1, encode))

        return encode

    elif flag == '2':
        var1 = text
        temp_list = []

        for i in range(len(text)):
            temp_list.append(text[i])

        count = temp_list.count('=')
        if count == 2:
            del temp_list[-1]
            del temp_list[-1]

        elif count == 1:
            del temp_list[-1]

        for i in range(len(temp_list)):
            temp_list[i] = dict_alf[temp_list[i]]
        text = ''.join(temp_list)

        if count == 2:
            text = text[:-4]
        elif count == 1:
            text = text[:-2]

        temp_list = []

        for i in range(len(text)):
            if i % 8 == 0:
                var = text[i:i + 8]
                temp_list.append(var)

        for i in range(len(temp_list)):
            temp_list[i] = chr(int(temp_list[i], 2))

        with open("output.txt", "a", encoding='utf-8') as file:
            file.write('BASE64 DECODE:\tисходное сообщение: {} ---> вывод: {}\n'.format(var1, ''.join(temp_list)))

        return ''.join(temp_list)


def base_32(text, flag):
    if flag == '1':
        var1 = text
        temp_list = []
        text = text_to_bin(text)
        count = 0

        while len(text) % 5 != 0:
            text = text + "0"
            count += 1

        for i in range(len(text)):
            if i % 5 == 0:
                var = text[i:i + 5]
                temp_list.append(var)

        for i in range(len(temp_list)):
            temp_list[i] = alf_dict_32[temp_list[i]]

        encode = ''.join(temp_list)

        if count == 3:
            encode = encode + '='

        elif count == 1:
            encode = encode + '==='

        elif count == 4:
            encode = encode + '===='

        elif count == 2:
            encode = encode + '======'

        with open("output.txt", "a", encoding='utf-8') as file:
            file.write('BASE32:\t\t\tисходное сообщение: {} ---> вывод: {}\n'.format(var1, encode))

        return encode

    elif flag == '2':
        var1 = text
        temp_list = []
        for i in range(len(text)):
            temp_list.append(text[i])

        count = temp_list.count('=')
        for i in range(count):
            temp_list.remove('=')

        for i in range(len(temp_list)):
            temp_list[i] = dict_alf_32[temp_list[i]]
        text = ''.join(temp_list)

        if count == 6:
            text = text[:-2]
        elif count == 4:
            text = text[:-4]
        elif count == 3:
            text = text[:-1]
        elif count == 1:
            text = text[:-3]

        temp_list = []

        for i in range(len(text)):
            if i % 8 == 0:
                var = text[i:i + 8]
                temp_list.append(var)

        for i in range(len(temp_list)):
            temp_list[i] = chr(int(temp_list[i], 2))

        with open("output.txt", "a", encoding='utf-8') as file:
            file.write('BASE32 DECODE:\tисходное сообщение: {} ---> вывод: {}\n'.format(var1, ''.join(temp_list)))

        return ''.join(temp_list)


menu()
