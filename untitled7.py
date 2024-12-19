# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Zx9vWRg7bLMWme7rOdGURofM85bwQy7v
"""

import pandas as pd

# CSV faylni yuklab olish
url = 'https://github.com/Zulayho06/Maxsus-topshiriq/blob/main/WHO%20COVID-19%20cases.csv?raw=true'
df = pd.read_csv(url)

# Ma'lumotlar to'plamini ko'rib chiqamiz
print(df.head())

# Ma'lumotlar to'plamining ustunlarini ko'rib chiqamiz
print(df.columns)

# Davlatlar bo'yicha aniqlangan covid holatlarini hisoblash
country_cases = df.groupby('Country')['New_cases'].sum().reset_index()

# Eng ko'p covid holatlar aniqlangan davlatlar ro'yxati
print(country_cases.sort_values(by='New_cases', ascending=False))