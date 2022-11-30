#import speech_recognition as sr
#import pyttsx3
import re
import sys
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

n12 = sys.argv[1]
print(n12)


s1 = n12.replace("[^a-zA-Z#]", " ")


# removing short words


def fun(x): return ' '.join([w for w in x.split() if len(w) > 3])


s1 = fun(s1)

# tokenization
s2 = s1.split()

all_words = ' '.join(text for text in s2)

result = ""
# extracting keywords
kw_extractor = yake.KeywordExtractor()
keywords = kw_extractor.extract_keywords(all_words)
for kw in keywords:
    result += kw[0] + ","

print(result)
