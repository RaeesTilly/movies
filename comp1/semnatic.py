import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("dog")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

tokens = nlp('dog apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# when i ran the above code we can deduce that cat and monkey are similar becase they are both animals
# ran an example of my own 'dog' and it gives the same result as 'cat'

# when i ran the example.py file in en_core_sm i got a warning 
# the warning is UserWarning: [W007] The model you're using has no word vectors loaded, so the result of the Doc.similarity method will be based on the tagger, parser and NER, which may not give useful similarity judgements. This may happen if you're using one of the small models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use context-sensitive tensors. You can always add your own word vectors, or use one of the larger models instead if available.
# from the warning we can deduce that en_core_web_md is used for bigger data vectors
     
