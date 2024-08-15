def bank():
    x = int(input('Введите сумму вклада: '))
    y = int(input('Введите срок вклада: '))
    for a in range (y):
        a = ((x*10)/100)
        x += a
    print(int(x))


bank()