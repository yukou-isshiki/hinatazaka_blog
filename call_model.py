from gensim.models import word2vec

model = word2vec.Word2Vec.load("kosakana_fun_model.model")
data = model.most_similar(positive=["小坂菜緒"])
print(data)
#print(model.corpus_count)