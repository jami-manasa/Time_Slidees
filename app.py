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
import text2emotion as te
import matplotlib.pyplot as plt
from collections import Counter
import datetime
import resp
##import reverse_geocoder as rg 
##import geocoder

app = Flask(__name__)
lan = "en"
f=open('360.txt','r',errors = 'ignore')
raw=f.read()
raw=raw.lower()
sent_tokens = nltk.sent_tokenize(raw)
word_tokens = nltk.word_tokenize(raw)
lemmer = nltk.stem.WordNetLemmatizer()
##conn = pymysql.connect(host="127.0.0.1",user="root",passwd="",database="test" )
##cursor = conn.cursor()



##g = geocoder.ip('me') 
##o=g.latlng
##import reverse_geocoder as rg
##coordinates = (o[0],o[1])
##m=rg.search(coordinates)
##m=str(m)
##k=m[-7]
##g=m[-6]
##result=k+g
##print(result)  

def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
GREETING_INPUTS = ("hello", "hi","hellooo" ,"hiiiii","heyyyy","greetings","i am very happy","i am mad at you ", "sup", "what's up","hey")
GREETING_RESPONSES = ["Namaste","Welcome to Vsualthree60", "How can i help you!", " Glad to see you here","Hello, I am Joe.","Hello"]
def greeting(sentence,lan):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            blob =  TextBlob(random.choice(GREETING_RESPONSES))
            if( lan != "en"):
                chatbot_res=blob.translate(from_lang="en",to=lan)
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


    chatbot_res=resp.res(user_response)
    if chatbot_res==None:
        return("please contact @9********6")
                
    else:
        return str(chatbot_res)
    


    
##    if(req_tfidf==0):
##        blob =  TextBlob(chatbot_response+"I am sorry! I dont understand your words")
##        if( lan != "en"):
##            chatbot_res=blob.translate(from_lang="en",to=lan)
##            return str(chatbot_res)
##        else:
##            return str(blob)
##    else:
##        blob =  TextBlob(chatbot_response+sent_tokens[idx])
##        if( lan != "en"):
##            chatbot_res=blob.translate(from_lang="en",to=lan)
##            return str(chatbot_res)
##        else:
##            return str(blob)
def chatbot_response(user_response,lan):
    user_response=user_response.lower()
    if(user_response!='bye'):
        if(user_response=='thanks' or user_response=='thank you'  ):
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

    text=userText
    my_dict=te.get_emotion(text)
    k = Counter(my_dict) 

    high = k.most_common(1)    
    for i in high: 
        y=i[0]
        print(y)

##
##
##    sql = "INSERT INTO visual (user_type,emotion,result) VALUES (%s, %s,%s)"
##    val = ("user",str(y),str(userText))
##
##    cursor.execute(sql, val)
##
##    conn.commit()

    



    

    
    listlan=["telugu","hindi","oriya","english","te","hi","or","en"]
    if userText in listlan[0:4]:
        
        for i in range(0,4):
            if userText == listlan[i]:
                lan = listlan[i+4]
                blob= TextBlob("Thank you for choosing this language")

##                sql = "INSERT INTO visual (user_type,emotion,result) VALUES (%s, %s,%s)"
##                val = ("Bot","Happy",str(blob))
##
##                cursor.execute(sql, val)
##
##                conn.commit()

                if( lan != "en"):
                    chatbot_res=blob.translate(from_lang="en",to=lan)
                    return str(chatbot_res)
                else:
                    return str(blob)
    if userText=="hi":
        blob= TextBlob("I am happy to see u here")
        
##        sql = "INSERT INTO visual (user_type,emotion,result) VALUES (%s, %s,%s)"
##        val = ("Bot","Happy",str(blob))
##
##        cursor.execute(sql, val)
##
##        conn.commit()
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

##            
##            sql = "INSERT INTO visual (user_type,emotion,result) VALUES (%s, %s,%s)"
##            val = ("Bot","Happy",str(res))
##
##            cursor.execute(sql, val)
##
##            conn.commit()
            return str(res)
        else:
            blob= TextBlob("Please contact @9********9")
##            
##            sql = "INSERT INTO visual (user_type,emotion,result) VALUES (%s, %s,%s)"
##            val = ("Bot","Happy",str(blob))
##            cursor.execute(sql, val)
##            conn.commit()

            
            if( lan != "en"):
                chatbot_res=blob.translate(from_lang="en",to=lan)
                return str(chatbot_res)
            else:
                return str(blob)




    

        




if __name__ == "__main__":
    app.run()



    

