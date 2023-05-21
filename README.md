## word2vec demo

### How to Use
1. Download damp file
Run src/download.sh

2. Create Plane text data
Run 'python -m wikiextractor.WikiExtractor jawiki-latest-pages-articles.xml.bz2'

3. Create Model
Run 'python createModel.py'

4. Test Model
Run 'python testModel.py'
