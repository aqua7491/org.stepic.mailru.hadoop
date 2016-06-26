import sys, re


def iterator():
    for line in sys.stdin:
        line = line.strip()
        if line and not line[0] == '#':
            yield line


def task():
    for line in iterator():
        sep_pos = line.find(':')
        doc_id = line[:sep_pos].strip()
        text = line[sep_pos + 1:].strip()
        words = re.findall(r'\w+', text)
        for word in words:
            print('%s#%s\t%s' % (word, doc_id, 1))


if __name__ == '__main__':
    task()
