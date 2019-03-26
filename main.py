# -*-coding:utf8-*-
from tkinter import *


# Hesaplama fonksiyonu
def hesapla():
    anaParaVar = int(anaParaEntry.get())
    oranVar = int(oranEntry.get())
    yilVar = int(yilEntry.get())
    basit_faiz = (anaParaVar*oranVar*yilVar)/100
    Result.config(text="Faiz miktarı : %s" % basit_faiz)


# Root Pencere
main = Tk()
main.geometry("200x300")

# Ana para için label ve entry
anaParaLbl = Label(text="Ana parayı giriniz")
anaParaLbl.pack()
anaParaEntry = Entry(main)
anaParaEntry.pack(side="top", pady=10)

# Oran için label ve entry
oranLbl = Label(text="Oran giriniz")
oranLbl.pack()
oranEntry = Entry(main)
oranEntry.pack(side="top", pady=10)

# Yıl için label ve entry
yilLbl = Label(text="Yıl giriniz")
yilLbl.pack()
yilEntry = Entry(main)
yilEntry.pack(side="top", pady=10)

# Hesaplama için Buton
buton = Button(main)
buton.config(text="Hesapla")
buton.config(command=hesapla)
buton.pack(side="top", pady=10)

# Sonuç için label
Result = Label(main)
Result.config(text="Değerleri giriniz...")
Result.pack(side="top", pady=10)


# Program döngüsü
main.mainloop()
