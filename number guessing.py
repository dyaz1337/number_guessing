import random
for _ in range(10):
    num = random.randint(1, 100)
print('Добро пожаловать в числовую угадайку')
def is_valid(s):
    return s.isdigit() and 1 <= int(s) <= 100

def is_valid_num():
    while True:
        n = input()
        if is_valid(n):
            return int(n)
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')

def number_guessing():
    while True:
        n = is_valid_num()
        if n < num:
            print('Ваше число меньше загаданного, попробуйте еще разок')
        elif n > num:
            print('Ваше число больше загаданного, попробуйте еще разок')
        else:
            print('Вы угадали, поздравляем!')
            break

number_guessing()
