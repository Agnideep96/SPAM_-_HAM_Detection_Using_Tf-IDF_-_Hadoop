import sys
import os


# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove starting  and trailing spaces
    line = line.strip()
    # split the line into words
    fileName,count=line.split('\t',1)
    Name,rid=fileName.split(' ',1)
    idAndCount=rid+' '+count+' '+str(1)
    print ('%s\t%s' % (Name,idAndCount))
        # write the results to STDOUT (standard output);
        #  Output of Mapper is the input of reducer