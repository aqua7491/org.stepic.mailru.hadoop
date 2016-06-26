import sys


def iterator():
    for line in sys.stdin:
        line = line.strip()
        if line and not line[0] == '#':
            yield line


def task():
    for line in iterator():
        for word in line.split(' '):
            print(word.strip() + '\t1')


if __name__ == '__main__':
    task()
