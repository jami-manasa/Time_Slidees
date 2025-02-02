from flask import Flask, render_template, request
import nltk
import numpy as np
import random
import string 
import warnings
import pandas as pd
from textblob import TextBlob
from nltk import word_tokenize, sent_tokenize
from nltk.corpus import stopwords
from nltk.stem import LancasterStemmer, WordNetLemmatizer, PorterStemmer
from wordcloud import WordCloud, STOPWORDS
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pymysql
import requests 
import json
import matplotlib.pyplot as plt

import pywhatkit as py
import datetime

app = Flask(__name__)
lan = "en"
f=open('cutm.txt','r',errors = 'ignore')
raw=f.read()
raw=raw.lower()
sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)
lemmer = nltk.stem.WordNetLemmatizer()
conn = pymysql.connect(host="127.0.0.1",user="root",passwd="12345",database="manasadb" )
cursor = conn.cursor()
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]

remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up","hey")
GREETING_RESPONSES = ["namaste","welcome to university", "how can i help you"]
def greeting(sentence,lan):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            blob =  TextBlob(random.choice(GREETING_RESPONSES))
            if( lan != "en"):
                chatbot_res=blob.translate(from_lang="en",to=lan)
                print(chatbot_res)
                return str(chatbot_res)
            else:
                return str(blob)
def response(user_response,lan):
    chatbot_response=''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx=vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if(req_tfidf==0):
        blob =  TextBlob(chatbot_response+"I am sorry! I dont understand your words")
        if( lan != "en"):
            chatbot_res=blob.translate(from_lang="en",to=lan)
            return str(chatbot_res)
        else:
            return str(blob)
    else:
        blob =  TextBlob(chatbot_response+sent_tokens[idx])
        if( lan != "en"):
            chatbot_res=blob.translate(from_lang="en",to=lan)
            return str(chatbot_res)
        else:
            return str(blob)
def chatbot_response(user_response,lan):
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you' or user_response=='thank u' ):
            return str("Thank you")
        else:
            if(greeting(user_response,lan)!=None):
                return greeting(user_response,lan)
            else:
                respons=response(user_response,lan)
                sent_tokens.remove(user_response)   
                return respons
                
    else:
        return str("Thank you")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get")

def get_bot_response():
    global lan
    print(lan)
    userText = request.args.get('msg')
    userText=userText.lower()
    print(userText)
    listlan=["telugu","hindi","oriya","english","te","hi","or","en"]
    if userText in listlan[0:4]:
        for i in range(0,4):
            if userText == listlan[i]:
                lan = listlan[i+4]
                blob= TextBlob("Thank you for choosing this language")
                if( lan != "en"):
                    chatbot_res=blob.translate(from_lang="en",to=lan)
                    return str(chatbot_res)
                else:
                    return str(blob)
    if userText=="hi":
        blob= TextBlob("I am happy to see u here")
        if( lan != "en"):
            chatbot_res=blob.translate(from_lang="en",to=lan)
            return str(chatbot_res)
        else:
            return str(blob)
        
    else:
        blob =  TextBlob(userText)
        lang=blob.detect_language()
        print(lang)
        if lang in listlan:
            if(lang!="en"):
                userText=blob.translate(from_lang=lan,to='en')
                userText=str(userText)
            else:
                gfg = TextBlob(userText) 
                # using TextBlob.correct() method 
                g = gfg.correct()
                if (gfg != g):
                    userText=str(g)
                else:
                    userText=str(userText)
                userText=str(userText)
            res = str(chatbot_response(userText,lan))
            return str(res)
        else:
            blob= TextBlob("Please enter a valid language")
            if( lan != "en"):
                chatbot_res=blob.translate(from_lang="en",to=lan)
                return str(chatbot_res)
            else:
                return str(blob)
@app.route("/results")
def results():
    regno = request.args.get('msg1')
    password = request.args.get('msg2')
    print(regno)
    login = pd.read_sql_query("select * from login",conn)
    result = pd.read_sql_query("select * from result",conn)
    if regno in login.values :
        p=login[login['username']==regno].index.values
        i=p[0]
        if login['password'].iloc[i]==password:
            if regno in result.values:
                data=result[result.regno==regno]
                data=data.reset_index(drop=True)
                data= data.rename(index={ 0 : 'RESULTS'})
                res=data.transpose()
                html = res.to_html()
                res=str(html)
                return res 
            else:
                return "NO RESULTS AVAILABLE FOR THIS REGNO."   
        else:
            return "Incorrect Password"
    else : 
        return "Invalid Username"

