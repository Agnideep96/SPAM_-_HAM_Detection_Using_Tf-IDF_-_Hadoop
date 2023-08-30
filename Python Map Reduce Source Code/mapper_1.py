

import sys
import os
#Stop words are words that are so common they are basically ignored by typical tokenizers
stopwords= ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very', 'having', 'with', 'they', 'own', 'an', 'be',
 'some', 'for', 'do', 'its', 'yours', 'such', 'into', 'of', 'most', 'itself', 'other', 'off', 'is', 's', 'am', 'or', 'who', 'as', 'from',
 'him', 'each', 'the', 'themselves', 'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more',
 'himself', 'this', 'down', 'should', 'our', 'their', 'while', 'above', 'both', 'up', 'to', 'ours', 'had', 'she', 'all', 'no', 'when', 'at', 'any',
 'before', 'them', 'same', 'and', 'been', 'have', 'in', 'will', 'on', 'does', 'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did',
 'not', 'now', 'under', 'he', 'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few', 'whom', 't', 'being', 'if',
 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here', 'than']; 
# input comes from STDIN CLI (standard input)
for line in sys.stdin:
    filename = os.environ["map_input_file"]
    # remove starting and trailing spaces
    line = line.strip()
    # words are formed by splitting the lines
    words = line.split()
    for word in words:
        word=word.lower();
        if word not in stopwords:
            newWord=word+' '+filename;
            print ('%s\t%s' % (newWord, 1))
        # write the results to STDOUT (standard output);
        #Output of Mapper is the input of reducer
