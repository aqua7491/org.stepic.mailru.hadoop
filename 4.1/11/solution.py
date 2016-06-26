import sys


def iterator():
    for line in sys.stdin:
        line = line.strip()
        if line and not line[0] == '#':
            yield line


def task():
    for line in iterator():
        # (fg, _) = line.split('\t')
        # fg = fg.strip()
        fg = line.strip()
        (f, g) = fg.split(',')
        print('%s\t%d' % (g, 1))


if __name__ == '__main__':
    task()
