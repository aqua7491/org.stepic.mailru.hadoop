import sys


def iterator():
    for line in sys.stdin:
        line = line.strip()
        if line and not line[0] == '#':
            yield line


def task():
    current = None
    for line in iterator():
        (fg, count) = line.split('\t')
        if current and current != fg:
            print(current)
            current = fg
        else:
            current = fg
    if current:
        print(current)


if __name__ == '__main__':
    task()
