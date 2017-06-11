import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer

from wombat.models import engine

# setup python nltk
custom_sent_tokenizer = PunktSentenceTokenizer()
# 
speech_parts = ['FW', 'NN', 'NNS', 'NNP', 'NNPS', 'JJ', 'FW', 'RB', 'RBR', 'RBS']
banned_words = ['gucci', 'dress', 'giannvito', 'rossi', 'cirrus', 'philip', 'jetset', 'diaries', 'gabrielle', 'nicole', 'miller', 'shift', 'right', 'minidress', 'golden', 'island']

# create a list containing all lines of the key words file so we can check to
# see if we are adding words twice
f = open('key_words.txt', 'r')
existing_words = f.read().split("\n") 
f.close() # close file

def process_sentence(text):
    # l will hold words we want to add to the key words file
    l = []
    tokenized = custom_sent_tokenizer.tokenize(text)
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            for part in tagged:
                # we don't want bad parts of speech like 'with' or 'in'
                if part[1] in speech_parts:
                    word = part[0].lower()
                    if (word not in existing_words) and (word not in l) and (word not in banned_words):
                        l.append("{}\n".format(word))

    except Exception as e:
        print(str(e))

    with open('key_words.txt', 'a') as fp:
        for word in l:
            fp.write(word)

res = engine.execute("SELECT title FROM items WHERE brand != 'LENDER SUBMISSION FILL IN' AND rent_per_week < 1000").fetchall()
for title in res[51:100]:
    process_sentence(title[0])
