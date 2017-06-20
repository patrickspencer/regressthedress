import re
from stop_words import get_stop_words
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
from wombat.models import dbsession, engine, Item
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

items = dbsession.query(Item).filter(Item.item_type == 'dresses').filter(Item.brand != 'LENDER SUBMISSION FILL IN').filter(Item.title != 'LENDER SUBMISSION FILL IN').all()

# extract just title and description
info_blobs = []
for item in items:
    info_blobs.append([item.title, item.description])

def get_first_sentence(string):
    try:
        first_sentence = re.split(r'(?<=[.:;])\s', string)[0]
    except TypeError:
        first_sentence = ''
    return first_sentence

# combine title and description
doc_set = []
for i, t in enumerate(info_blobs):
    first_sentence = get_first_sentence(t[1])
    item_title = info_blobs[i][0]
    combined = ' '.join([item_title, first_sentence])
    doc_set.append(combined.lower())

en_stop = get_stop_words('en')

# clean sentences
texts = []
for doc in doc_set:

    # tokenize document string
    tokens = tokenizer.tokenize(doc)
    
    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop]
    
    # stem tokens
    p_stemmer = PorterStemmer()
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens]

    texts.append(stemmed_tokens)

# combine list of tokens for each item
documents = []
for text in texts:
    text = ' '.join(text)
    documents.append(text)

documents.append('ava mini ')
    
# vectorize each item 'title + description'
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform(documents)

# calculate cosine similarities 
similarities = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix)

results_num = 20

# top_d is a dictionary of (index: similarity_ranking) values
top_d = {}
    
for i, s in enumerate(similarities[0]):
    # the first one will always be the actual item itself so if we want 20 items 
    # we ask for 21 hence the + 1
    if len(top_d) <= results_num:
        top_d[i] = s
    if (min(top_d.values()) < s) and (len(top_d) > results_num + 1):
       top_d[i] = s
       top_d.pop(min(top_d, key=top_d.get), None)

# the input item will always match itself perfectly so remove the item with a 
# ranking of 1
top_d = { k:v for k, v in top_d.items() if v < 1 }

print(len(top_d))

# sort the top values into a descending list
ranked_similarities = []

while len(top_d) > 0:
    ranked_similarities.append((max(top_d, key=top_d.get), max(top_d.values())))
    top_d.pop(max(top_d, key=top_d.get))
    
relevant_items = []
for i in ranked_similarities:
    relevant_items.append(items[i[0]])

print(relevant_items)
    
#prices = []
#for item in relevant_items:
    #print(item.rent_per_week)
    
