from flask import Flask,jsonify,request
from nltk.stem.porter import PorterStemmer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
import nltk
import pickle



app = Flask(__name__)

data=pickle.load(open('Ipc_code/data.pkl','rb'))
ps=PorterStemmer()
cv = CountVectorizer(max_features=5000,stop_words='english')



def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))
    return " ".join(y)


def recommend(reports,similarity):
    sections=[]
    punisment=[]
    index = data[data['Discription'] == reports].index[0]
    distances= sorted(list(enumerate(similarity[index])),reverse=True,key = lambda x: x[1])
    for i in distances[1:5]:
        sections.append(data.iloc[i[0]].Section)
        punisment.append(data.iloc[i[0]].Punishment)
    return sections,punisment
  



@app.route('/')
def home():
    report='Murder'
    report=stem(report)
    data.loc[len(data.index)] = ['1000',report,'NAN'] 
    vector=cv.fit_transform(data['Discription']).toarray()
    similarity = cosine_similarity(vector)
    Sec,pun=recommend(report,similarity)
    return pun


    



app.run(debug=True)