# #!/usr/bin/python

# import sys
# import os

# #input: ((word, doc_id), tfidf)
# #output: (tfidf, word)
# # mapper used to sort by tfidf and find the highest 10
# for line in sys.stdin:
# 	line = line.strip()
# 	key, tfidf = line.split('\t', 1)
# 	word, doc = key.split(' ', 1)
# 	tfidf = float(tfidf)
# 	print('%10.10f\t%s' % (tfidf, word))

#!/usr/bin/env python3 

import sys
import os
from math import log10,sqrt

D=10.0
# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()
    # split the line into words
    wf,nNm=line.split('\t',1)
    n,N,m=nNm.split(' ',2)
    n=float(n)
    N=float(N)
    m=float(m)
    tfidf= (n/N)*log10(D/m)
    print ('%s\t%s' % (wf,tfidf))
