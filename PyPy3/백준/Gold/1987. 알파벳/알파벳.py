import sys


def move(v, i, j, m):
    global max_move
    max_move = max(max_move, m)

    for di, dj in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
        x, y = i + di, j + dj

        if 0 <= x < R and 0 <= y < C:
            alphabet = road[x][y]

            if not v[ord(alphabet) - 65]:
                v[ord(alphabet) - 65] = True
                move(v, x, y, m + 1)
                v[ord(alphabet) - 65] = False


if __name__ == '__main__':
    input = sys.stdin.readline
    R, C = map(int, input().split())

    road = []

    for _ in range(R):
        road.append(list(input().rstrip()))

    visited = [False] * 26
    visited[ord(road[0][0]) - 65] = True

    max_move = 1
    move(visited, 0, 0, 1)

    print(max_move)
    