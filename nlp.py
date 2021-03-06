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
	yield (filtered_words)

text= open("sps.txt",encoding= 'latin-1').read()#file path, and also encoding may be different
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
finder2 = TrigramCollocationFinder.from_words(f[:][0])
scored = finder.score_ngrams(bigram_measures.raw_freq) #applies likelihood score
sorted(finder.nbest(bigram_measures.raw_freq, 20)) #finds top 20 bigrams number 20 can be adjusted
topbigram = sorted(finder.nbest(bigram_measures.raw_freq, 20)) #stores top 20 in a value
toptrigram = sorted(finder2.nbest(trigram_measures.raw_freq, 20))
freq = nltk.FreqDist(f[:][0])
#freq = nltk.FreqDist(contents_list)
freq_count =[]
for x in freq.items():
    freq_count.append(x)
    
df = pd.DataFrame(data=freq_count,columns=['word','count'])
df.index = df.word
df.sort_values(by=['count'],ascending=False)
df2.plot('word','count', kind='bar')
df2.plot('word','count',kind='pie')
df2.plot('word','count',kind='barh')

#top_word = sorted(freq_count[:],key=lambda key: key[1],reverse=True)[:10] #sort by count
#word_l = f[:][0] #stores list of tokens
