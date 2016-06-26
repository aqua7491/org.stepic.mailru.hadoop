import sys


def iterator():
    for line in sys.stdin:
        line = line.strip()
        if line and not line[0] == '#':
            yield line


def task():
    (site, count, sum) = (None, 0, 0)

    def _print():
        print(site + '\t' + str(int(sum / count)))

    for line in iterator():
        (_site, time) = line.split('\t')
        if site and site != _site:
            _print()
            (site, count, sum) = (_site, 1, int(time))
        else:
            (site, count, sum) = (_site, count + 1, sum + int(time))
    if site:
        _print()


if __name__ == '__main__':
    task()
