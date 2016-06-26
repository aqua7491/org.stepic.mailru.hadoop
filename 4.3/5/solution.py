import sys


def iterator():
    for line in sys.stdin:
        line = line.strip()
        if line and not line[0] == '#':
            yield line


def task():
    def _buffer():
        current_word = None
        total_docs = 0
        buffer = []
        for line in iterator():
            (word, _triple) = line.split('\t')
            (doc_id, word_count, doc_count) = _triple.split(';')

            if not current_word:
                current_word = word

            if current_word == word:
                total_docs += int(doc_count)
                buffer.append((word, doc_id, word_count))
            else:
                for _tuple in buffer:
                    yield _tuple + (total_docs,)
                current_word = word
                total_docs = 1
                buffer = [(word, doc_id, word_count)]
        if len(buffer):
            for _tuple in buffer:
                yield _tuple + (total_docs,)

    for __tuple in _buffer():
        print('%s#%s\t%s\t%d' % __tuple)


if __name__ == '__main__':
    task()
