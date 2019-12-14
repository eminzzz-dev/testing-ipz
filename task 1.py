from cmath import sqrt


def main():
    x = int(input("Введите x: "))
    z1 = x ** 2 + 2 * x - 3 + (x + 1) * sqrt((x ** 2) - 9)
    z2 = sqrt((x + 3) / (x - 3))
    return f"Формула z1: {z1}\nФормула z2: {z2}"


if __name__ == '__main__':
    print(main())
