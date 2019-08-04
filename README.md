# word2vec-study

word2vec学习，利用python中gensim等构建中文词向量并测试。

# 中文语料预处理

## 下载语料包

# 解压 用WikiExtractor库
```
WikiExtractor.py zhwiki-latest-pages-articles.xml.bz2
```
# 繁体转中文 用OpenCC库
```
opencc -i testArticle.txt -o testArticlesimp2.txt -c E:\Wiki\python_whl\opencc-1.0.4\share\opencc\t2s.json
```
# 删除非中文的字符（英文、括号、等其他符号）
```
python testDeleteNotCHineseCharacters.py testArticle_simp.txt testArticle_onlyChinese.txt
```
# 分词 用jieba库
```
python testJiebaPartSentences.py testArticle_onlyChinese.txt testArticle_words.txt
```
# 进行简单测试
