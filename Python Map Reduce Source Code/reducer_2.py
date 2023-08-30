

from operator import itemgetter
import sys


old = None
current_count = 0
word = None
flag=0
dataframe={}
array=[]


for line in sys.stdin:
    line = line.strip()
    array.append(line)
    filename,wordcount = line.split('\t', 1)
    word,count = wordcount.split(' ', 1)
    count=int(count)
    if old == filename:
        flag=flag+count
    else:
       if old != None:
            dataframe[old]=flag
       flag=0
       old = filename
dataframe[old]=flag


for h in array:
    filename,wordcount = h.split('\t', 1)
    word,count = wordcount.split(' ', 1) 
    for k in dataframe:
        if filename == k:
           wordFile=word+' '+filename
           count_merge=count+' '+str(dataframe[k])
           print ('%s\t%s' % (wordFile,count_merge))
