#!/usr/bin/python3
from operator import itemgetter
import sys

current_word = None
current_count = 0
word = None

for line in sys.stdin:
    line = line.strip()# removing leading and trailing whitespace
    # print("Line:"+line)
    word,count = line.split("\t",1)
    #print("word:{0},count:{1}".format(word,count))
    try:
        count= int(count)
    except ValueError:
        continue

    if current_word==word:
        current_count += count
    else:
        if current_word:# current_word is not null
            # print('Currentword<>null,word:{0},count:{1},current_w:{2},current_c:{3}'.format(word,count,current_word,current_count))
            print('{0}\t{1}'.format(current_word,current_count))
        current_count = count
        current_word = word
if current_word==word:# used to count the last item
    print('{0}\t{1}'.format(current_word,current_count))

# which pair is to export:
