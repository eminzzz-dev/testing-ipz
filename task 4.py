def main():
    a = int(input("Введите a: "))
    if a == 1:
        raise ValueError("Ошибка!")
    b = int(input("Введите b: "))
    ran = [k for k in range(a, b + 1)]
    for k in ran:
        hip = (k ** 2 + 1) % (k ** 2 - 1) == 0
        if hip:
            print("Работает!", k)
        print("Не работает!", k)


if __name__ == '__main__':
    main()
