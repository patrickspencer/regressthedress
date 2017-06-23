# -*- coding: utf-8 -*-
"""
    parse_sentences.py
    ~~~~~~~~~~~~~~~~~~~~
    This modules extracts the adjectives from the title and description of 
"""

import re
import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
from nltk.stem.porter import PorterStemmer

from wombat.models import engine

# setup python nltk
custom_sent_tokenizer = PunktSentenceTokenizer()
# 
speech_parts = ['FW', 'NN', 'NNS', 'NNP', 'NNPS', 'JJ', 'FW', 'RB', 'RBR', 'RBS']


# create a list containing all lines of the key words file so we can check to
# see if we are adding words twice
f = open('key_words2.txt', 'r')
existing_words = f.read().split("\n") 
f.close() # close file

f = open('banned_words.txt', 'r')
banned_words = f.read().split("\n") 
f.close() # close file

print(existing_words)

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
                    p_stemmer = PorterStemmer()
                    word = p_stemmer.stem(part[0].lower())
                    if (word not in existing_words) and (word not in l) and (word not in banned_words):
                        l.append("{}\n".format(word))
                print("l is: {}".format(l))
                print("word is: {}".format(word))

    except Exception as e:
        print(str(e))

    print("l is: {}".format(l))
    with open('key_words2.txt', 'a') as fp:
        for word in l:
            fp.write(word)

def get_first_sentence(string):
    try:
        return re.split(r'(?<=[.:;])\s', string)[0]
    except TypeError:
        return ''

res = engine.execute("SELECT title, description FROM items WHERE brand != 'LENDER SUBMISSION FILL IN' AND rent_per_week < 1000").fetchall()
for text in res[0:10]:
    first_sentence = get_first_sentence(text[1])
    item_title = text[0]
    combined = ' '.join([item_title, first_sentence])
    process_sentence(combined)
# print(res[0][0])
# process_sentence2(0)
