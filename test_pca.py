#from https://web.stanford.edu/class/cs224n/materials/Gensim%20word%20vector%20visualization.html
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from gensim.models import word2vec
# 用于改变字体，但是坐标轴部分还是会出现小方块
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']

def display_pca_scatterplot(model, words=None, sample=0):
    if words is None:
        if sample > 0:
            words = np.random.choice(list(model.wv.vocab.keys()), sample)
        else:
            words = [word for word in model.wv.vocab]

    word_vectors = np.array([model.wv[w] for w in words])
    #降维至二维
    twodim = PCA().fit_transform(word_vectors)[:, :2]

    plt.figure(figsize=(6, 6))
    plt.scatter(twodim[:, 0], twodim[:, 1], edgecolors='k', c='r')
    for word, (x, y) in zip(words, twodim):
        print(word)
        plt.text(x + 0.05, y + 0.05, word)
    plt.show()
model = word2vec.Word2Vec.load('800M\wiki_corpus_100_sg0_hs0.model');

print(model.wv.most_similar('男人'));

# 1 随机取300个样例数据降维
#display_pca_scatterplot(model, sample = 300);
# 2 指定词进行降维
display_pca_scatterplot(model, ['男人','女人','女孩','男孩','新娘','新郎','爸爸','妈妈','女生','男生','男性','女性']);
