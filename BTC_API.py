from binance.client import Client
import os
import time
import pandas as pd
from tkinter import *
import tkinter
from threading import Thread
import threading
from playsound import playsound


api_key = 'TyzeDcleTpIf0kUveTKuBPiEsTwGRCw7NRJ6z0GINR7lRfGKn8YYErzlSI6QHJn8'
api_secret = 'oYRTToPhoM9OLgXLfbB13rzGk12mpbFRWkuPLmoiXQiUbRttRLjdNZSOHoomWHTc'
client = Client(api_key, api_secret)

last_time = 0
last_price = 1

root = Tk()                          # создаем корневой объект - окно
root.title("BTC_PROG")               # устанавливаем заголовок окна
root.geometry("1440x500+200+340")    # устанавливаем размеры окна
radio_var_value = tkinter.IntVar()   # ___global value for RadioButton
radio_var_value.set(10)              # __ set value default   







try:
    client.ping()
    print("PING OK")
except Exception:
    print("NO PING SERVER!")
    





#___________________Radio___button_______________

radio_btn1 = Radiobutton(text='1 min', value=60, variable=radio_var_value)
radio_btn2 = Radiobutton(text='2 min', value=120, variable=radio_var_value)
radio_btn3 = Radiobutton(text='3 min', value=180, variable=radio_var_value)
radio_btn4 = Radiobutton(text='4 min', value=240, variable=radio_var_value)

radio_btn1.place(x=700,y=10)
radio_btn2.place(x=700,y=30)
radio_btn3.place(x=700,y=50)
radio_btn4.place(x=700,y=70)





def printit():  #__________Get_Price_btc()
    threading.Timer(radio_var_value.get(), printit).start()
    print("Hello, World!")
    Get_Price_btc()
          

def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")



def Get_Price_btc():   #__________________get price time 
    t = client.get_avg_price(symbol='BTCUSDT')
    global last_price,last_time
    price_btc = round(float(t['price']),1)
    
    label_price_btc = Label(bg='grey', text='$' + str(price_btc) + ' BTC/USDT',font = ('Impact',20 )) # создаем текстовую метку
    label_last_price = Label(bg='grey', text='Last price : $'+ str(last_price),font = ('Impact',20 ))
    label_time_price_btc = Label(bg='grey', text=''+ time.ctime(time.time()),font = ('Impact',14 )) # создаем текстовую метку
    label_last_time = Label(bg='grey', text=''+ str(last_time),font = ('Impact',14 ))
    
    
    entry_buy = Entry()
    entry_buy.insert(0, 'market  '+ str(round(float(t['price']))))
    
    #___calculate percent change cost
    change_percent_BTC = (price_btc-last_price)/last_price*100
    #___if UP cost  GREEN if down cost RED
    if change_percent_BTC >= 0:
        bg_='green'
    else:
        bg_='red'
    #___edit lable percnt change    
    label_percent = Label(bg=bg_, text=str(round(change_percent_BTC,2)),font = ('Impact',14 ))
    
    
    label_price_btc.place(x=300,y=5)
    label_last_price.place(x=1,y=5)
    label_time_price_btc.place(x=300,y=50)
    label_last_time.place(x=1,y=50)
    label_percent.place(x=600,y=12,width=50)
    entry_buy.place(x=0,y=300)
    
    last_time = time.ctime(time.time())
    last_price = round(float(t['price']),1)
    print(radio_var_value.get())
    playsound("/home/ss/Prog/Other/Sound_04590.mp3")
  
  




#th = Thread(target=remind, args=())   #__________________многопоточность

#th = Timer(5.0, Get_Price_btc())
#th.start()
#________________function

#Get_Price_btc()
#  printit()

# И запускаем его


#______________button_

btn_buy = Button(text="BUY!", bg = 'green', heigh = 3, width = 6,borderwidth=5, font = ('Impact',20 ))
btn_sell = Button(text="SELL!", bg = 'red', heigh = 3, width = 6,borderwidth=5, font = ('Impact',20 ))
btn_update = Button(text="PRICE", bg = 'grey', heigh = 3, width = 6,borderwidth=5, font = ('Impact',20 ),command = Get_Price_btc)
#btn_update = Button(text="Price", bg = 'grey', width = 4,borderwidth=5,
 #                   font = ('Impact',20 ),padx = 1, pady = 1,command = Get_Price_btc)
#______________Entry

#entry_buy = Entry()
#entry_buy.insert(index, str)

#_____________place widger________________

btn_buy.place(x=10,y=350)    # размещаем кнопку в окне
btn_sell.place(x=200,y=350)
btn_update.place(x=390,y=350)









#print(client.get_historical_trades(symbol='BTCUSDT'))
#print(pd.DataFrame(client.get_symbol_info('BTCUSDT'),index=[5]))
#print(client.get_products('BTCUSDT'))
#t = client.get_avg_price(symbol='BTCUSDT') 
#print(client.get_avg_price(symbol='BTCUSDT'))
#print(pd.DataFrame(t, index=[0]))
#print(pd.DataFrame(client.get_historical_trades(symbol='BTCUSDT'), index=[1]))


  #_______________________________МНОГОПОТЧОНОСТЬ	
  
#Get_Price_btc()
printit()
root.protocol("WM_DELETE_WINDOW", finish)
#th.start()
root.mainloop()

