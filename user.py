class User:
    def __init__(self, phone, password):
        self.phone = phone
        self.password = password


class Profile(User):
    def __init__(self, phone, password, status):
        super().__init__(phone, password)
        self.status = status


class Display:

    def __init__(self, obj):
        self.obj = obj

    def show_display(self):
        if self.obj.status:
            print(self.obj.phone, self.obj.password)
        else:
            print(self.obj.phone, self.cipher(self.obj.password))

    def cipher(self, password):

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


p1 = Profile('999', 'password', True)
p2 = Profile('888', 'password', False)

d1 = Display(p1)
d2 = Display(p2)

d1.show_display()
d2.show_display()
