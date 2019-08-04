# word2vec-study

以下为个人学习记录，如有不对的地方，希望您不啬指出，非常感谢！

word2vec学习，利用python中gensim等构建中文词向量并测试。

# 中文语料预处理
### 环境
windows10 python3.6 powershell

### 下载语料包
采用[维基中文语料](https://dumps.wikimedia.org/zhwiki/latest/)下载如下文件名称的，带有“article”的“.xml.bz2”格式的文件。

维基自动每几天打包一份，日期不同没关系。

> zhwiki-latest-pages-articles.xml.bz2       02-Aug-2019 21:28         16350985901

### 解压 用WikiExtractor库
```powershell
WikiExtractor.py zhwiki-latest-pages-articles.xml.bz2
```
### 繁体转中文 用OpenCC库（用的短的test.txt语料，可以将下面的文件名称替换成wiki解压出的文件名称）
> opencc -i [输入文件名] -o [输出文件名称] -c [opencc的配置，去其文件名称下面找，t2s代表traditional to simplified，即繁体转简体]
```powershell
opencc -i testArticle.txt -o testArticlesimp2.txt -c E:\Wiki\python_whl\opencc-1.0.4\share\opencc\t2s.json
```
### 删除非中文的字符（英文、括号、等其他符号）（用的短的test.txt语料，可以将下面的文件名称替换成wiki中文转化后的文件名称）
```powershell
python testDeleteNotCHineseCharacters.py testArticle_simp.txt testArticle_onlyChinese.txt
```
### 分词 用jieba库（用的短的test.txt语料，可以将下面的文件名称替换成wiki保留中文后的文件名称）
```powershell
python testJiebaPartSentences.py testArticle_onlyChinese.txt testArticle_words.txt
```
### 测试截图 （用的短的test.txt语料，可以将下面的文件名称替换成wiki分词后的文件名称）
![中文词预处理执行过程](https://github.com/RelativeWang/word2vec-study/blob/master/%E4%B8%AD%E6%96%87%E8%AF%8D%E9%A2%84%E5%A4%84%E7%90%86powershell.jpg)
# 训练模型
## Word2Vec 用gensim库
### 环境
windows10 pycharm python3.6
### 过程
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

## Glove
## FastText
# 测试
一个比较困扰过我的问题

究竟怎样判断一个模型的好坏，其标准是什么？

就我的了解，应用到实际看效果是最好的，但是对我这样在学习的人来讲，还有常用的相似度测试和类比测试的方法。
### 应用到实际
### 相似度测试
### 类比测试
模型：为了方便测试，随机截取57.5 MB的维基百科中文预料，采用CBOW模型，负采样法，sample=0.001。
![]
