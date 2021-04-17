"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
"""

users = ['wolf75', 'tiger78', 'owl45', 'bear35', 'dog25']
user_password = {'wolf75': '123asd',
                 'tiger78': '123qwe',
                 'owl45': '890qwe',
                 'bear35': '768asd',
                 'dog25': '567qwe'}
user_status = {'wolf75': True,
               'tiger78': False,
               'owl45': True,
               'bear35': False,
               'dog25': True}

def access_users_1(): # Сложность:O(n^2)-Квадратичная.
    while True:
        user = input("Enter the user name: ")
        password = input("Enter your password: ")
        if user in users:
            if password == user_password.get(user) and user_status.get(user) == True:
                print(f'Welcome {user}, access allowed!')
            elif password == user_password.get(user) and user_status.get(user) == False:
                print(f'{user} access denied, your account is not activated!')
            elif password != user_password.get(user):
                print("Invalid password!")
        else:
            print("A user with this name does not exist!")

access_users_1()
#
def access_users_2(user, password): # Сложность:O(1)-Константная. Данное решение более эффективное т.к. менее сложное по 0-нотации.
    if user in users:
        if password == user_password.get(user) and user_status.get(user) == True:
            print(f'Welcome {user}, access allowed!')
        elif password == user_password.get(user) and user_status.get(user) == False:
            print(f'{user} access denied, your account is not activated!')
        elif password != user_password.get(user):
            print("Invalid password!")
    else:
        print("A user with this name does not exist!")

access_users_2('wolf75','123asd')

def access_users_3(user, password): # Сложность:O(n)-Линейная.
    for name in users:
        if user == name:
            if password == user_password.get(user) and user_status.get(user) == True:
                print(f'Welcome {user}, access allowed!')
            elif password == user_password.get(user) and user_status.get(user) == False:
                print(f'{user} access denied, your account is not activated!')
            elif password != user_password.get(user):
                print("Invalid password!")
            else:
                print("A user with this name does not exist!")

access_users_3('owl45','890qwe')