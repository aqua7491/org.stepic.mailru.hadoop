import sys


def iterator():
    for line in sys.stdin:
        line = line.strip()
        if line and not line[0] == '#':
            yield line


def task():
    (cur, urls, queries) = (None, [], [])
    for line in iterator():
        (user_id, action) = line.strip().split('\t')
        (_type, val) = action.split(':')
        if cur is None:
            cur = user_id
        if cur != user_id:
            if len(urls) and len(queries):
                for query in queries:
                    for url in urls:
                        print('%s\t%s\t%s' % (cur, query, url))
            urls = []
            queries = []
        cur = user_id
        if _type == 'url':
            urls.append(val)
        else:
            queries.append(val)
    if len(urls) and len(queries):
        for query in queries:
            for url in urls:
                print('%s\t%s\t%s' % (cur, query, url))


if __name__ == '__main__':
    task()
