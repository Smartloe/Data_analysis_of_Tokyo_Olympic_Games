# 分析奥运会奖牌分布情况并可视化
import requests
import json
import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Map, Bar, Grid, Page, WordCloud
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType


# 数据读取
def Data_processing():
	# 读取Excel文件
	file = pd.ExcelFile('东京奥运会数据/national_medal.xlsx')
	data = file.parse()
	# 读取json文件
	with open('name_map.json', 'r', encoding='utf8')as fp:
		name_map = json.load(fp)
	data = [data, name_map]
	return data


# 奖牌全球分布图
def Medals_distribution_map(data):
	countries_and_nums = dict(zip(data['国家'].to_list(), data['总数'].to_list()))
	countries_and_nums['中国'] = countries_and_nums['中国'] + countries_and_nums['中国台北'] + countries_and_nums['中国香港']
	del countries_and_nums["中国台北"]
	del countries_and_nums["中国香港"]
	countries_en = []
	for i in countries_and_nums.keys():  # 遍历字典的键
		if i in name_map.values():
			countries_en.append(list(name_map.keys())[list(name_map.values()).index(i)])
	medal_num = []
	for j in countries_and_nums.values():
		medal_num.append(j)
	list_countries_nums = [countries_en, medal_num]
	# print([list(z) for z in zip(list_countries_nums[0], list_countries_nums[1])])
	map_world = (
		Map(init_opts=opts.InitOpts(theme="vintage", chart_id=1))
			.add("", [list(z) for z in zip(list_countries_nums[0], list_countries_nums[1])], "world",
				 is_map_symbol_show=False)
			.set_series_opts(label_opts=opts.LabelOpts(is_show=False))
			.set_global_opts(
			title_opts=opts.TitleOpts(title="东京奥运会-奖牌全球分布图", subtitle='单位: 枚'),
			visualmap_opts=opts.VisualMapOpts(max_=120),
		)
	)
	return map_world


# 奖牌排行条形图
def Medals_ranking(data):
	bar = (
		Bar(init_opts=opts.InitOpts(theme="vintage", chart_id=2))
			.add_xaxis((data['国家'].to_list())[:5])
			.add_yaxis("金牌", (data['金牌'].to_list())[:5])
			.add_yaxis("银牌", (data['银牌'].to_list())[:5])
			.add_yaxis("铜牌", (data['铜牌'].to_list())[:5])
			.set_global_opts(
			title_opts={"text": "奖牌数量", "subtext": "单位: 枚"}
		)
	)
	return bar


# 词云图
def Word_cloud(data):
	words = list(zip(data['国家'].to_list(), data['总数'].to_list()))
	word_cloud = (
		WordCloud(init_opts=opts.InitOpts(theme="vintage", chart_id=3))
			.add(
			"",
			words,
			word_size_range=[20, 100],
			textstyle_opts=opts.TextStyleOpts(font_family="cursive"),
		)
			.set_global_opts(title_opts=opts.TitleOpts(title="奖牌数量词云图"))
	)
	return word_cloud


# 页面布局
def page_simple_layout(data):
	page = Page(layout=Page.DraggablePageLayout, page_title="奥运会奖牌分布情况")
	# 将上面定义好的图添加到 page
	page.add(
		Medals_distribution_map(data),
		Medals_ranking(data),
		Word_cloud(data)
	)
	page.render("Data_screen.html")
	page.save_resize_html('Data_screen.html', cfg_file='chart_config.json', dest='Data_screen.html')


if __name__ == "__main__":
	data = Data_processing()
	name_map = data[1]
	data = data[0]
	page_simple_layout(data)
