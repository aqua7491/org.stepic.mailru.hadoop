import sys


def iterator():
    for line in sys.stdin:
        line = line.strip()
        if line and not line[0] == '#':
            yield line


def task():
    (last_word, _sum) = (None, 0)

    def _print():
        print(last_word + '\t' + str(_sum))

    for line in iterator():
        (word, val) = line.split('\t')
        if last_word and last_word != word:
            _print()
            (last_word, _sum) = (word, int(val))
        else:
            (last_word, _sum) = (word, _sum + int(val))
    if last_word:
        _print()


if __name__ == '__main__':
    task()
