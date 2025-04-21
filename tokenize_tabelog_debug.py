import numpy as np
import pandas as pd
import codecs
from janome.tokenizer import Tokenizer


def split2words(hinsi,text):

    t = Tokenizer()
    words=''
    for token in t.tokenize(text):
        features =  token.part_of_speech.split(',')
        if features[0] == hinshi:
            words+=token.surface+','
    return words
            

tabelog_df = pd.read_csv('tabelog.csv', encoding='ms932', sep=',',skiprows=0)    

kuchikomi2words=[]
for kuchikomi in tabelog_df('text'):

    words = split2words('名詞',kuchikomi)
    print(words)
    kuchikomi2words.append(words)

kuchikomi_df = pd.DataFrame(kuchikomi2words,columns=['kuchikomi words'])
tabelog_withTokens = pd.concat([tabelog_df,kuchikomi_df], axis =1)

with codecs.open("tabelog_withTokens.csv", "w", "ms932", "ignore") as f: 
    #header=Trueで、見出しを書き出す
    tabelog_withTokens.to_csv(f, index=False, encoding="ms932", mode='w', header=True)

