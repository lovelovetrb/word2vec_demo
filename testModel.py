from gensim.models import KeyedVectors

wv = KeyedVectors.load_word2vec_format('./wiki_data.model', binary=True)
results = wv.most_similar(positive=input('単語を入力\n>>> '))
for result in results:
  print(result)
