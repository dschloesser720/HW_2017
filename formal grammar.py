import nltk

RWR = CFG.fromstring(demo_grammar) #RWR = random_word_replacements

print (RWR) 

for RS in generate(RWR, n=5): #RS = Random_Sentence
    print(' '.join(RS))    
