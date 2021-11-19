import pandas as pd
import numpy as np
import jieba
import pyecharts.options as opts
from pyecharts.charts import Line, Bar, Grid, Funnel
from pyecharts.faker import Faker

olympic_sports = ["田径", "赛艇", "跆拳道", "自行车", "帆船", "皮划艇", "射剑", "射击", "游泳", "铁人三项", "现代五项", "拳击 ", "击剑 ", "柔道", "摔跤",
				  "举重", "体操", "乒乓球 ", "羽毛球", "排球", "篮球", "足球 ", "棒球", "垒球", "曲棍球", "手球", "网球", "马术","滑板","冲浪","竞技攀岩",
				  "棒垒球","空手道"]
FILTER_WORDS = ['男子', '10', '跳台', '静水', '女子', '500', '双人', '划艇', '女子', '标枪',  '男子', '团体',  '女子', '团体',  '女子', '10', '跳台', 
				'女子', '平衡木', '男子', '双杠',  '男子', '跳板', '女子', '87', '公斤', '上级', '场地', '女子', '团体', '争先', '男子', '吊环', '男子',
				 '50', '步枪', '三姿', '女子', '87', '公斤', '女子单打',  '女子', '跳板', '女子', '铅球', '男子', '81', '公斤', '女子', '帆板', 'RS',  
				 '男子单打', '混合双打', '蹦床', '女子组', '男子', '200', '个人', '混合泳',  '女子单打', '女子', '4x200',  '接力', '女子', '200',  
				 '男子', '73', '公斤',  '男子', '双人', '跳板', '女子', '四人', '双桨', '混合', '团体', '10', '气步枪',  '女子', '双人', '10', '跳台', 
				 '混合', '团体', '10', '气手枪', '男子', '67', '公斤', '男子', '61', '公斤',  '女子', '双人', '跳板', '女子', '个人', '重剑', '女子', 
				 '49', '公斤', '女子', '10', '气步枪', '女子', '中量级', '69', '75', '公斤', '女子', '自由式', '50', '公斤', '团体',  '男子', 
				 '10', '跳台', '女子', '量级', '64', '69', '公斤', '静水', '男子', '1000', '单人', '划艇', '女子', '自由式', '53', '公斤', 
				 '女子组', '61', '公斤',  '女子', '10', '跳台', '男子', '三级跳远', '双人', '女子', '链球', '女子', '平衡木',  '男子', '跳板', '静水', 
				 '男子', '1000', '双人', '划艇', '男子单打', '男子', '吊环', '女子双打',  '女子', '跳板', '男子双打', '蹦床', '男子组', '男女', 
				 '混合', '4x100', '混合泳', '接力',  '男子单打', '混合双打', '蹦床', '女子组',  '女子单打', '男子', '全能',  '混合双打', '女子', '55', 
				 '公斤',  '男子', '双人', '10', '跳台', '女子', '100',  '男子', '10', '气步枪', '女子组', '61', '公斤', '上级', '女子', '20', '公里', 
				 '女子', '自由式', '76', '公斤', '男子', '古典式', '60', '公斤', '男子', '25', '手枪', '速射', '男子', '男子', '帆板',
				 'RS', '女子', '25', '手枪', '女子', '八人', '单桨', '舵手', '三人', '女子组', '男子', '双人', '双桨', '男子', '团体', '女子', '双向', 
				 '飞碟', '女子', '400',  '男子', '68', '公斤', '男子', '10', '气步枪', '女子', '10', '气手枪', '男子', '10', '气手枪']
# 数据读取
def to_read_data():
	medal_list = ['golds','silvers', 'bronzes ']
	medals_data = []
	for i in medal_list:
		medals_datum = pd.read_excel(f'东京奥运会数据/{i}.xlsx')
		medals_data.append(medals_datum)
	return medals_data


# 数据预处理：空值处理，简单筛选
def data_pre_processing():
	data = to_read_data()
	medals_data = []
	for i in data:
		i = i[~(i['日期'].isnull())]  # 删掉空行
		i = i.loc[i['countryid'].str.contains('CHN')]	# 筛选出中国的数据
		medals_data.append(i)
	return medals_data


