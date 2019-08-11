# word2vec-study
感谢老师查看，报告PPT，为方便查看，我转成了pdf放在库中了，谢谢漆老师！ (8.5.2019)

word2vec学习，利用python中gensim等构建中文词向量并测试。

以下为个人学习记录，如有不对的地方，希望您不啬指出，非常感谢！

## 目录
* [语料预处理](#中文语料预处理)
    * [环境](#环境)
    * [下载语料包](#下载语料包)
    * [解压](#解压)
    * [繁体转简体](#繁体转中文)
    * [删除非中文字符](删除非中文的字符)
    * [分词](#分词)
    * [测试截图](#测试截图)
* [训练模型](#训练模型)
    * [Word2Vec](#Word2Vec 用gensim库)
        * [环境](#环境)
        * [过程](#过程)
    * [Glove](#Glove)
    * [FastText](#FastText)
* [测试](#测试)
    * [环境](#环境)
    * [相似度测试](#相似度测试)
    * [类比测试](#类比测试)
    * [通过类比测试看一些变化](#通过类比测试看一些变化)
    * [可视化](#可视化)
        * [PCA二维](#PCA二维)
        * [PCA三维](#PCA三维)
* [参考&感谢](#参考&感谢)


## 中文语料预处理
### 环境
windows10 python3.6 powershell

### 下载语料包
采用[维基中文语料](https://dumps.wikimedia.org/zhwiki/latest/)下载如下文件名称的，带有“article”的“.xml.bz2”格式的文件。

维基自动每几天打包一份，日期不同没关系。

> zhwiki-latest-pages-articles.xml.bz2       02-Aug-2019 21:28         16350985901

### 解压 
**用WikiExtractor库**
```powershell
WikiExtractor.py zhwiki-latest-pages-articles.xml.bz2
```
### 繁体转中文 
**用OpenCC库（用的短的test.txt语料，可以将下面的文件名称替换成wiki解压出的文件名称）**
> opencc -i [输入文件名] -o [输出文件名称] -c [opencc的配置，去其文件名称下面找，t2s代表traditional to simplified，即繁体转简体]
```powershell
opencc -i testArticle.txt -o testArticlesimp2.txt -c E:\Wiki\python_whl\opencc-1.0.4\share\opencc\t2s.json
```
### 删除非中文的字符
**（英文、括号、等其他符号）（用的短的test.txt语料，可以将下面的文件名称替换成wiki中文转化后的文件名称）**
```powershell
python testDeleteNotCHineseCharacters.py testArticle_simp.txt testArticle_onlyChinese.txt
```
### 分词
**用jieba库（用的短的test.txt语料，可以将下面的文件名称替换成wiki保留中文后的文件名称）**
```powershell
python testJiebaPartSentences.py testArticle_onlyChinese.txt testArticle_words.txt
```
### 测试截图
**（用的短的test.txt语料，可以将下面的文件名称替换成wiki分词后的文件名称）**
![中文词预处理执行过程](https://github.com/RelativeWang/word2vec-study/blob/master/image/%E4%B8%AD%E6%96%87%E8%AF%8D%E9%A2%84%E5%A4%84%E7%90%86powershell.jpg)
## 训练模型
### Word2Vec 用gensim库
#### 环境
windows10 pycharm python3.6
#### 过程
```python
# word2vec_train.py
import logging
from gensim.models import word2vec

def main():
    #训练时间会比较长，铜鼓logging来预估时间，人性化一点。
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s",level=logging.INFO)
    #将词库存入
    sentences = word2vec.LineSentence("wiki_01_simp_seq.txt")
    # size：单词向量的维度，也就是特征的个数，也就是投影层的维度。其中有两个默认参数，hs=0，sg=0，下面会解释一下。
    model = word2vec.Word2Vec(sentences,size=100)
    #保存模型
    #model.save("../model/wiki_corpus.bin")
    model.save("wiki_corpus_100.model")

if __name__ == "__main__":
    main()
```
符号|代表含义|常用中文翻译
hs=1|hierachical Softmax|层次Softmax方法
sg=1|Skip-gran model|跳字模型(一般就采用英文)
hs=0|Negative Sampling|中文：负采样方法
sg=0|CBOW Continuous Bag of Words|连续词袋模型

|hs=0|hs=1
sg=0|用负采样的CBOW模型|用层次Softmax的CBOW模型
sg=1|用负采样的Skip-gram模型|用层次Softmax的Skip-gram模型

### Glove
### FastText
## 测试
一个比较困扰过我的问题

究竟怎样判断一个模型的好坏，其标准是什么？

就我的了解，应用到实际看效果是最好的，但是对我这样在学习的人来讲，很难有这样的机会。但是，自己找了一种方式，可以通过参加比赛尽可能有实际背景。但对于学习来讲，还是操作起来难度有点高，在这里，我采取了很多人在用的相似度测试和类比测试的方法。
### 环境
windows10 pycharm
### 相似度测试
```python
#test_simTest.py
from gensim.models import word2vec

model = word2vec.Word2Vec.load('wiki_corpus_100.model')
# 直观看一下词向量,输出是一个size维数的向量，代表“男人”这个词的特征。
print(model['男人'])

#测试两个词的[余弦]相似度
print(model.wv.similarity('鼠标','键盘'))

#寻找词的近似词，topn=n代表返回最相近的前n个词
result = model.most_similar("男人", topn=10)
print(model.wv.most_similar("男人", topn=10))

#找出集合中不同类型的短语
list = [u'纽约','u'北京', u'美国', u'苏州']# 这个应该输出美国
list = ['篮球', '排球', '北京']#这个应该输出北京
print(model.wv.doesnt_match(list))
```

上面的例子中的测试，其实还是远远不够的，因为一两个词的相似度，只能说自己测着玩，看看对这个词库来讲，这个词意思最近的是什么，这两个词有多“近”。

对于我来讲，我是想看看它“好坏”。没有工业的应用，我就以“我”为标准，测试一下人类对于近似词的判定，和模型得出的判定，一致还是不一致。

*我找到了一个测试集合，(近义词测试集合)[https://www.cs.york.ac.uk/semeval-2012/task4/index.html]
这是下一步的工作。*
### 类比测试
```python
#test_simTest.py
from gensim.models import word2vec

model = word2vec.Word2Vec.load('wiki_corpus_100.model')

#这个代表，国王+女人-男人=?，一个比较有名的测试，我训练得出的是“女王”。
print(model.wv.most_similar(positive=[u'国王',u'女人'],negative=[u'男人']))
```
#### 通过类比测试看一些变化
一个对比测试，结论很明显：随着维数增大，“女王”排名越来越高。但是，我觉得很有成就感，毕竟研究都是一步一步走过来，不算浪费时间。

为了快点看效果，随机截取57.5 MB的维基百科中文预料，采用CBOW模型，负采样法，sample=0.001。

![类比测试的对比测试](https://github.com/RelativeWang/word2vec-study/blob/master/image/%E7%B1%BB%E6%AF%94%E6%B5%8B%E8%AF%95%E7%9A%84%E5%AF%B9%E6%AF%94%E6%B5%8B%E8%AF%95.png)

### 可视化
#### PCA·二维
之前的结果还算直观，但是，自己当是也想看一些更直观的东西，还真有。通过PCA(Principle Component Analysis)和T-SNE(t-Distributed Stochastic Neighbor Embedding)都可以实现降维，从而更直观的看到词和词的关系，其实是词向量和词向量的关系。

*感觉上这种降维会损失信息，因为看到有相关的文章说过PCA来对ont-hot进行降维从而获取词向量，效果不如word2vec好，那么这种为了可视化的降维感觉也会损失一些信息。但是证明这个好像没什么意义。*

代码参考：[[1]](https://web.stanford.edu/class/cs224n/materials/Gensim%20word%20vector%20visualization.html)
```python
# test_pca.py
# from https://web.stanford.edu/class/cs224n/materials/Gensim%20word%20vector%20visualization.html
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
display_pca_scatterplot(model, sample = 300);
# 2 指定词进行降维
display_pca_scatterplot(model, ['男人','女人','女孩','男孩','新娘','新郎','爸爸','妈妈','女生','男生','男性','女性']);
```
对于指定词降维图表如下：

![pca降维测试](https://github.com/RelativeWang/word2vec-study/blob/master/image/pca%E9%99%8D%E7%BB%B4%E6%B5%8B%E8%AF%951.png)

测试中，我发现还不错，对于这些反义词来讲，给人的感觉上**每对词的关系应当是差不多的**，也就是说“男人”“女人”的“距离”和“男孩”“女孩”的距离差不多，因为降维降低维数，但是词之间的关系还在。出来的结果，和我一开始感觉的样子一致。

*这个地方，可以再计算一下，来更加“强”的证实我的考虑。*

![](https://github.com/RelativeWang/word2vec-study/blob/master/image/%E5%9B%BD%E5%AE%B6-%E9%A6%96%E9%83%BD%E4%BA%8C%E7%BB%B4.png)
#### PCA·三维
代码在 test_pcaTriDim.py 中。

效果如下，
![](https://github.com/RelativeWang/word2vec-study/blob/master/image/%E6%97%B6%E9%97%B4%E5%B1%9E%E6%80%A7.png)
![](https://github.com/RelativeWang/word2vec-study/blob/master/image/Figure_3_ManWoman.png)

## 参考&感谢
[1] https://web.stanford.edu/class/cs224n/materials/Gensim%20word%20vector%20visualization.html
