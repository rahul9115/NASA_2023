import pickle
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from keybert import KeyBERT
import re
import numpy as np
from keyphrase_vectorizers import KeyphraseCountVectorizer
docs=[]
# def keywords(file):
#     with open(file,"r") as f:
#         docs.append(f.read())
#     kw_model=KeyBERT()
#     keywords=kw_model.extract_keywords(docs=docs, vectorizer=KeyphraseCountVectorizer())
#     for i in keywords:
#         print(i)
    # vectorizer = Keyphra
def weightage(word,text,number_of_documents=1):
    # print(word)
    word_list = re.findall(word,text)
    number_of_times_word_appeared =len(word_list)
    tf = number_of_times_word_appeared/float(len(text))
    idf = np.log((number_of_documents)/float(number_of_times_word_appeared))
    tf_idf = tf*idf
    return number_of_times_word_appeared,tf,idf ,tf_idf    


with open("19710021280.pickle","rb") as f:
    text=pickle.load(f)
    new_text=[]
    l1=[]
    l2=[]
    l3=[]
    l4=[]
    for i in text:
        if len(i)==1:
            continue
        new_text.append(i.lower())
    for i in new_text:
        number_of_times_word_appeared,tf,idf ,tf_idf=weightage(i,' '.join(new_text))
        l1.append(number_of_times_word_appeared)
        l2.append(tf)
        l3.append(idf)
        l4.append(tf_idf)
    df=pd.DataFrame(data={"keywords":new_text})
    df['number_of_times_word_appeared'] = l1
    df['tf'] = l2
    df['idf'] = l3
    df['tf_idf'] = l4
    
    print("Types: ",type(df["keywords"].values[0]))
    
    df = df.sort_values('tf_idf',ascending=False)
    df.to_csv("tfidf.csv")
    print(df.head(25))


#keywords("EJ131877.pdf_clean.txt")
# text=' '.join(final_cleaned_data1)
# word_cloud = WordCloud(background_color="black",max_words=300,\
#                max_font_size=30,min_font_size=0.00000001,\
#                random_state=42).generate(text)
# plt.imshow(word_cloud, interpolation='bilinear')
# plt.axis("off")
# #plt.savefig("word_cloud.jpg")
# plt.show()
