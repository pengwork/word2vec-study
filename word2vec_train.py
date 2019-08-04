import logging
from gensim.models import word2vec

def main():
    logging.basicConfig(format="%(asctime)s:%(levelname)s:%(message)s",level=logging.INFO)
    sentences = word2vec.LineSentence("wiki_01_simp_seq.txt")
    # size：单词向量的维度。
    model = word2vec.Word2Vec(sentences,size=100)
    #保存模型
    #model.save("../model/wiki_corpus.bin")
    model.save("wiki_corpus_100.model")
    # model.wv.save_word2vec_format("./sogou_word2vec/min_count-1/sogou.wor2vec.txt")

if __name__ == "__main__":
    main()
