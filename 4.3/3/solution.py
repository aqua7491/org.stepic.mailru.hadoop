import sys


def iterator():
    for line in sys.stdin:
        line = line.strip()
        if line and not line[0] == '#':
            yield line


def task():
    current_doc = None
    current_word = None
    current_count = 0
    for line in iterator():
        (word_doc_id, count) = line.split('\t')
        (word, doc_id) = word_doc_id.split('#')

        if not current_doc:
            current_doc = doc_id
            current_word = word

        if current_doc == doc_id and current_word == word:
            current_count += int(count)
        else:
            print('%s\t%s\t%d' % (current_word, current_doc, current_count))
            current_doc = doc_id
            current_word = word
            current_count = 1

    if current_doc:
        print('%s\t%s\t%d' % (current_word, current_doc, current_count))


if __name__ == '__main__':
    task()
