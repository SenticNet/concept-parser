#!/usr/bin/env python

'''
**************************************************************************************************************************
+ This python code contains the function of concept parsing to obtain all necessary concepts from a sentence			 +
+ Use the Input file to enter single or multiple text at once to obtain the results. File name: INPUT.txt				 +
+															 															 +					
+ This file is to be run after loading the python wrapper for StanfordCoreNLP from github. Link can be found from google +
+																														 +
+ This file parses the following:																						 +
+ nsubj, det, dep, dobj, advmod, amod, aux, nn, prep, prepc, manual, conjugator. Description alongside the function		 +
+																														 +
**************************************************************************************************************************
'''

from corenlp import *
import numpy as np
import json
import time
from nltk.stem import WordNetLemmatizer

wordnet_lemmatizer = WordNetLemmatizer()

corenlp = StanfordCoreNLP()												# StanfordCoreNLP python wrapper call

class concept_parser_v2:												# Class containing all word pair combination functions

	def __init__(self, words, postags):										# global assigner for words, postags
		self.words = words
		self.postags = postags
		self.ignore = 0
		pass

	# nsubj : nominal subject : Nominal subject is a noun phrase which is the syntactic subject of a clause
	def nsubject(self,line):	
		final_concept = []
		final_nsub = []
		pos = []
		for i in line:
			for j in range(0,len(self.words)):
				if i in self.words[j]:				
					final_nsub.append(self.words[j])
					pos.append(self.postags[j])
		if "DT" not in str(pos):										# DT check
			if "NN" in str(pos) or "JJ" in str(pos):							# NN and JJ check
				if "JJ" in str(pos):
					#print "1"
					final_concept.append(final_nsub[0] + "_" + final_nsub[1])

				if "JJ" not in str(pos):								
					if "PRP" in str(pos):
						final_concept.append(final_nsub[0])

					else:
						pass
						final_concept.append(final_nsub[1] + "_" + final_nsub[0])
				

			if "NN" not in str(pos):
				if "PRP" in str(pos):
						pass

				else:
						pass
		if "DT" in str(pos):
			final_concept.append(final_nsub[0])
				
		if not final_concept:
			pass
		else:
			#print final_concept
			return final_concept

	def prt(self,line):
		final_concept = []
		final_prt = []
		for i in line:
			for j in range(0,len(self.words)):
				if i in self.words[j]:
					final_prt.append(self.words[j])
		final_concept.append(final_prt[0] + "_" + final_prt[1])

		if not final_concept:
			pass
		else:
			#print final_concept
			return final_concept

	# det : determiner : Determiner is the relation between the head of an NP and its determiner
	def det(self,line):
		final_concept = []
		final_det = []
		pos = []
		for i in line:
			for j in range(0,len(self.words)):
				if i in self.words[j]:				
					final_det.append(self.words[j])
					pos.append(self.postags[j])

		if "DT" not in str(pos):										# DT check
			final_concept.append(final_det[1] + "_" + final_det[0])
		if "DT" in str(pos):
			final_concept.append(final_det[0])

		if not final_concept:
			pass
		else:
			#print final_concept
			return final_concept

	# dep : dependent : Dependency is labeled as dep when the system is unable to determine a more precise dependency relation between two words
	def dep(self,line):
		final_concept = []
		final_dep = []
		pos = []

		for i in line:
			for j in range(0,len(self.words)):
				if i in self.words[j]:				
					final_dep.append(self.words[j])
					pos.append(self.postags[j])

		if "DT" not in str(pos) and "JJ" in str(pos):
			final_concept.append(final_dep[1] + "_" + final_dep[0])

		if "DT" not in str(pos) and "JJ" not in str(pos):
			if "NN" in str(pos) and "VB" not in str(pos):
				final_concept.append(final_dep[0])
			else:
				final_concept.append(final_dep[0] + "_" + final_dep[1])



		if "DT" in str(pos):
			final_concept.append(final_dep[0])

		if not final_concept:
			pass
		else:
			#print final_concept
			return final_concept
				
	# dobj : direct object : Direct object of a VP is the noun phrase which is the (accusative) object of the verb
	def dobj(self,line):
		final_concept = []
		final_dobj = []

		for i in line:
			for j in range(0,len(self.words)):
				if i in self.words[j]:
					final_dobj.append(self.words[j])
		final_concept.append(final_dobj[0] + "_" + final_dobj[1])

		if not final_concept:
			pass
		else:
			#print final_concept
			return final_concept

	# acomp : adjectival complement : Adjectival complement of a verb is an adjectival phrase which functions as the complement
	def acomp(self,line):
		final_concept = []
		final_acomp = []
		for i in line:
			for j in range(0,len(self.words)):
				if i in self.words[j]:
					final_acomp.append(self.words[j])
		final_concept.append(final_acomp[0] + "_" + final_acomp[1])

		if not final_concept:
			pass
		else:
			#print final_concept
			return final_concept

	# advmod : adverbial modifier : Adverbial modifier of a word is a (non-clausal) adverb or adverbial phrase (ADVP) that serves to modify the meaning of the word
	def advmod(self,line):
		final_concept = []
		final_advmod = []
		pos = []
		for i in line:
			for j in range(0,len(self.words)):
				if i in self.words[j]:				
					final_advmod.append(self.words[j])
					pos.append(self.postags[j])
		#print pos
		if "VB" in str(pos) and "JJ" in str(pos):
			final_concept.append(final_advmod[0] + "_" + final_advmod[1])
		if "VB" in str(pos) and "JJ" not in str(pos) and "IN" in str(pos):
			final_concept.append(final_advmod[0] + "_" + final_advmod[1])
		if "VB" in str(pos) and "JJ" not in str(pos) and "IN" not in str(pos):
			final_concept.append(final_advmod[1] + "_" + final_advmod[0])
		if "VB" not in str(pos):
			final_concept.append(final_advmod[1] + "_" + final_advmod[0])

		if not final_concept:
			pass
		else:
			#print final_concept
			return final_concept

	# amod : adjectival modifier : Adjectival modifier of an NP is any adjectival phrase that serves to modify the meaning of the NP
	def amod(self,line):
		final_concept = []
		final_amod = []
		pos = []
		#print line
		for i in line:
			for j in range(0,len(self.words)):
				if i in self.words[j]:
					final_amod.append(self.words[j])
					pos.append(self.postags[j])
		if "VB" in str(pos):
			final_concept.append(final_amod[0] + "_" + final_amod[1])
		else:
			final_concept.append(final_amod[1] + "_" + final_amod[0])

		#print pos

		if not final_concept:
			pass
		else:
			#print final_concept
			return final_concept

	# aux : auxiliary : Auxiliary of a clause is a non-main verb of the clause	
	def aux(self,line):
		final_concept = []
		final_aux = []
		pos = []
		for i in line:
			for j in range(0,len(self.words)):
				if i in self.words[j]:				
					final_aux.append(self.words[j])
					pos.append(self.postags[j])
		if "TO" in pos:
			final_concept.append(final_aux[0])
		
		else:
			if "VB" in str(pos):
				#print "VB in pos"
				pass
			if "VB" not in str(pos):
				#print "VB not in pos"
				final_concept.append(final_aux[1] + "_" + final_aux[0])
		
		if not final_concept:
			pass
		else:
			#print final_concept
			return final_concept	

	# nn : noun compound modifier : Noun compound modifier of an NP is any noun that serves to modify the head noun
	def nn(self,line):
		final_concept = []
		final_nn = []
		posit_sum = []
		for i in line:
			for j in range(0,len(self.words)):
				if i in self.words[j]:
					final_nn.append(self.words[j])
					posit_sum.append(j)

		if (posit_sum[0] - posit_sum[1]) is 1:
			final_concept.append(final_nn[1] + "_" + final_nn[0])
		else:
			final_concept.append(final_nn[0] + "_" + final_nn[1])

		if not final_concept:
			pass
		else:
			#print final_concept
			return final_concept

	def neg(self,line):
		final_concept = []
		final_neg = []
		for i in line:
			for j in range(0,len(self.words)):
				if i in self.words[j]:
					final_neg.append(self.words[j])
		final_concept.append(final_neg[1] + "_" + final_neg[0])

		if not final_concept:
			pass
		else:
			#print final_concept
			return final_concept
	
	# prep : prepositional modifier : Prepositional modifier of a verb, adjective, or noun is any prepositional phrase that serves to modify the meaning of the verb, adjective, noun, or even another prepositon
	def prep(self,line):
		final_concept = []
		final_prep = []
		for i in line:
			for j in range(0,len(self.words)):
				if i in self.words[j]:
					final_prep.append(self.words[j])
		final_concept.append(final_prep[0] + "_" + final_prep[1])
		#print final_concept
		return final_concept

	def prep_(self,line):
		final_concept = []
		final_prep = []
		final_p = []
		flag = 0
		prep = line[0].split("_")[1]
		for i in line:
			for j in range(0,len(self.words)):
				if i in self.words[j]:
					final_prep.append(self.words[j])
		final_concept.append(final_prep[0] + "_" + prep + "_" + final_prep[1])

		for i in range(0,len(final_prep)):
			for j in range(0,len(self.words)):
				if final_prep[i] in self.words[j] and "NN" not in self.words[j]:
					final_p.append(final_prep[0])
					flag = 1
					break
				else:
					pass
				
		if flag is 1:
			final_prep = final_p
			final_concept.append(final_prep[0] + "_" + prep)
		if flag is 0:
			final_concept.append(final_prep[0] + "_" + prep + "_" + final_prep[1])
		
		if not final_concept:
			pass
		else:
			#print final_concept
			return final_concept
		
		'''if not final_concept:
			pass
		else:
			#print final_concept
			return final_concept'''

	# prepc : prepositional clausal modifier : prepositional clausal modifier of a verb, adjective, or noun is a clause introduced by a preposition which serves to modify the meaning of the verb, adjective, or noun
	def prepc_(self,line):
		final_concept = []
		final_prepc = []
		final_p = []
		flag = 0
		prep = line[0].split("_")[1]
		for i in line:
			for j in range(0,len(self.words)):
				if i in self.words[j]:
					final_prepc.append(self.words[j])
		for i in range(0,len(final_prepc)):
			for j in range(0,len(self.words)):
				if final_prepc[i] in self.words[j] and "NN" not in self.words[j]:
					final_p.append(final_prepc[0])
					flag = 1
					break
				else:
					pass
				
		if flag is 1:
			final_prepc = final_p
			final_concept.append(final_prepc[0] + "_" + prep)
		if flag is 0:
			final_concept.append(final_prepc[0] + "_" + prep + "_" + final_prepc[1])
		
		if not final_concept:
			pass
		else:
			#print final_concept
			return final_concept

	# This rule has been created for "TO" type postags for relation between objects
	def manual(self,words, postags):
		manual_concept = []
		for i in range(0,len(words)-1):
			pos = postags[i-1] + postags[i] + postags[i+1]
			word = words[i-1] + "_" + words[i] + "_" + words[i+1]
			if "JJTOVB" in pos or "JJTOVBD" in pos or "JJTOVBZ" in pos or "JJSTOVB" in pos or "JJSTOVBD" in pos or "JJSTOVBZ" in pos or "JJRTOVB" in pos or "JJRTOVBD" in pos or "JJRTOVBZ" in pos:
				manual_concept.append(word)
			else:
				pass

		if not manual_concept:
			pass
		else:	
			#print final_concept
			return manual_concept

	# This rule has been created for "AND" types for relation between structures of sentence
	def conjugator(self, words, postags):
		conju = ""
		final_concept = []
		flag = 0
		flag1 = 0
		for i in range(0,len(words)):
			if "and" in words[i] and "CC" in postags[i]:
				and_pos = i
				conju = words[i]
			if "or" in words[i] and "CC" in postags[i]:
				and_pos = i
				conju = words[i]

		word1 = and_pos - 1


		for i in range(and_pos, len(words)):
			if "DT" not in postags[i]:
				word2 = and_pos + (i - and_pos)

		verb = ""
		noun = ""

		for i in range(and_pos - 3,and_pos):
			if "VB" in postags[i]:
				verb = words[i]
				flag = 1
			if "NN" in postags[i]:
				noun = words[i]
				flag1 = 1
		#print "************************************************"
		#print and_pos, len(words)
		#print "words[word1]" + words[word1]
		#print "words[word2]" + words[word2]
		#print "verb" + verb
		#print "noun" + noun
		if flag1 is 1:
			for i in range(and_pos,len(words)):
				if noun is not "":
					#print "HERE"
					if words[word1] != noun and words[word2] != noun: 
						#print "Not noun"
						final_concept.append(words[word1] + "_" + noun)
						final_concept.append(words[word2] + "_" + noun)

					if words[word1] == noun:
						#print "Noun1"
						final_concept.append(words[word2] + "_" + noun)

					if words[word2] == noun:
						#print "Noun2"
						final_concept.append(words[word1] + "_" + noun)
					break
				if "between" in str(words[i]) or "over" in str(words[i]) or "with" in str(words[i]) or "on" in str(words[i]) or "to" in str(words[i]) or "of" in str(words[i]) or "into" in str(words[i]) or "in" in str(words[i]) or "at" in str(words[i]):
					word3 = i + 1
					final_concept.append(words[word1] + "_" + words[word3])
					final_concept.append(words[word2] + "_" + words[word3])	
					#flag = 1
					break
		if flag is 1:
			#print "NOT HERE"
			final_concept.append(verb + "_" + words[word1])
			final_concept.append(verb + "_" + words[word2])
			final_concept.append(words[word1] + "_" + conju + "_" + words[word2])
		#print "************************************************"
		#print final_concept
		#print "************************************************"
		if not final_concept:
			pass
		else:
			self.ignore = 1
			#print final_concept
			return final_concept

