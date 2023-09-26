import pickle
import pdfplumber
import nltk
import pandas as pd
import re,nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string
import contractions
import gensim

nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("punkt")
nltk.download("stopwords")
stops=set(stopwords.words("english"))

def clean_content(sentence):
    sentence=re.sub(r'\<[^<>]*\>','',sentence)
    sentence=re.sub(r'^\W+|\W+$',' ',sentence)
    sentence=re.sub(r'\s',' ',sentence)
    sentence=re.sub(r'[^a-zA-Z0-9]',' ',sentence)
    sentence =re.sub(r'/\r?\n|\r/g',' ',sentence)
    sentence = re.sub(r's/\([^)]*\)///g',' ',sentence)
    sentence = word_tokenize(sentence)
    sentence = [i for i in sentence if i not in stops]
    return sentence
def process_sentences(cleaned_content):
    word_list=[]    
    l = nltk.stem.WordNetLemmatizer()
    des_clean=[]
    
    for word in cleaned_content:
        word=''.join([i for i in word if not i.isdigit()])
        
        
            
        if word not in string.punctuation and word.lower() not in stops:
            
            
              stem=l.lemmatize(word)
              word_list.append(str(stem))
    str1=' '.join(word_list)
    text=contractions.fix(str1)
    

    return text
# with open("output.pickle","rb") as f:
#     data=pickle.load(f)
# for i,j in data.items():
#     pd.DataFrame()
final_conclusion_summary={}
def text_rank_conclusion_summary(id,final_cleaned_data1):
    
    
    extracted_text = '. '.join(final_cleaned_data1)
    def textrank(corpus, ratio=0.2):    
        if type(corpus) is str:        
            corpus = [corpus]    
            lst_summaries = [gensim.summarization.summarize(txt,  
                            ratio=ratio) for txt in corpus]    
        return lst_summaries
    val=textrank(extracted_text)
    print(len(val[0].split(".")))
    summary=str(val[0])

    with open(f"{id}_conclusion.txt","w") as f:
        f.write(str(summary))
    with open(f"{id}_conclusion.txt","r") as f:
        l=[]
        d={}
        
        for i in f.readlines():
            d[i]=d.get(i,0)+1
        final_summary=' '.join(d.keys())

    final_conclusion_summary.update({id:final_summary})

with pdfplumber.open(f'C:\\Users\\sudha\\Downloads\\NASA Space Apps Challenge\\pdf\\19710021280.pdf') as pdf:
        l=len(pdf.pages)  
        print(l)
        text=[]
        word_count=0
        for i in range(l):
            extracted_page =pdf.pages[i] 
            extracted_text = extracted_page.extract_text()
            
            
            text.append(extracted_text)
        extracted_text='. '.join(text)
        final_cleaned_data2=[]
        words_list=[]
        id="19710021280"
        for sentence in extracted_text.split("."):
            
            sentence=clean_content(sentence)
        
            sentence=process_sentences(sentence)
            
            final_cleaned_data2.append(sentence)
            with open(f"{id}_clean.txt","w") as f:
                f.write(". ".join(final_cleaned_data2))
        



