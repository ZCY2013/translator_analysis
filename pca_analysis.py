# coding: utf-8
import txt_pure
import jieba
from sklearn import datasets
import os
from wordcloud import WordCloud, ImageColorGenerator
import pickle
import matplotlib.pyplot as plt
from gensim.models import word2vec

if __name__ == '__main__':

	with open(txt_pure.save_file_path, 'rb') as f:
		text = f.read()
		cuted = ' '.join(words)
		f.close()