from random import randint


def min_steps_rec():
    print('rec')
    print()
    n = int(input())
    m = int(input())

    field = [[randint(0, 1) for _ in range(m)] for _ in range(n)]

    visited = [[False] * m for _ in range(n)]

    while True:
        start = (randint(0, n - 1), randint(0, m - 1))
        end = (randint(0, n - 1), randint(0, m - 1))
        if start != end and field[start[0]][start[1]] == 0 and field[end[0]][end[1]] == 0:
            break

    def find_path(x, y, steps):
        if x < 0 or x >= n or y < 0 or y >= m or field[x][y] == 1 or visited[x][y]:
            return float('inf')

        if (x, y) == end:
            return steps

        visited[x][y] = True

        up = find_path(x - 1, y, steps + 1)
        down = find_path(x + 1, y, steps + 1)
        left = find_path(x, y - 1, steps + 1)
        right = find_path(x, y + 1, steps + 1)

        visited[x][y] = False

        return min(up, down, left, right)

    res = find_path(start[0], start[1], 0)

    print()
    for row in field:
        print(*row)

    print()
    print(start)
    print(end)

    if res == float('inf'):
        print('\nпути нет\n\n')

    else:
        print(f'\nкратчайший путь: {res}\n\n')


min_steps_rec()


def min_steps_dp():
    print('dp')
    print()
    n = int(input())
    m = int(input())

    field = [[randint(0, 1) for _ in range(m)] for _ in range(n)]

    while True:
        start = (randint(0, n - 1), randint(0, m - 1))
        end = (randint(0, n - 1), randint(0, m - 1))
        if start != end and field[start[0]][start[1]] == 0 and field[end[0]][end[1]] == 0:
            break

    dp = [[float('inf')] * m for _ in range(n)]
    dp[start[0]][start[1]] = 0

    queue = [start]

    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y = queue.pop(0)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and field[nx][ny] == 0:
                if dp[nx][ny] > dp[x][y] + 1:
                    dp[nx][ny] = dp[x][y] + 1
                    queue.append((nx, ny))

    print()
    for row in field:
        print(*row)

    print()
    print(start)
    print(end)

    res = dp[end[0]][end[1]]
    if res == float('inf'):
        print('\nпути нет')

    else:
        print(f'\nкратчайший путь: {res}')


min_steps_dp()