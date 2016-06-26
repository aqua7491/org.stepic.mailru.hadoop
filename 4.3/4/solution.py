import sys


def iterator():
    for line in sys.stdin:
        line = line.strip()
        if line and not line[0] == '#':
            yield line


def task():
    for line in iterator():
        (word, doc_id, count) = line.split('\t')
        print('%s\t%s;%s;%d' % (word, doc_id, count, 1))


if __name__ == '__main__':
    task()
