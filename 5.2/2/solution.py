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
    """
    Algorithm
    ~~~
    class Mapper
      method Map(key, value)
        Emit(key, value)
        for all m in value.AdjacencyList do
          Emit(m, value.d + 1)
    ~~~
    """
    for line in iterator():
        print(line)
        (nid, weight, _list_raw) = line.split('\t')
        _list = unpack_struct(_list_raw)
        for nid in _list:
            if weight == 'INF':
                _weight = weight
            else:
                _weight = str(int(weight) + 1)
            print('%s\t%s\t%s' % (nid, _weight, pack_struct([])))


if __name__ == '__main__':
    task()
