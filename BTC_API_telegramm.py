from binance.client import Client
import telebot
from telebot import types
from threading import Timer
import time

last_price = 1

bot = telebot.TeleBot('')
api_key = ''
api_secret = ''

client = Client(api_key, api_secret)

try:
    client.ping()
    print("PING OK")
except Exception:
    print("NO PING SERVER!")



#______________get price function_____________
def get_and_calculate_price():
    t = client.get_avg_price(symbol='BTCUSDT')
    global last_price
    price_btc = round(float(t['price']),1)
    
    change_percent_BTC = (price_btc-last_price)/last_price*100
    if change_percent_BTC >= 1:
        bot.send_message(558777404,str(round(float(t['price']),1)))
        
    last_price = round(float(t['price']),1)
    
    return round(float(t['price']),1)



def get_open_orders():
    t = client.get_open_orders()
    bot.send_message(558777404,'dd') 
    
class RepeatedTimer(object):
    def __init__(self, interval, function, *args, **kwargs):
        self._timer     = None
        self.interval   = interval
        self.function   = function
        self.args       = args
        self.kwargs     = kwargs
        self.is_running = False
        self.start()

    def _run(self):
        self.is_running = False
        self.start()
        self.function(*self.args, **self.kwargs)

    def start(self):
        if not self.is_running:
            self._timer = Timer(self.interval, self._run)
            self._timer.start()
            self.is_running = True

    def stop(self):
        self._timer.cancel()
        self.is_running = False
    

#___________telegram bot________________
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'command:b - button')

@bot.message_handler(commands=['b'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Price")
    btn2 = types.KeyboardButton("Open Order")
    btn3 = types.KeyboardButton("Stop")
    
    markup.add(btn1,btn2,btn3)
    bot.send_message(message.chat.id,'button enable',reply_markup=markup)
    
    
@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text=="Price":#.................................... send Price
        Price = get_and_calculate_price()
        
        bot.send_message(message.chat.id,Price)
        
    elif message.text=="Open Order":#....................................send Order
        Open_order = client.get_open_orders()
    elif message.text=="Stop":#....................................send Order
        rt.stop()
        
rt = RepeatedTimer(2, get_open_orders)
     
bot.polling(none_stop=True, interval=0)

