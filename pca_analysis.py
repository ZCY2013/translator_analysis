# coding: utf-8
import txt_pure
import jieba
import os
from wordcloud import WordCloud, ImageColorGenerator
import pickle
import matplotlib.pyplot as plt

if __name__ == '__main__':

	with open(txt_pure.save_file_path, 'rb') as f:
		text = f.read()
		words = jieba.lcut(text)
		cuted = ' '.join(words)
		f.close()