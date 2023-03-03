import time
from tkinter import *
from tkinter import ttk


def finish():
    root.destroy()  # ручное закрытие окна и всего приложения
    print("Закрытие приложения")
    
    
root = Tk()     # создаем корневой объект - окно
root.title("BTC_PROG")     # устанавливаем заголовок окна
root.geometry("1440x500+200+340")    # устанавливаем размеры окна

#______________button____________________

btn_buy = Button(text="BUY!", bg = 'green', heigh = 3, width = 6,borderwidth=5, font = ('Impact',20 ))
btn_sell = Button(text="SELL!", bg = 'red', heigh = 3, width = 6,borderwidth=5, font = ('Impact',20 ))
btn_update = Button(text="PRICE", bg = 'grey', heigh = 3, width = 6,borderwidth=5, font = ('Impact',20 ),command = Get_Price_btc)
#btn_update = Button(text="Price", bg = 'grey', width = 4,borderwidth=5,
 #                   font = ('Impact',20 ),padx = 1, pady = 1,command = Get_Price_btc)
#______________Entry_____________________

#entry_buy = Entry()
#entry_buy.insert(index, str)

#_____________place widger________________

btn_buy.place(x=10,y=350)    # размещаем кнопку в окне
btn_sell.place(x=200,y=350)
btn_update.place(x=390,y=350)



root.protocol("WM_DELETE_WINDOW", finish)
#th.start()
root.mainloop()
