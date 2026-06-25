# 🔳 QR Kod Oluşturucu (QR Code Generator)

Bu proje, kullanıcının girdiği herhangi bir web sitesi linkini veya metni saniyeler içinde yüksek kaliteli bir **QR koda** dönüştüren **Python**, **Tkinter** ve **PyQRCode** tabanlı bir masaüstü uygulamasıdır. 

Oluşturulan QR kodlar, kalitesi bozulmadan istenildiği kadar büyütülebilmesi için **vektörel (SVG)** formatta kaydedilir.

---

## ✨ Özellikler

* **⚡ Hızlı QR Üretimi:** Girilen URL'yi anında taratılabilir bir QR koda dönüştürür.
* **📐 Vektörel Çıktı (SVG):** `scale=8` ölçeklendirmesi ile yüksek çözünürlüklü, baskıya hazır SVG dosyaları üretir. Tasarımlarda büyütüldüğünde pikselleşme yapmaz.
* **📂 Dinamik Dosya Kaydetme:** `filedialog` entegrasyonu sayesinde QR kodun bilgisayarda nereye ve hangi isimle kaydedileceğini kullanıcı seçer.
* **🎨 Dinamik Durum Bildirimleri:** Boş girişlerde uyarı (sarı/kırmızı), başarılı kayıtlarda ise onay mesajı (yeşil) vererek kullanıcıyı anlık bilgilendirir.
* **🛡️ Hata Yakalama:** Olası sistem veya kütüphane hatalarını `try-except` blokları ile yakalayarak uygulamanın çökmesini engeller ve kullanıcıya hata mesajı gösterir.

---

## 🛠️ Gereksinimler ve Kurulum

Uygulamanın çalışması için bilgisayarınızda Python 3.x yüklü olmalı ve QR kod üreten harici kütüphane kurulmalıdır. Terminal veya komut satırını açarak aşağıdaki komutla kurulumu gerçekleştirebilirsiniz:

```bash
pip install pyqrcode
```

*(Not: `tkinter` kütüphanesi Python'ın standart kütüphanesidir, ekstra bir kurulum gerektirmez.)*

---

## 🚀 Nasıl Çalıştırılır?

1. Bu depoda bulunan kodları `qr_olusturucu.py` adıyla bir dosyaya kaydedin.
2. Terminal veya komut satırından dosyanın bulunduğu dizine gidin:
   ```bash
   cd projenin_bulundugu_klasor
   ```
3. Uygulamayı başlatmak için şu komutu çalıştırın:
   ```bash
   python qr_olusturucu.py
   ```
4. Açılan sade arayüze URL adresinizi (örneğin: `https://github.com`) yazın, **QR Kod Oluştur** butonuna basın ve kaydedeceğiniz yeri seçin!

---

## 📝 Teknik Detaylar

* **`pyqrcode.create(url)`**: Girilen metni standartlara uygun bir QR kod nesnesine dönüştürür.
* **`defaultextension=".svg"`**: Kullanıcı dosya uzantısını yazmasa bile sistem otomatik olarak dosyayı `.svg` formatında paketler.
* **`resizable(False, False)`**: Pencere boyutlarının bozulmaması ve arayüz tasarımının sabit kalması için yeniden boyutlandırma kilitlenmiştir.
