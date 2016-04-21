import fileinput
import json
import sys
import os
from collections import defaultdict

line = []
tw = 0

f = 'tweet.json'

word_count = defaultdict(int)

for line in fileinput.input([f]):
        line = line.strip();
        if not line: continue
        tweettext = json.loads(line).get('text')
        if not json.loads(line).get('text'):
                continue
        words = tweettext.split()
        tw += len(words)
        for word in words:
                word_count[word]+=1

print word_count
print "total number of words", tw