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


def task():
    """
    Algorithm
    ~~~
    class Reducer
      method Reduce(nid m, [d1, ..., dk])
        dmin <- INF
        M <- empty
        for all d in counts [d1, ..., dk] do
          if IsNode(d) then
            M <- d
          else if d < dmin then
            dmin <- d
        M.Distance <- dmin
        Emit(nid m, node M)
    ~~~
    """
    cur_nid, cur_list, dmin = None, [], float('inf')
    def _print():
        _dmin = str(int(dmin)) if dmin < float('inf') else 'INF'
        print('%s\t%s\t%s' % (cur_nid, _dmin, pack_struct(cur_list)))
    for line in iterator():
        (nid, weight, _struct) = line.split('\t')
        _list = unpack_struct(_struct)
        if not cur_nid:
            cur_nid = nid

        if nid != cur_nid:
            _print()
            cur_nid = nid
            cur_list = []
            dmin = float('inf')

        if is_node(_list):
            cur_list = _list
            dmin = dmin if dmin < float(weight) else float(weight)
        elif float(weight) < dmin:
            dmin = float(weight)

    if cur_nid:
        _print()


if __name__ == '__main__':
    task()
