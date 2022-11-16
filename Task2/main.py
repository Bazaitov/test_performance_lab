import sys
import argparse as argp


def createParser():
    parser = argp.ArgumentParser()
    parser.add_argument('-c', '--circle', required=True)
    parser.add_argument('-p', '--points', required=True)
    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    cData = [line.rstrip('\n') for line in open(namespace.circle)]
    pData = [line.rstrip('\n') for line in open(namespace.points)]

    cData[0] = cData[0].split()
    cData[0] = list(map(float, cData[0]))
    cData[1] = list(map(float, cData[1]))

    for i in range(len(pData)):
        pData[i] = pData[i].split()
        pData[i] = list(map(float, pData[i]))
        if (cData[0][0] - pData[i][0]) ** 2 + (cData[0][1] - pData[i][1]) ** 2 == cData[1][0] ** 2:
            pData[i] = 0
        elif (1 - pData[i][0]) ** 2 + (1 - pData[i][1]) ** 2 < 25:
            pData[i] = 1
        else:
            pData[i] = 2
    print(pData)
