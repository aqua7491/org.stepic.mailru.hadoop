import sys


def iterator():
    for line in sys.stdin:
        line = line.strip()
        if line and not line[0] == '#':
            yield line


def task():
    (key, cur, cap) = (None, None, 0)
    for line in iterator():
        (_key, val) = line.strip().split('\t')
        if cur is None:
            cur = _key

        if key and cur != _key:
            if cap < 2:
                print(key)
            cur = _key
            cap = 1
        else:
            cap += 1

        key = _key
    if key and cap < 2:
        print(key)


if __name__ == '__main__':
    task()
