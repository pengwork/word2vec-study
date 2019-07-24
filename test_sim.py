from gensim.models import word2vec

model = word2vec.Word2Vec.load('wiki_corpus_100.model')
print(model['男人'])
#用类比测试 测试所有模型
# list = ['10', '100', '200', '300', '400', '500']
# for i in list:
#     model = word2vec.Word2Vec.load('wiki_corpus_'+ i +'.model')
#     result = model.wv.most_similar(positive=[u'国王', u'女人'], negative=[u'男人'])
#     j = 0
#     for j in range(10):
#         print("%s\t%.4f" % result[j])
#     print("\n")

#测试两个词的余弦相似度
#print(model.wv.similarity('鼠标','键盘'))

#寻找词的近似词
#result = model.most_similar("男人", topn=10)
#print(model.wv.most_similar("男人", topn=10))

#找出集合中不同类型的短语
#list = [u'纽约','u'北京', u'美国', u'苏州']
#list = ['篮球', '排球', '北京']
#print(model.wv.doesnt_match(list))

#经典
#print(model.wv.most_similar(positive=[u'国王',u'女人'],negative=[u'男人']))


