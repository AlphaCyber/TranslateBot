#!/usr/bin/python
# -*- coding: utf-8 -*-
import telebot
from telebot import types
from telebot import util
import re
import time
from time import sleep
import sys
import json
import os
import logging
import subprocess
import requests
import random
from random import randint
import base64
import urllib
from urllib import urlretrieve as dw
import urllib2
import redis
import requests as req
reload(sys)
sys.setdefaultencoding("utf-8")

TOKEN = 'Your Token Here'
bot = telebot.TeleBot(TOKEN)
sudo = 142141024
channel = "@CyberCH"
rediss = redis.StrictRedis(host='localhost', port=6379, db=0)
db = "https://api.telegram.org/bot{}/getMe?".format(TOKEN)
res = urllib.urlopen(db)
res_body = res.read()
parsed_json = json.loads(res_body.decode("utf-8"))
botid = parsed_json['result']['id']
botuser = parsed_json['result']['username']
bhash = "blocked:users:{}".format(botuser)


f = "\n \033[01;30m Bot Firstname: {} \033[0m".format(bot.get_me().first_name)
u = "\n \033[01;34m Bot Username: {} \033[0m".format(bot.get_me().username)
i = "\n \033[01;32m Bot ID: {} \033[0m".format(bot.get_me().id)
c = "\n \033[01;31m Bot Is Online Now! \033[0m"
print(f + u + i + c)

#################################################################################################################################################################################################

@bot.message_handler(commands=['bc'])
def bc(m):
    if m.from_user.id == sudo:
        text = m.text.replace('/bc ','')
        ids = rediss.smembers("members")
        for b in ids:
           try:
             bot.send_message(b, "{}".format(text))
           except:
             rediss.srem(bhash,id)

#################################################################################################################################################################################################

@bot.message_handler(commands=['start'])
def start(m):
    banlist = rediss.sismember('banlist', '{}'.format(m.from_user.id))
    if str(banlist) == 'False':
       rankch = bot.get_chat_member(channel,m.from_user.id).status
       if rankch == 'creator' or rankch == 'administrator' or rankch == 'member':
          markup = types.InlineKeyboardMarkup()
          c = types.InlineKeyboardButton("🇮🇷 فارسی 🇮🇷",callback_data='startfa')
          markup.add(c)
          b = types.InlineKeyboardButton("🇬🇧 English 🇬🇧",callback_data='starten')
          markup.add(b)
          id = m.from_user.id
          rediss.sadd('members',id)
          bot.send_message(m.chat.id, "`سلام`\n`به روبات مترجم خوش آمدید`\n`لطفا زبان خود را انتخاب کنید`\n\n*Hi*\n_Welcome To TranslateBot_\n*Please Select Your Language*", disable_notification=True, reply_markup=markup, parse_mode='Markdown')
       else:
          bot.send_message(m.chat.id, "*First Join To Bot Channel Then Try Again!*\n`ابتدا در کانال ربات عضو شوید و مجددا تلاش کنید!`\n{}".format(channel), disable_notification=True, parse_mode='Markdown')

#################################################################################################################################################################################################

