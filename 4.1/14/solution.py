import sys


def iterator():
    for line in sys.stdin:
        line = line.strip()
        if line and not line[0] == '#':
            yield line


def task():
    for line in iterator():
        objs = line.split(' ')
        for i in objs:
            for j in objs:
                if i != j:
                    print('%s,%s\t%d' % (i, j, 1))


if __name__ == '__main__':
    task()
