from random import randint


def robot_dp():
    print('dp')
    print()
    n = int(input())
    m = int(input())
    field = [[0] * (m + 1) for _ in range(n + 1)]

    for q in range(1, n + 1):
        for w in range(1, m + 1):
            field[q][w] = randint(10, 99)

    print()
    for row in field:
        print(*row)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 0 and j == 0:
                continue

            field[i][j] += max(field[i - 1][j], field[i][j - 1])

    print()
    print(field[-1][-1])
    print()


robot_dp()


def robot_rec():
    print()
    print('rec')
    print()
    n = int(input())
    m = int(input())

    field = [[randint(10, 99) for _ in range(m)] for _ in range(n)]

    print()
    for row in field:
        print(*row)

    def max_rec_coin(field, x, y):
        if x < 0 or y < 0:
            return 0

        if x == 0 and y == 0:
            return field[0][0]

        return max(max_rec_coin(field, x - 1, y), max_rec_coin(field, x, y - 1)) + field[x][y]

    print()
    print(max_rec_coin(field, n - 1, m - 1))


robot_rec()