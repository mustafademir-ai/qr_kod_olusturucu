import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import pyqrcode
from pyqrcode import QRCode

# QR kod oluşturma fonksiyonu
def qrkodolustur():
    url = url_girdi.get()
    
    if url:
        try:
            qr_url = pyqrcode.create(url)
            dosya_yolu = filedialog.asksaveasfilename(
                defaultextension=".svg",
                filetypes=[("SVG dosyaları", "*.svg")]
            )

            if dosya_yolu:
                qr_url.svg(dosya_yolu, scale=8)
                durum.config(text="✅ QR kod başarıyla kaydedildi!", fg="green")
        except Exception as e:
            messagebox.showerror("Hata", f"Bir hata oluştu:\n{e}")
    else:
        durum.config(text="⚠️ Lütfen bir URL giriniz.", fg="red")

# Ana pencereyi oluştur
pencere = tk.Tk()
pencere.title("🔳 QR Kod Oluşturucu")
pencere.geometry("450x200")
pencere.resizable(False, False)
pencere.configure(bg="#f2f2f2")

# Yazı tipi ayarları
font_baslik = ("Helvetica", 14, "bold")
font_normal = ("Helvetica", 11)

# Başlık etiketi
baslik = tk.Label(pencere, text="QR Kod Oluştur", font=font_baslik, bg="#f2f2f2")
baslik.pack(pady=10)

# URL giriş çerçevesi
giris_cercevesi = tk.Frame(pencere, bg="#f2f2f2")
giris_cercevesi.pack(pady=5)

etiket = tk.Label(giris_cercevesi, text="URL giriniz:", font=font_normal, bg="#f2f2f2")
etiket.grid(row=0, column=0, padx=5, pady=5)

url_girdi = tk.Entry(giris_cercevesi, width=40, font=font_normal)
url_girdi.grid(row=0, column=1, padx=5, pady=5)

# Buton
olusturbutonu = tk.Button(
    pencere, text="QR Kod Oluştur", font=font_normal, bg="#4CAF50", fg="white",
    width=20, command=qrkodolustur
)
olusturbutonu.pack(pady=10)

# Durum etiketi
durum = tk.Label(pencere, text="", font=font_normal, bg="#f2f2f2")
durum.pack()

# Tkinter döngüsünü başlat
pencere.mainloop()