'''***************************************************************************** MAIN FUNCTION*************************************************************************************'''	

def convert(senten):
	start_time = time.time()
	count0 = 0
	#senten = "finally, for the beginner there are not enough conceptual clues on what is actually going on and it is hard to form any mental model of the underlying processes"
	#senten = "the village still exists, of course, but you can only go shopping there: the shopkeepers are only ?pictures?, not persons, and you can't move around in the shop"
	#senten = raw_input("Enter sentence:")
	senten = senten.strip()
	count0 = count0 + 1
	#print count0
	#print "\n" + senten
	#print mystr
	line = senten.split()
	l = []
	for i in line:
		l.append(wordnet_lemmatizer.lemmatize(i, pos = 'v'))
	line = l
	senten = " ".join(l)

	#print senten
	line = senten.split()
	#print line

	mystr = corenlp.parse(senten)
	'''mystr = corenlp.parse(senten)
	#print mystr
	line = senten.split()'''
	myDict = json.loads(mystr)
	dependencies = myDict['sentences'][0]['dependencies']
	words = []
	postags= []
	for text in range(0,len(myDict['sentences'][0]['words'])):									# to get the dependencies, words and postags from the parse
		words.append(myDict['sentences'][0]['words'][text][0])
		postags.append(myDict['sentences'][0]['words'][text][1]['PartOfSpeech'])
	#print dependencies																		   #Uncomment for the dependencies
	#print words                                                                                #Uncomment for the words
	#print postags																			   #Uncomment for the postags
	
	'''print len(myDict['sentences'][0]['words'])
	print len(line)
	print "******************"
	for text in range(0,len(line)):									# to get the dependencies, words and postags from the parse
		charcheck = myDict['sentences'][0]['words'][text][1]['PartOfSpeech']
		if charcheck.isalpha() is True:
			print myDict['sentences'][0]['words'][text][0]
			print myDict['sentences'][0]['words'][text][1]['PartOfSpeech']'''

	final_concepts = []
	nsubjectcon = []
	dependency = []

	to_remove = []
	new_flag = 0

	for i in range(0,len(dependencies)):								
		remove_words = []
		remove = []
		for j in range(0,len(words)):								# Direct removal of PRP without NN word pairs (except nsubj)
			if words[j] in dependencies[i][1]:
				remove_words.append(dependencies[i][1])
				remove.append(postags[j])
				continue
			if words[j] in dependencies[i][2]:
				remove_words.append(dependencies[i][2])
				remove.append(postags[j])
				continue
		if "PRP" in remove and "NN" not in remove:
			to_remove.append(dependencies[i])
		if "PRP" in remove and "NN" in remove:
			new_flag = 1
		
	if new_flag is 1:
		del dependencies[i]
		for k in range(0,len(words)):
			if "NN" in postags[k]:		
				final_concepts.append(words[k])

	remove = []
	for i in range(0,len(to_remove)):
		remove.append(to_remove[i][2] + "_" + to_remove[i][1])

	if not to_remove:
		pass
	else:
		dependency = []
		for i in dependencies:
			for j in to_remove:
				#print i,j
				if i is not j:
					#print "2"
					dependency.append(i)
					#print "No match"
				else:
					pass
					#print "Match"
		dependencies = dependency

	if len(to_remove) > 1:
		dependencies = [i for i in dependencies if dependencies.count(i) > 1]

	dependencies = reduce(lambda x, y: x + y if y[0] not in x else x, map(lambda x: [x],dependencies))			# Remove Duplicates

	concept = concept_parser_v2(words, postags)								# Class Initialization
	for i in range(0,len(dependencies)):
		if "nsubj" in dependencies[i] and "nsubjpass" not in dependencies[i]:			# <function_name> Call
			#print "nsubj"
			final_concepts.append(concept.nsubject(dependencies[i]))			# nsubj Call

		if "prt" in dependencies[i]:			# <function_name> Call
			#print "prt"
			final_concepts.append(concept.prt(dependencies[i]))

		if "det" in dependencies[i]:
			#print "det"
			final_concepts.append(concept.det(dependencies[i]))				# det Call
	
		if "dep" in dependencies[i]:
			#print "dep"
			final_concepts.append(concept.dep(dependencies[i]))				# dep Call

		if "dobj" in dependencies[i]:
			#print "dobj"
			final_concepts.append(concept.dobj(dependencies[i]))			# dobj Call

		if "acomp" in dependencies[i]:
			#print "acomp"
			final_concepts.append(concept.acomp(dependencies[i]))			# acomp Call

		#if "advmod" in dependencies[i]:
		#	final_concepts.append(concept.advmod(dependencies[i]))			# advmod Call

		if "amod" in dependencies[i]:
			#print "amod"
			final_concepts.append(concept.amod(dependencies[i]))			# amod Call	

		if "aux" in dependencies[i]:
			#print "aux"
			final_concepts.append(concept.aux(dependencies[i]))				# aux Call

		if "nn" in dependencies[i]:
			#print "nn"
			final_concepts.append(concept.nn(dependencies[i]))				# nn Call	

		if "neg" in dependencies[i]:
			#print "neg"
			final_concepts.append(concept.neg(dependencies[i]))				# neg Call	

		if "prep" in dependencies[i]:
			#print "prep"
			final_concepts.append(concept.prep(dependencies[i]))			# prep Call

		if "prep_" in dependencies[i][0]:
			#print "prep_"
			final_concepts.append(concept.prep_(dependencies[i]))			# prep_<> Call

		if "prepc_" in dependencies[i][0]:
			#print "prepc_"
			final_concepts.append(concept.prepc_(dependencies[i]))			# prepc_<> Call
		
	and_list = []

	and_occ = [x.encode('UTF8') for x in words][0]
		#print and_occ
	if and_occ=='and' or and_occ=='or':
		#print 'here'
		pass
	else:
		#print 'not here'
		for i in range(0,len(words)):
			if "and" in words[i] and "CC" in postags[i] or "or" in words[i] and "CC" in postags[i]:
				and_list = concept.conjugator(words,postags)				# conjugator Call

	if concept.ignore is 0:
		final_concepts.append(concept.manual(words,postags))				# manual Call
	else:
		pass

	#print and_list
	if not and_list:
		pass
	else:
		and_list = [x.encode('UTF8') for x in and_list]							# covert utf-8 to ascii
	#rint final_concepts
	s = []
	for i in range(0,len(final_concepts)):
		if final_concepts[i] is not None:
			s.append(final_concepts[i])

	final_concepts = s
	#rint final_concepts

	final = []
	for i in range(0,len(final_concepts)):
			final.append(final_concepts[i][0])

	final = [x.encode('UTF8') for x in final]
	if not and_list:
		pass
	else:
		final_concepts = final + list(set(and_list) - set(final))

	if not final_concepts:
		pass
	else:
		final_concepts = reduce(lambda x, y: x + y if y[0] not in x else x, map(lambda x: [x],final_concepts))			# Remove Duplicates

	final_concepts2=[]
	for i in range(0,len(final_concepts)):
		if len(final_concepts[i]) > 1:
			final_concepts2.append(final_concepts[i])

	return final_concepts	
'''
	for i in range(0,len(final_concepts)):
		if len(final_concepts[i]) > 1:
			print final_concepts[i]								# Final Concepts of current sentence
'''

