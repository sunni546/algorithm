import sys


def cal(c, s):
    x = int(c[1])

    if c[0] == 'add':
        s.add(x)
    elif c[0] == 'remove':
        s.discard(x)
    elif c[0] == 'check':
        print(int(x in s))
    elif c[0] == 'toggle':
        if x in s:
            s.remove(x)
        else:
            s.add(x)

    return s


if __name__ == '__main__':
    input = sys.stdin.readline
    m = int(input())
    s = set()

    for i in range(m):
        calculation = input().split()

        if calculation[0] == "all":
            s = set(list(range(1, 21)))
        elif calculation[0] == "empty":
            s = set()
        else:
            s = cal(calculation, s)
