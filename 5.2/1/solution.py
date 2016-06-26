from queue import PriorityQueue
import sys


def iterator():
    for line in sys.stdin:
        line = line.strip()
        if line and not line[0] == '#':
            yield line


def storage():
    def decorate(func):
        func.storage = {}
        return func
    return decorate


@storage()
def w(_from, _to, value=None):
    if value is not None:
        if _from not in w.storage:
            w.storage[_from] = {}
        w.storage[_from][_to] = value
    elif _from == _to:
        return 0
    elif _from in w.storage and _to in w.storage[_from]:
        return w.storage[_from][_to]
    else:
        return float('inf')


def task():
    """
    Algorithm
    ~~~
    Dijkstra(V, s, w)

      V - множество вершин
      s - вершина входа
      w - множество весов

      for all vertex v in V do
        d[v] <- Inf
      d[s] <- 0
      Q <- {V}
      while Q != empty do
        u <- ExtractMin(Q)
        for all vertex v in u.AdjacencyList do
          if d[v] > d[u] + w(u, v) then
            d[v] <- d[u] + w(u, v)
    ~~~
    """
    (nodes, edges) = (None, None)
    (_from, _to) = (None, None)
    V = {}

    for line in iterator():
        elems = line.split()
        if len(elems) == 2:
            if not nodes:
                (nodes, edges) = elems
            else:
                (_from, _to) = elems
        elif len(elems) == 3:
            if elems[0] not in V:
                V[elems[0]] = set()
            if elems[1] not in V:
                V[elems[1]] = set()
            V[elems[0]].add(elems[1])
            w(elems[0], elems[1], int(elems[2]))

    d = {}
    Q = PriorityQueue()
    for v in V.keys():
        d[v] = w(_from, v)
        Q.put((d[v], v))

    while not Q.empty():
        (priority, u) = Q.get()
        for v in V[u]:
            if v in d and u in d and d[v] > d[u] + w(u, v):
                d[v] = d[u] + w(u, v)
                Q.put((d[v], v))

    print(d[_to] if _to in d and d[_to] < float('inf') else -1)

if __name__ == '__main__':
    task()
