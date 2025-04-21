from janome.tokenizer import Tokenizer

t = Tokenizer()
text = '今日の授業では、テキストエディタでプログラムを書いて実行した。'

for token in t.tokenize(text):
    features =  token.part_of_speech.split(',')
    if features[0] == '名詞':
        print( token.surface, features) 
        
    
