# -*- coding: utf-8 -*-
import random

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
required_number = []
def comparison():
    number = random.choice(numbers[:-1])
    required_number.append(str(number))
    numbers.remove(number)
    for _ in range(3):
        number = random.choice(numbers)
        required_number.append(str(number))
        numbers.remove(number)
    print(required_number)

def is_correct_entry(number):
    if len(number) != 4:
        # print('Некорректный ввод')
        return False
    elif len(set(number)) != 4:
        # print('Некорректный ввод')
        return False
    for n in number:
        try:
            int(n)
        except ValueError:
            # print('Некорректный ввод')
            return False
    return True

def guess_the_number(number):
    herd = {'bools': 0, 'cows': 0}
    for numeral in number:
        for nnumeral in required_number:
            if numeral == nnumeral:
                herd['cows'] += 1
                # print(number.index(numeral), required_number.index(nnumeral))
                if number.index(numeral) == required_number.index(nnumeral):
                    herd['cows'] -= 1
                    herd['bools'] += 1
    return (herd)

def win(n):
    return required_number == list(n)

