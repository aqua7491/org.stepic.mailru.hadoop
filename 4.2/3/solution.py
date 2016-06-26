import sys


def iterator():
    for line in sys.stdin:
        line = line.strip()
        if line and not line[0] == '#':
            yield line


def task(column):
    _map = {
        'id': 0,
        'user_id': 1,
        'url': 2,
    }
    if column not in _map:
        raise Exception()
    for line in iterator():
        cols = line.split('\t')
        print(cols[_map[column]])


if __name__ == '__main__':
    task('url')
