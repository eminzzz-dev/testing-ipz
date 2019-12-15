def main():
    digits = \
        [
            [-11, 1, 2, 3, 5, 6, 1, 3, 4, 1],
            [-5, 3, 1, 5, 7, 10, 103, -301, 4, 1],
            [-1, 1, 2, 3, 5, 6, 1, 3, 4, 1],
            [-5, 3, 1, 5, 7, 10, 103, -301, 4, 1],
            [-1, 1, 2, 3, 5, 6, 1, 3, 4, 1],
            [-5, 3, 1, 5, 7, 10, 103, -301, 4, 1],
            [-1, 1, 2, 3, 5, 6, 1, 3, 4, 1],
            [-5, 3, 1, 5, 7, 10, 103, -301, 4, 1],
            [-1, 1, 2, 3, 5, 6, 1, 3, 4, 1],
            [-5, 3, 1, 5, 7, 10, 103, -301, 4, 1],
            [-1, 1, 2, 3, 5, 6, 1, 3, 4, 1],
            [-5, 3, 1, 5, 7, 10, 103, -301, 4, 1],
            [-1, 1, 2, 3, 5, 6, 1, 3, 4, 1],
            [-5, 3, 1, 5, 7, 10, 103, -301, 4, 1],
            [-1, 1, 2, 3, 5, 6, 1, 3, 4, 1],
            [-5, 3, 1, 5, 7, 10, 103, -301, 4, 1],
            [-1, 1, 2, 3, 5, 6, 1, 3, 4, 1],
            [-5, 3, 1, 5, 7, 10, 103, -301, 4, 1],
            [-11, 1, 2, 3, 5, 6, 1, 3, 4, 1],
            [-51, 31, 1, 5, 7, 10, 103, -301, 4, 1]
        ]
    program_one(digits)
    program_two()


def program_one(digits):
    print("Програма 1:\nМасив")
    for k in digits:
        print(*k)
    with open('db/db1.txt', 'w') as f:
        for k in digits:
            f.write(str(k) + '\n')


def program_two():
    print("Програма 2:\nМасив")
    with open('db/db1.txt', 'r') as f:
        data = f.readlines()
    print(data)


if __name__ == '__main__':
    main()
