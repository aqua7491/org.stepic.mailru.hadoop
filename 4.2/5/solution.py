import sys


def iterator():
    for line in sys.stdin:
        line = line.strip()
        if line and not line[0] == '#':
            yield line


def task():
    (key, _key, val, _val) = (None, None, None, None)
    for line in iterator():
        (_key, _val) = line.strip().split('\t')
        if key and key == _key and val != _val:
            print(key)
        key = _key
        val = _val
    if key and key == _key and val != _val:
        print(key)


if __name__ == '__main__':
    task()
