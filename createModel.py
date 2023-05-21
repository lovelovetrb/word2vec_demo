import glob
import MeCab
import logging
import os.path
import re

import yaml
import sys

from gensim.models import word2vec

config = None

try:
    with open('config.yaml') as file:
        config = yaml.safe_load(file)
except Exception as e:
    print('Exception occurred while loading YAML...', file=sys.stderr)
    print(e, file=sys.stderr)
    sys.exit(1)


if (os.path.exists('./src/text')):
    logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
    logger = logging.getLogger(__name__)

    tagger = MeCab.Tagger("-Owakati")

    AllData = ''
    Folders = glob.glob('./src/text/*')

    for FolderName in Folders:
        files = glob.glob(f"{FolderName}/*")
        for file in files:
            f = open(file, 'r', encoding='UTF-8')
            data = f.read()
            wakatiData = tagger.parse(data)
            AllData += wakatiData + '\n'
            logger.info(file)
            wf = open(f'src/wakati/wiki_data_{FolderName[11:13]}.txt', 'w', encoding='UTF-8')
            wf.write(AllData)
            wf.close

    wf = open('src/wiki_data_wakati.txt', 'w', encoding='UTF-8')
    wf.write(AllData)
    wf.close()

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
sentences = word2vec.Text8Corpus('src/wiki_wakati_w.txt')

model = word2vec.Word2Vec(sentences, vector_size=200, min_count=20, window=15, workers=10)
model.wv.save_word2vec_format("wiki.model", binary=True)
