import sys

if __name__ == '__main__':
    input = sys.stdin.readline
    n, k = map(int, input().split())
    ranks = {}
    scores = []

    for i in range(n):
        score = list(map(int, input().split()))
        country = score[0]
        medal = score[1:4]

        scores.append([country, medal])

    scores.sort(key=lambda item: item[1], reverse=True)

    rank = 1
    for i in range(n):
        country = scores[i][0]

        if i != 0 and scores[i][1] == scores[i - 1][1]:
            ranks[country] = ranks[scores[i - 1][0]]
        else:
            ranks[country] = rank

        rank += 1

    print(ranks[k])
