import telebot
import requests
import json
from telebot import types


from requests.auth import HTTPDigestAuth
#import bs4 as BS
from bs4 import BeautifulSoup
t = 0
r = requests.get('http://192.168.1.23/cgi-bin/minerStatus.cgi', auth=HTTPDigestAuth('root', 'root'))
soup = BeautifulSoup (r.text, 'lxml')
soup_2 = BeautifulSoup (r.text, 'html.parser')
list_tag = soup.find_all('td', class_='cbi-value-field')


bot = telebot.TeleBot("5294703958:AAG1-Ggk4-C2qaa99PiPiN0fraj5rlK7QlE", parse_mode=None)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
	
#@bot.message_handler(func=lambda m: True)
#ef echo_all(message):
#	bot.reply_to(message, message.text)
	
	
@bot.message_handler(commands=['a'])
def send_welcome(message):
	bot.reply_to(message, i())
	
	
	
@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Кнопка")
    markup.add(item1)
    bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
    
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Кнопка":
        bot.send_message(message.chat.id, i())
  
	
def i():
    a = list_tag[127].text.strip()
    b = list_tag[118].text.strip()
    return (a,b)
def info():
    r = requests.get('http://192.168.1.23/cgi-bin/minerStatus.cgi', auth=HTTPDigestAuth('root', 'root'))
    soup = BeautifulSoup (r.text, 'lxml')
    list_tag = soup.find_all('td', class_='cbi-value-field')
    
   # r_config = requests.get('http://192.168.1.23/cgi-bin/minerConfiguration.cgi',auth=HTTPDigestAuth('root', 'root'))
    #soup_config = BeautifulSoup (r.text, 'lxml')
    #list_config = soup.find_all('td', class_='ant_low_vol')
        
    #print('Response  ',r.status_code)
    #print ('GH/S RT   '   , list_tag[1].text.strip())
    #print ('Alive      ', list_tag[11].text.strip())
    #print ('HW total  ', list_tag[77].text.strip())
    #print ('chain  Temp    Chip num   Rt        HW')
    
    print ('',list_tag[93].text.strip(), '   ', list_tag[100].text.strip() , '       ' ,list_tag[94].text.strip(), '    ',list_tag[97].text.strip(),'  ',list_tag[98].text.strip() )
    print ('',list_tag[102].text.strip(), '   ', list_tag[109].text.strip() , '       ' ,list_tag[103].text.strip(), '    ',list_tag[106].text.strip(),'  ',list_tag[107].text.strip() )
    print ('',list_tag[111].text.strip(), '   ', list_tag[118].text.strip() , '       ' ,list_tag[112].text.strip(), '    ',list_tag[115].text.strip(),'  ',list_tag[116].text.strip() )
    print ('',list_tag[120].text.strip(), '   ', list_tag[127].text.strip() , '       ' ,list_tag[121].text.strip(), '    ',list_tag[124].text.strip(),'  ',list_tag[125].text.strip() )
    print ('',list_tag[118].text.strip(), '   ', list_tag[111].text.strip() , '       ' ,list_tag[112].text.strip(), '    ',list_tag[115].text.strip(),'  ',list_tag[116].text.strip() )
    
    
    


	
	
bot.infinity_polling()