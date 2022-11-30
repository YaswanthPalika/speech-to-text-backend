import speech_recognition as sr
import pyttsx3
import re
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import string
import nltk
import warnings
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import urllib
import requests
import yake
warnings.filterwarnings("ignore", category=DeprecationWarning)


s1 = new_text.replace("[^a-zA-Z#]", " ")

# removing short words


def fun(x): return ' '.join([w for w in x.split() if len(w) > 3])


s1 = fun(s1)

# tokenization
s2 = s1.split()

all_words = ' '.join(text for text in s2)

# extracting keywords
kw_extractor = yake.KeywordExtractor()
keywords = kw_extractor.extract_keywords(all_words)
for kw in keywords:
    print(kw[0])

# vizualization
wordcloud = WordCloud(width=800, height=800, background_color='white',
                      min_font_size=10).generate(all_words)
plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()