@bot.message_handler(content_types=['text'])
def translate(m):
     if rediss.get("language") == "en":
        text = m.text
        rediss.hset("translate:text","{}".format(m.from_user.id),"{}".format(text))
        markup = types.InlineKeyboardMarkup()
        c = types.InlineKeyboardButton("English",callback_data='english')
        v = types.InlineKeyboardButton("Persian",callback_data='persian')
        markup.add(c,v)
        q = types.InlineKeyboardButton("French",callback_data='french')
        w = types.InlineKeyboardButton("Russian",callback_data='russian')
        markup.add(q,w)
        e = types.InlineKeyboardButton("Arabic",callback_data='arabic')
        r = types.InlineKeyboardButton("Chinese",callback_data='chinese')
        markup.add(e,r)
        t = types.InlineKeyboardButton("Japanese",callback_data='japanese')
        y = types.InlineKeyboardButton("German",callback_data='german')
        markup.add(t,y)
        u = types.InlineKeyboardButton("Spanish",callback_data='spanish')
        z = types.InlineKeyboardButton("Turkish",callback_data='turkish')
        markup.add(u,z)
        hg = types.InlineKeyboardButton("Italy",callback_data='italy')
        gh = types.InlineKeyboardButton("Romanian",callback_data='romanian')
        markup.add(hg,gh)
        jh = types.InlineKeyboardButton("Armenia",callback_data='armenia')
        kj = types.InlineKeyboardButton("Azerbaijani",callback_data='azerbaijani')
        markup.add(jh,kj)
        kjm = types.InlineKeyboardButton("Exit",callback_data='starten')
        markup.add(kjm)
        bot.send_message(m.chat.id, "*Please Select Translation Language!*", disable_notification=True, reply_markup=markup, parse_mode="Markdown")
     elif rediss.get("language") == "fa":
        text = m.text
        rediss.hset("translate:text","{}".format(m.from_user.id),"{}".format(text))
        markup = types.InlineKeyboardMarkup()
        c = types.InlineKeyboardButton("انگلیسی",callback_data='englishfa')
        v = types.InlineKeyboardButton("فارسی",callback_data='persianfa')
        markup.add(c,v)
        q = types.InlineKeyboardButton("فرانسوی",callback_data='frenchfa')
        w = types.InlineKeyboardButton("روسیه ای",callback_data='russianfa')
        markup.add(q,w)
        e = types.InlineKeyboardButton("عربی",callback_data='arabicfa')
        r = types.InlineKeyboardButton("چینی",callback_data='chinesefa')
        markup.add(e,r)
        t = types.InlineKeyboardButton("ژاپنی",callback_data='japanesefa')
        y = types.InlineKeyboardButton("آلمانی",callback_data='germanfa')
        markup.add(t,y)
        u = types.InlineKeyboardButton("اسپانیایی",callback_data='spanishfa')
        z = types.InlineKeyboardButton("ترکیه ای",callback_data='turkishfa')
        markup.add(u,z)
        hg = types.InlineKeyboardButton("ایتالیایی",callback_data='italyfa')
        gh = types.InlineKeyboardButton("رومانیایی",callback_data='romanianfa')
        markup.add(hg,gh)
        jh = types.InlineKeyboardButton("ارمنی",callback_data='armeniafa')
        kj = types.InlineKeyboardButton("آذربایجانی",callback_data='azerbaijanifa')
        markup.add(jh,kj)
        kjm = types.InlineKeyboardButton("خروج",callback_data='startfa')
        markup.add(kjm)
        bot.send_message(m.chat.id, "`لطفا زبان ترجمه را انتخاب کنید!`", disable_notification=True, reply_markup=markup, parse_mode="Markdown")