# 可视化part1
def chart_one(data):
	# 透视数据
	df_p1 = data[0].pivot_table(index='日期',    
						values='名次',	
						aggfunc='count'	
						 )
	df_p2 = data[1].pivot_table(index='日期',    
						  values='名次',    
						  aggfunc='count'    
						 )
	df_p3 = data[2].pivot_table(index='日期',    
						  values='名次',    
						  aggfunc='count'    
						 )
	medals_num = pd.merge(pd.merge(df_p1, df_p2, how="outer", on="日期"),df_p3,how="outer", on="日期")
	medals_num.fillna(0, inplace=True)
	medals_num.sort_values(by='日期',ascending=True, inplace=True)# 排序
	date = []
	for i in range(0,16):
		date.append((medals_num.index.astype(str))[i])
	gold_medal, silver_medal, bronze_medal = medals_num['名次_x'].to_list(), medals_num['名次_y'].to_list(), medals_num['名次'].to_list()
	
	# 柱形图
	bar = (
		Bar()
		.add_xaxis(date)
		.add_yaxis("金牌", gold_medal, stack="stack1", color="#CD7F32")
		.add_yaxis("银牌", silver_medal, stack="stack1", color="#C0C0C0")
		.add_yaxis("铜牌", bronze_medal, stack="stack1", color="#FFD700")
		.set_series_opts(
			label_opts=opts.LabelOpts(is_show=False),
		)
		.set_global_opts(
			title_opts=opts.TitleOpts(subtitle="单位：枚"),
			brush_opts=opts.BrushOpts(),
		)
	)

	gold_medals, silver_medals, bronze_medals = [], [], []
	n1, n2, n3 = 0, 0, 0
	for j in range(0,16):
		# 金
		n1 += gold_medal[j]
		gold_medals.append(n1)
		# 银
		n2 += silver_medal[j]
		silver_medals.append(n2)
		# 铜
		n3 += bronze_medal[j]
		bronze_medals.append(n3)

	# 折线图
	line = (
		Line()
		.add_xaxis(date)
		.add_yaxis("金牌", gold_medals, is_smooth=True, color="#CD7F32")
		.add_yaxis("银牌", silver_medals, is_smooth=True, color="#C0C0C0")
		.add_yaxis("铜牌", bronze_medals, is_smooth=True, color="#FFD700")
		.set_series_opts(
			areastyle_opts=opts.AreaStyleOpts(opacity=0.5),
			label_opts=opts.LabelOpts(is_show=False),
		)
		.set_global_opts(
			xaxis_opts=opts.AxisOpts(
				axistick_opts=opts.AxisTickOpts(is_align_with_label=True),
				is_scale=False,
				boundary_gap=False,
			),
		)
	)
	grid = (
		Grid(init_opts=opts.InitOpts(width="100%",height="750px",page_title="我国奖牌随时间分布情况"))
		.add(bar, grid_opts=opts.GridOpts(pos_right="60%",pos_left="1%"))
		.add(line, grid_opts=opts.GridOpts(pos_left="50%",pos_right="0.5%"))
		.render("我国奖牌随时间分布情况.html")
	)

# 可视化part2
def chart_two(data):
	temp_list = []
	for i in range(0,3):
		for j in data[i]['项目'].to_list():
			temp_list.append(j)
	comment_str_all = ''
	for comment in temp_list:
		comment_str_all +=comment + '\n'
	
	#获取分词后的列表
	seg_list = list(jieba.cut(comment_str_all))
	#转换成Pandas的Series类型数据
	keywords_counts = pd.Series(seg_list)
	#统计各个关键词的出现次数
	keywords_counts = keywords_counts.value_counts()
	keywords_counts = pd.Series(seg_list)
	keywords_counts = keywords_counts[keywords_counts.str.len()>1]
	keywords_counts = keywords_counts[~keywords_counts.str.contains('|'.join(FILTER_WORDS))]
	# print(keywords_counts.to_list())
	keywords_counts = keywords_counts.value_counts()#筛选完才能做value_counts
	result_data = zip(keywords_counts.index.to_list(),keywords_counts.to_list())
	c = (
		Funnel()
		.add(
			"商品",
			list(result_data),
			sort_="ascending",
			label_opts=opts.LabelOpts(position="inside"),
		)
		.set_global_opts(title_opts=opts.TitleOpts(title="Funnel-Sort（ascending）"))
		.render("funnel_sort_ascending.html")
	)
	# print([list(z) for z in zip(Faker.choose(), Faker.values())])



if __name__ == "__main__":
	medals_data = data_pre_processing()
	chart_one(medals_data)
	chart_two(medals_data)


