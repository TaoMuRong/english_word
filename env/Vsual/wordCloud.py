import jieba
from wordcloud import WordCloud
from imageio import imread
import matplotlib.pyplot as plt
from collections import Counter

def chineseWordCloud():
	text = open(r'chinese.txt', encoding='utf8')
	mylist = list(text)
	word_list = [' '.join(jieba.cut(sentence)) for sentence in mylist]
	new_text = ' '.join(word_list)

	pac_mask = imread('word.jpg')
	wc = WordCloud(font_path='simhei.ttf', background_color='white', max_words=2000,
				   mask=pac_mask).generate(new_text)

	plt.imshow(wc)
	plt.axis("off")
	plt.show()
	wc.to_file(r'chineseWordCloud.png')  # 保存词云


def englishWordCloud():
	text = open(r'english.txt', encoding='utf8')
	mylist = list(text)
	word_list = [' '.join(jieba.cut(sentence)) for sentence in mylist]
	new_text = ' '.join(word_list)

	pac_mask = imread('word.jpg')
	wc = WordCloud(font_path='simhei.ttf', background_color='white', max_words=2000,
				   mask=pac_mask).generate(new_text)

	plt.imshow(wc)
	plt.axis("off")
	plt.show()
	wc.to_file(r'englishWordCloud.png')  # 保存词云

# 生成中文词云图
chineseWordCloud()

# 生成英文词云图
englishWordCloud()