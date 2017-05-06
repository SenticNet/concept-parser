from corenlp import *

corenlp = StanfordCoreNLP()		

input_file = open('//home/subh1m/stanford-corenlp-python/dataset/semantic_parsing.xml','r')		

s = input_file.read()
print s
#print s.shape

input_file.close()