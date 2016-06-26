import sys


def iterator():
    for line in sys.stdin:
        line = line.strip()
        if line and not line[0] == '#':
            yield line


def task():
    fgs = {}
    gc = {}
    for line in iterator():
        (f, g) = line.split('\t')
        g = g.strip()
        if f not in fgs:
            fgs[f] = set()
        fgs[f].add(g)
    for _, gs in fgs.items():
        for g in gs:
            if g not in gc:
                gc[g] = 0
            gc[g] += 1
    for g, count in gc.items():
        print('%s\t%d' % (g, count))


if __name__ == '__main__':
    task()
