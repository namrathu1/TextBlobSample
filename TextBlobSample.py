# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 11:19:25 2018

@author: SmithaK
"""

from textblob import TextBlob
wiki = TextBlob("Im learning ML and im very happy")
print(wiki.tags)
print(wiki.words)
print(wiki.sentiment.polarity)
print(wiki.noun_phrases)