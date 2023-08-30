

from operator import itemgetter
import sys

old = None
count = 1 
wordord = None
dataFrame={}
arrayFlag=[]
# input comes from STDIN
for line in sys.stdin:
    line = line.strip()
    word,rest= line.split('\t', 1)
    f,restCount = rest.split(' ',1)
    n,restCount1=restCount.split(' ',1)
    rest,c=restCount1.split(' ',1)
    if old == word:
        count = count+int(c)
    else:
        if old != None:
            q=n+' '+rest+' '+str(count)
            dataFrame[old]=q
            j=old+' '+f
            arrayFlag.append(j)
        count=1
        old = word

       
q=n+' '+N+' '+str(count)
dataFrame[old]=q
j=old+' '+f
arrayFlag.append(j)

for h in arrayFlag:
   word,f=h.split(' ',1)
   for d in dataFrame:
       if word == d:
          print ('%s\t%s' % (h,dataFrame[d]))
