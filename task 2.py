from colorama import Fore

blue = Fore.BLUE
clear = Fore.RESET


def main():
    data_path = 'db/db.txt'
    print("Програма 1:")
    digits = [507, 351, 105, 420, 977, 12, 32, -79, 429, 937, 789, 810, 699, 885, 661, 538, -29, 97, 992, 839, 158, 743,
              507,
              351, 105, 420, 977, -79, 429, 937, 789, 810, 699, 885, 661, 538, -29, 97, 992, 839, 158, 743, 507, 351,
              105, 420, 977, -79, 429, 937]
    print("Масив", blue)
    print(*digits, clear)
    n = int(input("Введіть n (10 <= n <= 50): "))
    if 10 <= n <= 50:
        new_digits = []
        for i, k in enumerate(digits):
            if i == n:
                break
            new_digits.append(k)
        print("Масив", blue)
        print(*new_digits, clear)
        with open(data_path, 'w') as file:
            string = ""
            for k in new_digits:
                string += str(k) + ' '
            file.write(string)
        print(f"Масив збережено в файл {blue + data_path + clear}")
    else:
        raise Exception("Число n не підпадае під умови виконання програми!")
    print("Програма 2:")
    with open(data_path, 'r') as file:
        data = file.read()
        data = data.split()
    read_data = [int(k) for k in data]
    print("Масив", blue)
    print(*read_data, clear)
    print("Кількість елементів: " + blue + str(len(read_data)) + clear)
    minimum = []
    for k in read_data:
        if k < 0:
            minimum.append(k)
    print("Сума від’ємних: " + blue + str(sum(minimum)) + clear)
    print("Максимальний елемент: " + blue + str(max(read_data)) + clear)
    print("Мінімальний елемент: " + blue + str(min(read_data)) + clear)
    elements = read_data[read_data.index(max(read_data)) + 1: read_data.index(min(read_data))]
    print("Елементи масиву між максимальним та мінімальним:", blue, *elements, clear)
    mul = multiply(read_data[read_data.index(max(read_data)) + 1: read_data.index(min(read_data))])
    print("Добуток всіх елементів між максимальним та мінімальним:", blue, mul, clear)


def multiply(a):
    mul = 1
    for k in a:
        mul *= k
    return mul


if __name__ == '__main__':
    main()
