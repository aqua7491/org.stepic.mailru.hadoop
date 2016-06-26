import sys


def iterator():
    for line in sys.stdin:
        line = line.strip()
        if line and not line[0] == '#':
            yield line


def task():
    (key, val, first) = (None, None, None)
    for line in iterator():
        (_key, _val) = line.strip().split('\t')
        if not first:
            first = _val
        if key and key != _key and ((_val == first and val == first) or (_val != first and val == first)):
            print(key)
        key = _key
        val = _val
    if key and _val == first and val == first:
        print(key)


if __name__ == '__main__':
    task()
