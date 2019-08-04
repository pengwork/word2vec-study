# word2vec-study

word2vec学习，利用python中gensim等构建中文词向量并测试。

# 中文语料预处理
### 系统
windows10 python3.6 powershell

### 下载语料包
采用[维基中文语料](https://dumps.wikimedia.org/enwiki/latest/)下载如下文件名称的，也就是带有“article”的“.xml.bz2”格式的文件。维基自动每几天打包一份，日期不同没关系。

- enwiki-latest-pages-articles.xml.bz2               02-Aug-2019 21:28         16350985901

### 解压 用WikiExtractor库
```powershell
WikiExtractor.py zhwiki-latest-pages-articles.xml.bz2
```
### 繁体转中文 用OpenCC库（用的短的test.txt语料，可以将下面的文件名称替换成wiki解压出的文件名称）
opencc -i [输入文件名] -o [输出文件名称] -c[opencc的配置，去其文件名称下面找，t2s代表traditional to simplified，即繁体转简体]
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
# 简单测试
### 类比测试
### 