@app.route("/attendance")
def attendance():
    regno = request.args.get('msg1')
    password = request.args.get('msg2')
    login = pd.read_sql_query("select * from login",conn)
    result = pd.read_sql_query("select * from result",conn)
    if regno in login.values :
        p=login[login['username']==regno].index.values
        i=p[0]
        if login['password'].iloc[i]==password:
            if regno in result.values:
                data=result[result.regno==regno]
                data=data.reset_index(drop=True)
                data= data.rename(index={ 0 : 'ATTENDANCE'})
                res=data.transpose()
                html = res.to_html()
                res=str(html)
                return res 
            else:
                return "NO RESULTS AVAILABLE FOR THIS REGNO."   
        else:
            return "Incorrect Password"
    else : 
        return "Invalid Username"
@app.route("/appl")
def appl():
    name = request.args.get('app1')
    fname = request.args.get('app2')
    m1= request.args.get('app3')
    m2= request.args.get('app4')
    m3= request.args.get('app5')
    m4 = request.args.get('app6')
    m5 = request.args.get('app7')
    final="name: "+name+";"+"Father: "+fname+";"+"10th: "+m1+";"+"12th: "+m2+";"+"phno: "+m3+";"+"Branch: "+m4+";"+"EMAIL: "+m5
##    current_time = datetime.datetime.now()
##    Hour=current_time.hour  
##    Minute=current_time.minute 
##    num="+918074557609"
##    py.sendwhatmsg(num,final,Hour,Minute+2)
    return "Thank You! We will contact you shortly…"
@app.route("/mobile")
def mobile():
    mobil()
def review1():
    data = pd.read_sql_query("select * from review",conn)
    fig=data['stars'].value_counts().plot(kind='bar',color = 'darkblue')
    fig.figure.savefig('my_plot.png')
def review():
    df= pd.read_sql_query("select * from review",conn)
    df['feedback'] = df['feedback'].astype(str)
    df['feedback'] = df['feedback'].apply(lambda x: " ".join(x.lower() for x in x.split()))
    df['feedbacks'] = df['feedback'].str.replace('[^ws]','')
    stop = stopwords.words('english')
    df['feedback'] = df['feedback'].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
    st = PorterStemmer()
    df['feedbacks'] = df['feedbacks'].apply(lambda x: " ".join([st.stem(word) for word in x.split()]))
    df['feedback']
    def senti(x):
        return TextBlob(x).sentiment  
    df['senti_score'] = df['feedback'].apply(senti)
    d=df['senti_score'] 
    polarity = []
    for i in range(len(d)):
        polarity.append(d[i][0])
        
    polarity=pd.Series(polarity)
    fig1=polarity.plot.hist(grid=True, bins=20, rwidth=0.9,
                   color='#607c8e')
    plt.xlabel("RANGE")
    plt.ylabel("SCALE")
    legend=['Polarity']
    plt.legend(legend)
    plt.xticks(range(-1, 2))
    plt.yticks(range(1, 10))
    plt.title('Polarity of Feedback.')
    plt.savefig('my_plot1.png')

def mobil():
    mob=request.args.get('mob')
    print(mob)
    mobi=str(mob)
    print(mobi)
    mob=mobi[3:]
    print(mob)
    url = "https://www.fast2sms.com/dev/bulk"
    my_data = { 'sender_id': 'CUTMAP', 'message': 'Thank you for visiting Centurion Unversity Website.', 'language': 'english', 'route': 'p', 'numbers': mob} 
    headers = {'authorization': 'lfquMBPwkFVTcCJXg4eO7yI1WDH0G6UKY25Nxm3EpzjbAr9vQaN2GOSVDJ9gEF5ALdHWfkb8uYlMmZK6', 'Content-Type': "application/x-www-form-urlencoded", 'Cache-Control': "no-cache"}
    response = requests.request("POST", url, data = my_data, headers = headers)
    returned_msg = json.loads(response.text) 
    print(returned_msg['message'])
##    current_time = datetime.datetime.now()
##    Hour=current_time.hour  
##    Minute=current_time.minute 
##    num=mobi
##    py.sendwhatmsg(num,"Thank you for Visiting Our Centurion University Website.",Hour,Minute+2)
##    review()
##    review1()

if __name__ == "__main__":
    app.run()

