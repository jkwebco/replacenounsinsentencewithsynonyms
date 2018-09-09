# -*- coding: utf-8 -*-
from thesaurus import Word

import sys
reload(sys)
sys.setdefaultencoding('utf8')


w = Word('box')

import nltk
import re

mystr = """
The agency sees its primary role as pushing forward new technological solutions to military problems, 
and the Trump administration's technical chieftains have strongly backed injecting artificial 
intelligence into more of America's weaponry as a means of competing better with Russian and Chinese military forces.

"""

mystr.decode('utf-8').strip() 

#wordList = re.sub("[^\w]", " ",  mystr).split()
#mystr.replace("'","")

# function to test if something is a noun
is_noun = lambda pos: pos[:2] == 'NN'
# do the nlp stuff
tokenized = nltk.word_tokenize(mystr)
nouns = [word for (word, pos) in nltk.pos_tag(tokenized) if is_noun(pos)] 

print nouns

for i in nouns:
	w = Word(i)
	print i
	x	= w.synonyms()
	print x[0]
	mystr = mystr.replace(i, x[0])
	print "\n"


print mystr
