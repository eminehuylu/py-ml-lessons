import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

# CSV dosyasının tam yolu
dosya_yolu = "C:\\Users\\seytim13\\PycharmProjects\\py-ml-lessons\\eksikveriler.csv"

# CSV dosyasını yükle
df = pd.read_csv(dosya_yolu)
print("Veri Çerçevesi:\n", df)

imputer = SimpleImputer(missing_values=np.nan, strategy='mean')
yas_sutunlari = df.iloc[:, 1:4].values
print("\nİlk Durum:\n", yas_sutunlari)

# Eksik değerleri ortalama ile doldur
yas_sutunlari = imputer.fit_transform(yas_sutunlari)
#fitle öğretip transformla öğrenileni alıyoruz
print("\nEksik Değerler Ortalama ile Doldurulmuş Hali:\n", yas_sutunlari)
