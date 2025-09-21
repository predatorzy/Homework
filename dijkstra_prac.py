import heapq
import math

SIZE = 10
BASE_SPEED = 10

speed = {
    0: 1.0,
    1: 0.75,
    2: 0.5
}


class Graph:
    def __init__(self, matrix):
        self.matrix = matrix
        self.n = len(matrix)
        self.edges = {}
        self.weights = {}
        self._build_graph()

    def _calc_time(self, a, b):
        (x1, y1), (x2, y2) = a, b
        dx, dy = abs(x1 - x2), abs(y1 - y2)

        if dx + dy == 1:
            dist = SIZE / 2

        elif dx == 1 and dy == 1:
            dist = round(math.sqrt(2) * SIZE / 2, 2)

        else:
            return float('inf')

        v_a = BASE_SPEED * speed[self.matrix[x1][y1]]
        v_b = BASE_SPEED * speed[self.matrix[x2][y2]]

        time = dist / v_a + dist / v_b
        return round(time, 2)

    def _build_graph(self):
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1),
                      (1, 1), (-1, -1), (1, -1), (-1, 1)]

        for i in range(self.n):
            for j in range(self.n):
                if self.matrix[i][j] == -1:
                    continue
                self.edges[(i, j)] = []

                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < self.n and 0 <= y < self.n and self.matrix[x][y] != -1:
                        time = self._calc_time((i, j), (x, y))
                        if time != float('inf'):
                            self.edges[(i, j)].append((x, y))
                            self.weights[((i, j), (x, y))] = time

    def get_time(self, start, end, with_path=False):
        dist = {node: float('inf') for node in self.edges}
        prev = {node: None for node in self.edges}
        dist[start] = 0
        pq = [(0, start)]

        while pq:
            current_time, u = heapq.heappop(pq)
            if u == end:
                break

            if current_time > dist[u]:
                continue

            for v in self.edges[u]:
                weight = self.weights[(u, v)]
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    prev[v] = u
                    heapq.heappush(pq, (dist[v], v))

        if with_path:
            path = self._reconstruct_path(prev, start, end)
            self.print_path(path)
        return dist[end]

    @staticmethod
    def _reconstruct_path(prev, start, end):
        path = []
        cur = end
        while cur is not None:
            path.append(cur)
            cur = prev[cur]
        path.reverse()
        return path

    @staticmethod
    def print_path(path):
        print("Путь:")
        for step in path:
            print(step, end=" -> ")
        print("конец")


matrix = [
    [0, 1, 0],
    [0, 2, 0],
    [0, 0, 0]
]

g = Graph(matrix)

t1 = g.get_time((0, 0), (2, 2))
print("Время без пути:", t1)

t2 = g.get_time((0, 0), (2, 2), with_path=True)
print("Время с путём:", t2)
