import json

import requests as requests
from nltk import edit_distance
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier


with open('BOT_CONFIG.json','r', encoding='utf-8') as f:
  BOT_CONFIG=json.load(f)

X=[]
y=[]

count=0

for intent in BOT_CONFIG['intents'].keys():
  try:
    for example in BOT_CONFIG['intents'][intent]['examples']:
      X.append(example)
      y.append(intent)
  except KeyError:
    count+=1

vectorizer=CountVectorizer()
X_vectorized=vectorizer.fit_transform(X)
model=RandomForestClassifier(n_estimators=500,min_samples_split=3)
model.fit(X_vectorized,y)
import random


def clean_text(text):
  output_text = ''
  for char in text:
    if char.isalpha():
      output_text += char
  return output_text


def get_intent(input_text):
  return model.predict(vectorizer.transform([input_text]))[0]


def bot(input_text):
  intent = get_intent(input_text)  #
  return random.choice(BOT_CONFIG['intents'][intent]['responses'])
from telegram import Update
from telegram.ext import Updater #
from telegram.ext import MessageHandler, Filters
BOT_KEY='5369308043:AAF0bjhS-GO6zrXqmEm4XrvRbb4zS--ocSM'



def botReactorOnMessange(update: Update, context):
  p = open("photo.jpg", "rb")
  f = open("1.jpg", "rb")
  d = open("de.png", "rb")
  t = open("sam.jpg", "rb")
  b = open("ne.jpg", "rb")
  n = open("nepol.jpg", "rb")
  g = open("ache.jpg", "rb")
  text1=update.message.text
  print(f'[user]: {text1}')
  if(text1=="кто владеет миром"):
    update.message.reply_text("я ничего не скажу")
    update.message.reply_photo(b)
  elif (text1 == "Ты помидор"):
   update.message.reply_text("хочешь меня обидеть ничего не выйдет")
   update.message.reply_photo(n)
  elif (text1 == "Кто лучшая вайфу"):
   update.message.reply_text("Асока Тано")
   update.message.reply_photo(p)
  elif (text1 == "раскажи секрет"):
   update.message.reply_text("Хорошо только быстее.....}")
   update.message.reply_text("Пока он не пришел}")
   update.message.reply_photo(g)
  elif(text1=="Есть ли жизнь на марсе"):
    update.message.reply_text("а ты зубы чистил")
    update.message.reply_photo(f)
  elif (text1 == "ты плохой"):
    update.message.reply_text("______________________")
    update.message.reply_photo(t)
  elif (text1 == "А ты робот"):
    update.message.reply_text("Нет блин тостер")
    update.message.reply_photo(d)
  else:
    reply= bot(text1)
    print(f'[bot]: {reply}')
    update.message.reply_text(reply)
upd=Updater(BOT_KEY)
handler=MessageHandler(Filters.text, botReactorOnMessange)
upd.dispatcher.add_handler(handler)
upd.start_polling()
upd.idle()