#test_simTest.py
from gensim.models import word2vec

model = word2vec.Word2Vec.load('wiki_corpus_100.model')
print(model.wv.most_similar(positive=[u'国王',u'女人'],negative=[u'男人']))