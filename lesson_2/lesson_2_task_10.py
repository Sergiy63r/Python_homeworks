def bank():
    x = int(input('Введите сумму вклада: '))
    y = int(input('Введите срок вклада: '))
    for _ in range (y):
        interest = (x*10)/100
        x += interest
    print(int(x))


bank()