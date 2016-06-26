import sys


def iterator():
    for line in sys.stdin:
        line = line.strip()
        if line and not line[0] == '#':
            yield line


def task():
    _buffer = {}
    for line in iterator():
        for word in line.split(' '):
            word = word.strip()
            _buffer[word] = _buffer[word] + 1 if word in _buffer else 1
    for word, count in _buffer.items():
        print(word + '\t' + str(count))


if __name__ == '__main__':
    task()
