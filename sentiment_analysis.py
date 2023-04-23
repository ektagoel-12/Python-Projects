import nltk
from nltk.corpus import treebank,stopwords
from nltk.tokenize import word_tokenize
import string
from collections import Counter  
import matplotlib.pyplot as plt
import pandas as pd
from nltk.sentiment.vader import SentimentIntensityAnalyzer


df=pd.read_excel('D:/minor/second/sentiment_analysis/shemirama_em.xlsx',sheet_name=0)
mylist=df['tweet_text'].tolist()
# print(mylist)

text=""
text_tweets=mylist
text=' '.join(map(str,text_tweets))
print(text)


# text=open('D:/minor/second/sentiment_analysis/read.txt',encoding='utf-8').read()
lower_case=text.lower() #Convert to lower case
cleaned_text=lower_case.translate(str.maketrans('','',string.punctuation))
# print(cleaned_text)


#TOKENIZATION- BREAKING UP THE SENTENCE
tokenized_words=word_tokenize(cleaned_text,"english")
# print(tokenized_words)

final_words=[]
for word in tokenized_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

# print(final_words)

#EMOTION ALGORTIHM
emotion_list=[]
with open("D:/minor/second/sentiment_analysis/emotions.txt",'r') as file:
    for line in file:
        clear_line=line.replace('\n','').replace(',','').replace("'",'').strip()
        word,emotion=clear_line.split(':')

        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
w=Counter(emotion_list)
print(w)

def sentiment_analysis(sentiment_text):
    sia=SentimentIntensityAnalyzer()
    score=sia.polarity_scores(sentiment_text)
    neg=score['neg']
    pos=score['pos']
    if neg>pos:
        print("Negative Sentiment")
    elif pos>neg:
        print("Positive Sentiment")
    else:
        print("Neutral emotion")

sentiment_analysis(cleaned_text)

fig,ax1=plt.subplots()
ax1.bar(w.keys(),w.values())
fig.autofmt_xdate()
plt.savefig('graph.png')
plt.show()