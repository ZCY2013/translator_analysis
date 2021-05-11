# coding: utf-8
import txt_pure
import jieba
import os
from wordcloud import WordCloud, ImageColorGenerator
import pickle
import matplotlib.pyplot as plt



'''统计词频'''
def statistics(texts, stopwords):
	words_dict = {}
	for text in texts:
		temp = jieba.cut(text)
		for t in temp:
			if t in stopwords or t == 'unknow':
				continue
			if t in words_dict.keys():
				words_dict[t] += 1
			else:
				words_dict[t] = 1
	return words_dict


'''词云'''
def drawWordCloud(words, title, savepath='./results'):
	if not os.path.exists(savepath):
		os.mkdir(savepath)
	wc = WordCloud(font_path='simkai.ttf', background_color='white', max_words=2000, width=1920, height=1080, margin=5)
	wc.generate_from_frequencies(words)
	wc.to_file(os.path.join(savepath, title+'.png'))


if __name__ == '__main__':

	with open(txt_pure.save_file_path, 'rb') as f:
		text = f.read()
		words = jieba.lcut(text)
		cuted = ' '.join(words)
		f.close()
	print(cuted[:200])
	wc = WordCloud(background_color="white",  # 背景颜色
				   max_words=1000,  # 词云显示的最大词数
				   max_font_size=500,  # 字体最大值
				   min_font_size=20,  # 字体最小值
				   random_state=42,  # 随机数
				   collocations=False,  # 避免重复单词
				   width=1600, height=1200, margin=10,  # 图像宽高，字间距，需要配合下面的plt.figure(dpi=xx)放缩才有效
				   )
	wc.generate(cuted)
	plt.figure(dpi=100)  # 通过这里可以放大或缩小
	plt.imshow(wc, interpolation='catrom', vmax=1000)
	plt.show()
	plt.axis("off")  # 隐藏坐标