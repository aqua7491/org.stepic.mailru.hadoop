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
            stripe = {}
            for j in objs:
                if i != j:
                    stripe[j] = 1 if j not in stripe else stripe[j] + 1
            print('%s\t%s' % (i, ','.join(['%s:%s' % (k, v) for k, v in stripe.items()])))


if __name__ == '__main__':
    task()
