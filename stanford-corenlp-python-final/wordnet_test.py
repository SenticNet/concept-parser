from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()

senten = "finally, for the beginner there are not enough conceptual clues on what is actually going on and it is hard to form any mental model of the underlying processes"

line = senten.split()
l = []
for i in line:
	l.append(wordnet_lemmatizer.lemmatize(i, pos = 'v'))
line = l
senten = " ".join(l)

print senten

