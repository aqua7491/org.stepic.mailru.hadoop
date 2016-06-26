import sys


def iterator():
    for line in sys.stdin:
        line = line.strip()
        if line and not line[0] == '#':
            yield line


def unpack_struct(_struct):
    return list(filter(lambda x: bool(x), _struct.strip('{}').split(',')))


def pack_struct(_list):
    return '{%s}' % ','.join(_list)


def task():
    for line in iterator():
        (n, p, _struct) = line.split('\t')
        _list = unpack_struct(_struct)
        page_rank = float(p) / len(_list)
        print('%s\t%0.3f\t%s' % (n, float(p), pack_struct(_list)))
        for _n in _list:
            print('%s\t%0.3f\t%s' % (_n, page_rank, pack_struct([])))


if __name__ == '__main__':
    task()
