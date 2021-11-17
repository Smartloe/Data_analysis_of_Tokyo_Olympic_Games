import pandas as pd
import numpy as np
import pyecharts.options as opts
from pyecharts.charts import Line, Bar, Grid
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
def chart_part1(data):
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
def chart_part1():
	pass

if __name__ == "__main__":
	chart_part1(data_pre_processing())
