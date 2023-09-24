from string import ascii_lowercase
ABC = ascii_lowercase
KEY = int(input('Введите значение ключа шифрования: '))
SECRET = ''

password = input("Введите пароль: ").lower()
for symbol in password:
    index = ABC.index(symbol)
    new_index = (index + KEY) % len(ascii_lowercase)
    new_symbol = ABC[new_index]
    SECRET += new_symbol

print(SECRET)