from flask import Flask
import random

#http://127.0.0.1:5000/

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '''<h1>Web siteme hoşgeldiniz!</h1>
      <a href="/rastgele_gercek">Rastgele bir gerçeği görüntüle! </a>
      <a href="/sifre_sayfasi">/ 15 haneli bir şifre oluştur!</a>
      '''

gercek = ["Pythonda bir string'in başına tırnak işaretlerinden önce f koyarsan {} işareti arasında yazdığın değişkeni string'e yazar.",
          "Pythonda uzun listelerle uğraşırken virgülden sonra enter basarsan alt satıra geçer.",
          "Pythonda (''') üç kesme işareti kullanarak çok sayıda satırdan oluşan stringler ve komutlar yazmak mümkündür.",
          "Flask ile çalışırken stringlerin içindeki html kodlarını python tanır."]

@app.route("/rastgele_gercek")
def second_page():
    info = random.choice(gercek)
    return  f'''<h1> Rastgele gerçekler: </h1>
              <h2>  {info} </h2>
            '''

@app.route("/sifre_sayfasi")
def sifre_sayfasi():
    icerik = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    password = ""
    for i in range(15):
        password += random.choice(icerik)
    return  f'''<h1> Şifreniz başarıyla oluşturuldu: </h1>
              <h2>  {password} </h2>
            '''

app.run(debug=True)
