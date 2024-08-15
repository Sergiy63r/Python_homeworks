def is_year_leap():
    is_year_leap = input("Введите год: ")
    is_year_leap = int(is_year_leap)
    if (is_year_leap % 4 == 0):
        print("год ", is_year_leap, True)
    else:
        print("год ", is_year_leap, False)


is_year_leap()
