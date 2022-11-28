import sys
import argparse as argp


def createParser():
    parser = argp.ArgumentParser()
    parser.add_argument('-n', '--number', required=True)
    parser.add_argument('-m', required=True)
    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    n = int(namespace.number)
    m = int(namespace.m)

    i = 1
    while True:
        print(i, end='')
        i = 1 + (i + m - 2) % n
        if i == 1:
            break
    print()

