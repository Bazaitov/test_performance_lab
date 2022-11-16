import sys
import argparse as argp
import numpy as np


def createParser():
    parser = argp.ArgumentParser()
    parser.add_argument('-n', '--name', required=True)
    return parser


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    fData = [int(line.rstrip('\n')) for line in open(namespace.name)]
    median = round(np.percentile(fData, 50))
    print(sum(abs(i - median) for i in fData))
