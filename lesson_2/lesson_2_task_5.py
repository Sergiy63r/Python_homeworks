def month_to_season():
    n = int(input("Введите номер месяца: "))
    if (n == 3) or (n == 4) or (n == 5):
        print("Весна")
    elif (n == 6) or (n == 7) or (n == 8):
        print("Лето")
    elif (n == 9) or (n == 10) or (n == 11):
        print("Осень")
    elif (n == 12) or (n ==1) or (n == 2):
        print("Зима")


month_to_season()
