#!/usr/bin/python

import sys

# #input: ((word, doc_id), 1)
# #output: (doc_id, (word, 1))
# for line in sys.stdin:
# 	line = line.strip()
# 	key, count = line.split('\t', 1)
# 	word, doc = key.split(' ', 1)
# 	value = str(word) + ' ' + str(count)
# 	print('%s\t%s' % (str(doc), value)) 

#!/usr/bin/env python3 

import sys


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    wordfilename,count=line.split('\t',1)
    word,filename=wordfilename.split(' ',1)
    z=word+' '+count;
    print ('%s\t%s' % (filename, z))
        # write the results to STDOUT (standard output);
        # what we output here will be the input for the
        # Reduce step, i.e. the input for reducer.py
        #
        # tab-delimited; the trivial word count is 1

