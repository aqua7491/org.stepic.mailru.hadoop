import sys


def iterator():
    for line in sys.stdin:
        line = line.strip()
        if line and not line[0] == '#':
            yield line


def task():
    current = None
    for line in iterator():
        (val, key) = line.strip().split('\t')
        if current and current != val:
            print(current)
        current = val
    if current:
        print(current)


if __name__ == '__main__':
    task()
