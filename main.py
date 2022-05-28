from tkinter import *
from tkinter import messagebox
import time

pencere = Tk()
 
pencere.title("KDV Hesaplayıcı v2.0 - developed by whiskydev11")
pencere.geometry("600x300")

uygulama = Frame(pencere)
uygulama.grid()

# Hata mesajımızı bu Label'e yazdıracaz
L3 = Label(pencere)
L3.place(x=148,y=200)

L1 = Label(uygulama, text="Ürün Fiyatını Giriniz:")
L1.grid(padx=110, pady=10)
 
E1 = Entry(uygulama, bd =2)
E1.grid(padx=110, pady=3)

L2 = Label(uygulama, text="KDV Oranını Giriniz:")
L2.grid(padx=115, pady=15)
 
E2 = Entry(uygulama, bd =2)
E2.grid(padx=115, pady=8)

def islem():
    if (not E1.get()):
        messagebox.showerror("Değer Bulunamadı!", "Ürün fiyatını girmeden bu işlemi yapamazsınız.")

    elif (not E2.get()):
        messagebox.showerror("Değer Bulunamadı!", "KDV Oranını girmeden bu işlemi yapamazsınız.")

    try:
        temizKdvOrani = int(E2.get().strip("%"))
        hesapla = (int(E1.get()) * temizKdvOrani) / 100
        hesapla2 = int(E1.get()) + hesapla
        messagebox.showinfo(f"Sonuç", f"KDV Dahil Olmayan Fiyat: {int(E1.get())} \nKDV Oranı: {hesapla} \nKDV Dahil Fiyat: {hesapla2}")

    except ValueError:
        messagebox.showerror("Değer Geçersiz!", "Geçersiz bir değer girdiğiniz için hesap yapılamadı. Lütfen tekrar deneyin.")

def cikis():
    exit(0)

def credits():
    messagebox.showinfo("Krediler", "Geliştirici: whiskydev11 \n \nGithub: github.com/whiskydev11 \n \nWebsite: whiskydev.xyz")


kullan = Button(uygulama,
            text="Hesapla",
            padx="60",pady="5",
            command=islem)
kullan.grid(padx=60, pady=5)

kullan2 = Button(uygulama,
            text="Programı Kapat",
            padx="60",pady="5",
            command=cikis)
kullan2.grid(padx=60, pady=5)

kullan3 = Button(uygulama,
            text="Krediler",
            padx="60",pady="5",
            command=credits)
kullan3.grid(padx=60, pady=5)

pencere.mainloop()
