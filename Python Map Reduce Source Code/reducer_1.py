from operator import itemgetter
import sys

word_pick = None
word_count = 0
word = None

# input comes from STDIN
for entries in sys.stdin:
    # remove leading and trailing whitespace
    entries = entries.strip()

    # words and count are formed by splitting the entries
    word, count = entries.split('\t', 1)

    # parsing count to integer variable
    try:
        count = int(count)
    except ValueError:
        continue

    # Before passing the output of the map to the reducer, Hadoop sorts it by key (in this case, word).
    if word_pick == word:
        word_count += count
    else:
        if word_pick:
            # writing the result to STDOUT
            print ('%s\t%s' % (word_pick, word_count))
        word_count = count
        word_pick = word

if word_pick == word:
    print ('%s\t%s' % (word_pick, word_count))
