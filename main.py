n_ps = input("Введите пароль")
ps = input("Повторите пожалуйста пароль")

def ask_password(ps_f, n_ps_f):
    run = True
    while run:
        if ps_f == n_ps_f:
            print("Правильный пароль")
            run = False
        else:
            print("Пароль не верный")
            run = False
ask_password(ps, n_ps)