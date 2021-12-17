text = open('C:/Users/zainab/Desktop/shakespeare.txt')

def split(data):
    
    return([i for item in data for i in item.split()])

words = split(text)   
    
word_count = []

word_count= set(words)

len(word_count)

for word in words:
    
    word = word.lower()
    
import pandas as pd

DF = pd.DataFrame(word_count)

DF.columns = ['words']  

word_counts = []

for i in DF['words']:
   
   word_counts.append(words.count(i))
    
DF['count'] = word_count    
    
DF = DF.sort_values('count',ascending=False)    
    
word_dict = dict(zip(DF['words'], DF['count']))    
    
word_dict    
    
    
    