#################################################################################################################################################################################################

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
  if call.message:
     if call.data == "englishfa":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("بازگشت به منوی ترجمه",callback_data='trfa')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=en&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='`ترجمه :`\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "persianfa":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("بازگشت به منوی ترجمه",callback_data='trfa')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=fa&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='`ترجمه :`\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "frenchfa":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("بازگشت به منوی ترجمه",callback_data='trfa')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=fr&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='`ترجمه :`\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "russianfa":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("بازگشت به منوی ترجمه",callback_data='trfa')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=ru&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='`ترجمه :`\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "arabicfa":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("بازگشت به منوی ترجمه",callback_data='trfa')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=ar&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='`ترجمه :`\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "chinesefa":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("بازگشت به منوی ترجمه",callback_data='trfa')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=zh&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='`ترجمه :`\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "japanesefa":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("بازگشت به منوی ترجمه",callback_data='trfa')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=ja&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='`ترجمه :`\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message:
     if call.data == "germanfa":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("بازگشت به منوی ترجمه",callback_data='trfa')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=de&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='`ترجمه :`\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "spanishfa":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("بازگشت به منوی ترجمه",callback_data='trfa')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=es&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='`ترجمه :`\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "turkishfa":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("بازگشت به منوی ترجمه",callback_data='trfa')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=tr&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='`ترجمه :`\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "italyfa":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("بازگشت به منوی ترجمه",callback_data='trfa')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=it&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='`ترجمه :`\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "romanianfa":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("بازگشت به منوی ترجمه",callback_data='trfa')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=ro&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='`ترجمه :`\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "armeniafa":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("بازگشت به منوی ترجمه",callback_data='trfa')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=am&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='`ترجمه :`\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "azerbaijanifa":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("بازگشت به منوی ترجمه",callback_data='trfa')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=az&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='`ترجمه :`\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "english":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("Back To Translate Menu",callback_data='tren')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=en&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Translation :*\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "persian":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("Back To Translate Menu",callback_data='tren')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=fa&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Translation :*\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "french":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("Back To Translate Menu",callback_data='tren')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=fr&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Translation :*\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "russian":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("Back To Translate Menu",callback_data='tren')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=ru&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Translation :*\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "arabic":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("Back To Translate Menu",callback_data='tren')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=ar&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Translation :*\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "chinese":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("Back To Translate Menu",callback_data='tren')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=zh&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Translation :*\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "japanese":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("Back To Translate Menu",callback_data='tren')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=ja&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Translation :*\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "german":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("Back To Translate Menu",callback_data='tren')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=de&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Translation :*\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "spanish":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("Back To Translate Menu",callback_data='tren')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=es&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Translation :*\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "turkish":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("Back To Translate Menu",callback_data='tren')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=tr&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Translation :*\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "italy":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("Back To Translate Menu",callback_data='tren')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=it&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Translation :*\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "romanian":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("Back To Translate Menu",callback_data='tren')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=ro&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Translation :*\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "armenia":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("Back To Translate Menu",callback_data='tren')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=am&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Translation :*\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "azerbaijani":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("Back To Translate Menu",callback_data='tren')
       markup.add(c)
       text = rediss.hget("translate:text","{}".format(call.from_user.id))
       url ="https://translate.yandex.net/api/v1.5/tr.json/translate?key=trnsl.1.1.20160119T111342Z.fd6bf13b3590838f.6ce9d8cca4672f0ed24f649c1b502789c9f4687a&format=plain&lang=az&text={}".format(text)
       opener = urllib2.build_opener()
       f = opener.open(url)
       parsed_json = json.loads(f.read())
       textx = parsed_json["text"][0]
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='*Translation :*\n{}'.format(textx), reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "starten":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("About",callback_data='about')
       markup.add(c)
       b = types.InlineKeyboardButton("Help",callback_data='help')
       markup.add(b)
       oo = types.InlineKeyboardButton("Channel", url='https://telegram.me/CyberCH')
       markup.add(oo)
       rediss.set('language','en')
       rediss.hdel("translate:text","{}".format(call.from_user.id))
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Hi*\n_Welcome To TranslateBot_\n*Please Choose One*", reply_markup=markup, parse_mode='Markdown')
  if call.message: 
     if call.data == "startfa":
       markup = types.InlineKeyboardMarkup()
       c = types.InlineKeyboardButton("درباره روبات",callback_data='aboutfa')
       markup.add(c)
       b = types.InlineKeyboardButton("راهنما",callback_data='helpfa')
       markup.add(b)
       oo = types.InlineKeyboardButton("کانال", url='https://telegram.me/CyberCH')
       markup.add(oo)
       rediss.set('language','fa')
       rediss.hdel("translate:text","{}".format(call.from_user.id))
       bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="`سلام`\n`یه روبات مترجم خوش آمدید`\n`لطفا یک گزینه را انتخاب کنید`", reply_markup=markup, parse_mode='Markdown')
     if call.message:
        if call.data == "tren":
          markup = types.InlineKeyboardMarkup()
          c = types.InlineKeyboardButton("English",callback_data='english')
          v = types.InlineKeyboardButton("Persian",callback_data='persian')
          markup.add(c,v)
          q = types.InlineKeyboardButton("French",callback_data='french')
          w = types.InlineKeyboardButton("Russian",callback_data='russian')
          markup.add(q,w)
          e = types.InlineKeyboardButton("Arabic",callback_data='arabic')
          r = types.InlineKeyboardButton("Chinese",callback_data='chinese')
          markup.add(e,r)
          t = types.InlineKeyboardButton("Japanese",callback_data='japanese')
          y = types.InlineKeyboardButton("German",callback_data='german')
          markup.add(t,y)
          u = types.InlineKeyboardButton("Spanish",callback_data='spanish')
          z = types.InlineKeyboardButton("Turkish",callback_data='turkish')
          markup.add(u,z)
          hg = types.InlineKeyboardButton("Italy",callback_data='italy')
          gh = types.InlineKeyboardButton("Romanian",callback_data='romanian')
          markup.add(hg,gh)
          jh = types.InlineKeyboardButton("Armenia",callback_data='armenia')
          kj = types.InlineKeyboardButton("Azerbaijani",callback_data='azerbaijani')
          markup.add(jh,kj)
          kjm = types.InlineKeyboardButton("Exit",callback_data='starten')
          markup.add(kjm)
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="*Please Select Translation Language!*", reply_markup=markup, parse_mode='Markdown')
     if call.message:
        if call.data == "trfa":
          markup = types.InlineKeyboardMarkup()
          c = types.InlineKeyboardButton("انگلیسی",callback_data='englishfa')
          v = types.InlineKeyboardButton("فارسی",callback_data='persianfa')
          markup.add(c,v)
          q = types.InlineKeyboardButton("فرانسوی",callback_data='frenchfa')
          w = types.InlineKeyboardButton("روسیه ای",callback_data='russianfa')
          markup.add(q,w)
          e = types.InlineKeyboardButton("عربی",callback_data='arabicfa')
          r = types.InlineKeyboardButton("چینی",callback_data='chinesefa')
          markup.add(e,r)
          t = types.InlineKeyboardButton("ژاپنی",callback_data='japanesefa')
          y = types.InlineKeyboardButton("آلمانی",callback_data='germanfa')
          markup.add(t,y)
          u = types.InlineKeyboardButton("اسپانیایی",callback_data='spanishfa')
          z = types.InlineKeyboardButton("ترکیه ای",callback_data='turkishfa')
          markup.add(u,z)
          hg = types.InlineKeyboardButton("ایتالیایی",callback_data='italyfa')
          gh = types.InlineKeyboardButton("رومانیایی",callback_data='romanianfa')
          markup.add(hg,gh)
          jh = types.InlineKeyboardButton("ارمنی",callback_data='armeniafa')
          kj = types.InlineKeyboardButton("آذربایجانی",callback_data='azerbaijanifa')
          markup.add(jh,kj)
          kjm = types.InlineKeyboardButton("خروج",callback_data='startfa')
          markup.add(kjm)
          bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="`لطفا زبان ترجمه را انتخاب کنید!`", reply_markup=markup, parse_mode='Markdown')
     if call.message:
        if call.data == "helpfa":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="متن خود را برای ترجمه ارسال کنید")
     if call.message:
        if call.data == "help":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="Send Your Text To Translate")
     if call.message:
        if call.data == "aboutfa":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="روبات مترجم توسط @AlphaCyber ساخته شده است و به زبان پایتون نوشته شده است")
     if call.message:
        if call.data == "about":
            bot.answer_callback_query(callback_query_id=call.id, show_alert=True, text="TranslateBot Created By @AlphaCyber And Written In Python")

#################################################################################################################################################################################################

@bot.message_handler(commands=['stats'])
def stats(m):
    if m.from_user.id == sudo:
      if rediss.get("language") == "en":
        usrs = str(rediss.scard('members'))
        text = '*Users : {}*'.format(usrs)
        bot.send_message(m.chat.id,text,parse_mode='Markdown')
      elif rediss.get("language") == "fa":
        usrs = str(rediss.scard('members'))
        text = '`تعداد کاربران : {}`'.format(usrs)
        bot.send_message(m.chat.id,text,parse_mode='Markdown')

#################################################################################################################################################################################################
bot.polling(True)
#end

