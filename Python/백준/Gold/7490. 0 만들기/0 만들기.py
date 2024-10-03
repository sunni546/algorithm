import sys


def make_text(n, txt, k, t):
    if n == k:
        if '+' not in t and '-' not in t:
            return
        if '-' not in t:
            return
        return txt.append(t)

    make_text(n, txt, k + 1, f'{t} {k + 1}')
    make_text(n, txt, k + 1, f'{t}+{k + 1}')
    make_text(n, txt, k + 1, f'{t}-{k + 1}')


if __name__ == '__main__':
    input = sys.stdin.readline
    test = int(input())

    for _ in range(test):
        N = int(input())

        text = []
        make_text(N, text, 1, '1')

        answer = []

        for txt in text:
            result = eval(txt.replace(' ', ''))

            if result == 0:
                answer.append(txt)

        for a in answer:
            print(a)

        print()
        