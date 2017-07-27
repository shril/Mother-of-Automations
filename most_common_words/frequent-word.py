from nltk.corpus import stopwords
import codecs
import nltk
import sys

#input file
textFile = (open('warpeace.txt','r').read()).decode('utf-8')

#removing stopwords like 'the', 'is', 'are', etc.
default_stopwords = set(nltk.corpus.stopwords.words('english'))- set(('and', 'or', 'not'))

#some other stopwords customized choice
custom_stopwords = set(["'s","'d","'ll"])
#tokenize text by words
words = nltk.word_tokenize(textFile)
#union of all possible stopwords
all_stopwords = default_stopwords | custom_stopwords

words = [word for word in words if len(word) > 1]
#words = [word for word in words if not word.isnumeric()]
words = [word.lower() for word in words]
words = [word for word in words if word not in all_stopwords]
fdist = nltk.FreqDist(words)
#fdist


for word, frequency in fdist.most_common(10):
    print(u'{}:{}'.format(word, frequency))
