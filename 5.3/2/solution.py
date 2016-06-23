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


def is_node(_list):
    return len(_list) > 0


def page_rank_reduce():
    (current_node, current_struct, page_rank) = (None, [], 0.0)

    def _print():
        print('%s\t%0.3f\t%s' % (current_node, page_rank, pack_struct(current_struct)))

    for line in iterator():
        (n, p, _struct) = line.split('\t')
        _list = unpack_struct(_struct)

        if not current_node:
            current_node = n

        if n != current_node:
            if not current_struct:
                current_struct = _list
            _print()
            current_node = n
            current_struct = []
            page_rank = 0.0

        if is_node(_list):
            current_struct = _list
        else:
            page_rank += float(p)

    if current_node:
        _print()


if __name__ == '__main__':
    page_rank_reduce()
