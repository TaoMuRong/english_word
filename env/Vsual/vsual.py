# 导入地图
from pyecharts import Map
# 导入柱状图
from pyecharts import Bar
# 导入词云图
from pyecharts import WordCloud

# 中国地图
def chinaMap(direction):
	# 进行省分分配
	province  = [i for i in direction.地区]
	# 报考人数分配
	number = [i for i in direction.报考人数]
	map = Map("报考人数分布图",'部分省份未统计',width=1200, height=600)
	map.add("省会", province, number, visual_range=[0, 50], maptype='china', is_visualmap=True,
is_map_symbol_show=False, visual_text_color='#000')
	map.render(path="../Vsual/考研人数分布图.html")

# 柱状图
def barPicture(initial):
	columns = [i for i in initial]
	word = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w']
	num = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
	j = 0
	for i in columns:
		if word[j] == i :
			num[j] += 1
		else:
			j = j % 22 + 1
	bar = Bar("柱状图", "单词首字母出现次数")
	bar.add("单词出现次数", word, num, mark_line=["average"], mark_point=["max", "min"])
	bar.render(path="../Vsual/单词首字母出现次数.html")

# 词云图
def wordCloud(collectCsv):
	englishWord = [i for i in collectCsv.单词]
	chineseWord = [i for i in collectCsv.释义]
	value = [10000, 6181, 4386, 4055, 2467, 2244, 1898, 1484, 1112, 965, 847, 582, 555, 550, 462, 366, 360, 282, 273,265]
	# 生成单词词云图
	englishwordcloud = WordCloud(width=1300, height=620)
	englishwordcloud.add("单词词云图", englishWord, value, word_size_range=[0, 1])
	englishwordcloud.show_config()
	englishwordcloud.render(path="../Vsual/单词词云图.html")
	# 生成汉字词云图
	chinesewordcloud = WordCloud(width=1300, height=620)
	chinesewordcloud.add("汉字释义词云图", chineseWord, value, word_size_range=[20, 100])
	chinesewordcloud.show_config()
	chinesewordcloud.render(path="../Vsual/汉字释义词云图.html")