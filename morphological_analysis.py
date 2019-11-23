import MeCab
from gensim.models import word2vec
import re

def model_develop():
    bindata = open("kosakana_fan_blog_text.txt", "r").read()
    text = re.sub("\n", "", bindata)
    text = text.split("。")
    tokeData = []
    for i in range(len(text)):
        sentence_list = []
        sepalate_list = []
        try:
            before_sentence = text[i]
            m = MeCab.Tagger("")
            sentence = m.parse(before_sentence)
            word_data_list = sentence.split("\n")
            for word_data in word_data_list:
                word = word_data.split("\t")[0]
                sepalate_list.append(word)
                if (word_data.split("\t")[1].split(",")[0] == "名詞") or (word_data.split("\t")[1].split(",")[0] == "動詞") or (word_data.split("\t")[1].split(",")[0] == "形容詞"):
                    sentence_list.append(word)
                sentence_sepalate = "/".join(sepalate_list)
        except:
            print("[]")
        tokeData.append(sentence_list)
        print(before_sentence)
        print(sentence_sepalate)
    print(len(tokeData))
    model = word2vec.Word2Vec(tokeData, size=100, min_count=5, window=5, iter=3)
    model.save("kosakana_fun_model.model")

if __name__ == '__main__':
    model_develop()