import sys


def iterator():
    for line in sys.stdin:
        line = line.strip()
        if line and not line[0] == '#':
            yield line


def task(user_id):
    for line in iterator():
        (_, _user_id, _) = line.split('\t')
        if user_id == _user_id:
            print(line)


if __name__ == '__main__':
    task('user10')
