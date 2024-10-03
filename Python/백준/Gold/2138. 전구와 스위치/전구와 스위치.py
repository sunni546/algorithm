import sys


def click_switch(light_bulbs, switch):
    for i in [-1, 0, 1]:
        s = switch + i

        if 0 <= s < N:
            light_bulbs[s] = int(not light_bulbs[s])


def check(light_bulbs, a, click_num):
    for i in range(0, N - 1):
        if light_bulbs[i] != a[i]:
            click_switch(light_bulbs, i + 1)
            click_num += 1

    if light_bulbs == a:
        return click_num
    else:
        return -1


if __name__ == '__main__':
    input = sys.stdin.readline
    N = int(input())
    before = list(map(int, input().rstrip()))
    after = list(map(int, input().rstrip()))

    not_click_first = before.copy()
    min_click = check(not_click_first, after, 0)

    if min_click == -1:
        click_switch(before, 0)
        min_click = check(before, after, 1)

    print(min_click)
