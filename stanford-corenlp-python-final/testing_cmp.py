import re

text = ['Tom','and','Billy','were','great','and','spirited']
pos = ['NN','CC','NN','JJ','FF','CC','EE']
aa = [n for (n, e) in enumerate(text) if e == 'and']
for i in aa:
	if "CC" in pos[i]:
		print i
