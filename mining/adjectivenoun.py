#!/usr/bin/env python

import sys
import nltk
from stanford_utils import Tokenizer

tokenizer = Tokenizer()

def get_word_pairs(review):
    d = {}
    tokens = tokenizer.tokenize(review.lower())
    tagged_tokens = nltk.pos_tag(tokens)
    for i,word in enumerate(tokens[:-1]):
        if tagged_tokens[i][1]=='JJ' and tagged_tokens[i+1][1].startswith("NN"):
            k = (tokens[i], tokens[i+1]) 
            d[k] = d.setdefault(k, 0) + 1
    return d

freq = {}

fp = open(sys.argv[1])
for i,line in enumerate(fp):
    d = eval(line.strip())
    review = d['text']
    bid = d['business_id']
    a = get_word_pairs(review)
    b = freq.setdefault(bid, {})
    for k,v in a.iteritems():
       b[k] = b.setdefault(k, 0) + v
    if i>2000:
        break
fp.close()

ofp = open("anfreq_per_business.json", "w")
ofp.write(repr(freq))
ofp.close()

anfreq = {}

for k,v in freq.iteritems():
    for a,b in v.iteritems():
        anfreq[a] = anfreq.setdefault(a, 0) + b

anfreq = {"%s %s"%(k[0], k[1]):v for k,v in anfreq.iteritems() if v>1}

ofp = open("anfreq.json", "w")
ofp.write(repr(anfreq))
ofp.close()

