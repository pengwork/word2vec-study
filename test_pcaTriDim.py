import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from gensim.models import word2vec
# 用于改变字体，但是坐标轴部分还是会出现小方块
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['SimHei']
from mpl_toolkits.mplot3d import Axes3D

def display_pca_scatterplot(model, words=None, sample=0):
    if words is None:
        if sample > 0:
            words = np.random.choice(list(model.wv.vocab.keys()), sample)
        else:
            words = [word for word in model.wv.vocab]
    word_vectors = np.array([model.wv[w] for w in words])
    ax = plt.subplot(111, projection='3d')
    tridim = PCA().fit_transform(word_vectors)[:,:3]
    ax.scatter(tridim[:, 0], tridim[:, 1], tridim[:, 2])
    for word, (x, y, z) in zip(words, tridim):
        print(word)
        ax.text(x+0.5, y+0.5, z+0.5, word)

    plt.show()
#加载模型
model = word2vec.Word2Vec.load('800M\wiki_corpus_100_sg0_hs0.model');
#输出和'男人'最相关的词
print(model.wv.most_similar('男人'));

# 1 随机取300个样例数据降维
#display_pca_scatterplot(model, sample = 300);
# 2 指定词进行降维
#display_pca_scatterplot(model, ['男人','女人','女孩','男孩','新娘','新郎','爸爸','妈妈','女生','男生','男性','女性']);
#3 国家和首都指定词降维
#display_pca_scatterplot(model, ['中国','北京','美国','华盛顿','日本','东京','法国','巴黎'])
# 4 动词过去式和进行时
display_pca_scatterplot(model, ['男人','女人','女孩','男孩','新娘','新郎','爸爸','妈妈','女生','男生','男性','女性'])