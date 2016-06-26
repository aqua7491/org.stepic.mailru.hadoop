import sys


def iterator():
    for line in sys.stdin:
        line = line.strip()
        if line and not line[0] == '#':
            yield line


def task():
    for line in iterator():
        (f, gs) = line.split('\t')
        gs = gs.strip()
        for G in gs.split(','):
            print('%s,%s\t%d' % (f, G, 1))


if __name__ == '__main__':
    task()
