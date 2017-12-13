
"""wcount.py: count words from an Internet file.

__author__ = "Wangyan"
__pkuid__  = "1700011794"
__email__  = "wangyan2333@pku.edu.cn"
"""

import sys
from urllib.request import urlopen

def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """

    import string
    import re

    b=lines
    b=b.lower()
    c=''
    d=[]
    e=[]
    for i in b:
        if i.isalpha():
            c=c+i
        else:
            c=c+' '
    c=c.split()
    for i in c:
        if i in d:
            e[d.index(i)]=e[d.index(i)]+1
        else:
            e.append(1)
            d.append(i)
    for m in range(topn):
        x=e.index(max(e))
        print(d[x],e[x])
        del d[x]
        del e[x]
    pass

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)

    try:
        topn = 10
        if len(sys.argv) == 3:
            topn = int(sys.argv[2])
    except ValueError:
        print('{} is not a valid topn int number'.format(sys.argv[2]))
        sys.exit(1)

    try:
        with urlopen(sys.argv[1]) as f:
            contents = f.read()
            lines   = contents.decode()
            wcount(lines, topn)
    except Exception as err:
        print(err)
        sys.exit(1)
