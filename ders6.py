#ders6 :kütüphane yüklenmesi
#kütüphaneler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# CSV dosyasının tam yolu
dosya_yolu = "C:\\Users\\seytim13\\PycharmProjects\\py-ml-lessons\\veriler.csv"

# CSV dosyasını yükle
df = pd.read_csv("C:\\Users\\seytim13\\PycharmProjects\\py-ml-lessons\\veriler.csv")
print(df)

boy_kilo=(df[['boy']])
print(boy_kilo)
print(df[['boy','kilo']])

print(df[['yas','cinsiyet']])
