import string
import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords
import re
from nltk import *
import pandas as pd

def preprocess(text):
	text = text.lower()
	tokenizer = RegexpTokenizer(r'\w+')
	tokens = tokenizer.tokenize(text)
	filtered_words = [w for w in tokens if not w in stopwords.words('english')]
	yield filtered_words

text= open("practice.txt",encoding= 'latin-1').read() #file to be parse and encoding may need to be changed
f = list(preprocess(text))
# tokens = word_tokenize(text) # breaks on words
# stemmer = PorterStemmer() #stemmer fishing fishes turn into fish

hunt = "data" #change to any keyword you need
def hunter(sent):
    sentences = sent.split('.')
    for each in sentences: 
        check = each.split(' ')
        for word in check:
            if word == hunt:
                yield each

key_sents = list(hunter(text))

bigram_measures = nltk.collocations.BigramAssocMeasures()
trigram_measures = nltk.collocations.TrigramAssocMeasures()
finder = BigramCollocationFinder.from_words(f[:][0]) #finds bigrams
scored = finder.score_ngrams(bigram_measures.raw_freq) #applies likelihood score
sorted(finder.nbest(bigram_measures.raw_freq, 20)) #finds top 20 bigrams number 20 can be adjusted
topbigram = sorted(finder.nbest(bigram_measures.raw_freq, 20)) #stores top 20 in a value

freq = nltk.FreqDist(f[:][0])
#freq = nltk.FreqDist(contents_list)
freq_count =[]
for x in freq.items():
    freq_count.append(x)
    
top_word = sorted(freq_count[:],key=lambda key: key[1],reverse=True)[:10] #sort by count
word_l = f[:][0] #stores list of tokens
