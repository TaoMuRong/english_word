from pyecharts import Map

def chinaMap(direction):
	province  = [i for i in direction.地区]
	number = [i for i in direction.报考人数]
	map = Map("报考人数分布图",width=1200, height=600)
	map.add("省会", province, number, visual_range=[0, 50], maptype='china', is_visualmap=True,
is_map_symbol_show=False, visual_text_color='#000')
	map.render(path="考研人数分布图.html")