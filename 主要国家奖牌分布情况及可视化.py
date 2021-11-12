import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Pie, Tab, Timeline, Bar, Page,  Grid, Gauge
from pyecharts.commons.utils import JsCode
from pyecharts.globals import ThemeType
from pyecharts.components import Table, Image
from pyecharts.faker import Faker

# 主要国家美国,中国(略),日本,英国,俄罗斯奥运队
# 维度时间,项目,类别（金,银,铜）

olympic_sports = ["田径", "赛艇", "跆拳道", "自行车", "帆船", "皮划艇", "射剑", "射击", "游泳", "铁人三项", "现代五项", "拳击 ", "击剑 ", "柔道", "摔跤",
				  "举重", "体操", "乒乓球 ", "羽毛球", "排球", "篮球", "足球 ", "棒球", "垒球", "曲棍球", "手球", "网球", "马术","滑板","冲浪","竞技攀岩",
				  "棒垒球","空手道"]
fn = """
	function(params) {
		if(params.name == '其他')
			return '\\n\\n\\n' + params.name + ' : ' + params.value + '%';
		return params.name + ' : ' + params.value + '%';
	}
	"""


def new_label_opts():
	return opts.LabelOpts(formatter=JsCode(fn), position="center")


# 数据读取
def data_reading():
	# 读取Excel文件
	data = pd.DataFrame()
	file_name = ['golds', 'silvers', 'bronzes ']
	# 合并表
	for i in file_name:
		file = pd.ExcelFile(f'东京奥运会数据/{i}.xlsx')
		df = file.parse()
		df = df[~(df['日期'].isnull())]  # 删掉空行
		data = data.append(df)	
	return data



# 美国,日本,英国,俄罗斯奥运队擅长的运动项目数据分析
def good_projects(data):
	countryids = ['USA','JPN','GBR','ROC']
	result_data = []
	for i in countryids:
		data_usa = data[data['countryid']==f'{i}']
		result = pd.pivot_table(data_usa, index=['项目'], columns=['countryid'], values=["名次"], aggfunc=[len])
		# 小项分类汇总为大项
		temp_list = []
		for i in data_usa['项目']:
			for j in olympic_sports:
				if j in i:
					temp_list.append(j)
					break
		d = pd.Series(temp_list).value_counts().head(5)
		reuslt = [list(z) for z in zip(list(d.keys()), list((d).to_list()))]
		result_data.append(reuslt)
	return result_data


# 美国,日本,英国,俄罗斯奥运队擅长的运动项目可视化展示
def good_projects_view(data):
	# 美国
	c_usa = (
		Pie(init_opts=opts.InitOpts(width="50%", height="400px"))
		.add(
			"",
			data[0],
			radius=["40%", "75%"],

		)
		.set_global_opts(
			title_opts=opts.TitleOpts(title="USA"),
			legend_opts=opts.LegendOpts(orient="vertical", pos_top="15%", pos_left="2%"),
		)
		.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
	)

	# 日本
	sum = 0
	for k in data[1]:
		sum += k[1]
	c_jpn = (
		Pie(init_opts=opts.InitOpts(width="50%", height="410px"))
		.add(
				"",
				[list(z) for z in zip([data[1][0][0], "其他"], [data[1][0][1], sum-data[1][0][1]])],
				center=["20%", "30%"],
				radius=[60, 80],
				label_opts=new_label_opts(),
			)
			.add(
				"",
				[list(z) for z in zip([data[1][1][0], "其他"], [data[1][1][1], sum-data[1][1][1]])],
				center=["55%", "30%"],
				radius=[60, 80],
				label_opts=new_label_opts(),
			)
			.add(
				"",
				[list(z) for z in zip([data[1][2][0], "其他"], [data[1][2][1], sum-data[1][2][1]])],
				center=["20%", "70%"],
				radius=[60, 80],
				label_opts=new_label_opts(),
			)
			.add(
				"",
				[list(z) for z in zip([data[1][3][0], "其他"], [data[1][3][1], sum-data[1][3][1]])],
				center=["55%", "70%"],
				radius=[60, 80],
				label_opts=new_label_opts(),
			)
			.set_global_opts(
				title_opts=opts.TitleOpts(title="JPN"),
				legend_opts=opts.LegendOpts(
					type_="scroll", pos_top="20%", pos_left="80%", orient="vertical"
				),
			)
		)
	# 英国
	c_cbr = (
		Pie(init_opts=opts.InitOpts(width="50%", height="400px"))
		.add(
			"",
			data[2],
			radius=["40%", "55%"],
			label_opts=opts.LabelOpts(
				position="outside",
				formatter="{a|{a}}{abg|}\n{hr|}\n {b|{b}: }{c}  {per|{d}%}  ",
				background_color="#eee",
				border_color="#aaa",
				border_width=1,
				border_radius=4,
				rich={
					"a": {"color": "#999", "lineHeight": 22, "align": "center"},
					"abg": {
						"backgroundColor": "#e3e3e3",
						"width": "100%",
						"align": "right",
						"height": 22,
						"borderRadius": [4, 4, 0, 0],
					},
					"hr": {
						"borderColor": "#aaa",
						"width": "100%",
						"borderWidth": 0.5,
						"height": 0,
					},
					"b": {"fontSize": 16, "lineHeight": 33},
					"per": {
						"color": "#eee",
						"backgroundColor": "#334455",
						"padding": [2, 4],
						"borderRadius": 2,
					},
				},
			),
		)
		.set_global_opts(title_opts=opts.TitleOpts(title="CBR"))
	)
	# 俄罗斯奥运队
	c_roc = (
		Pie(init_opts=opts.InitOpts(width="50%", height="400px"))
		.add(
			"",
			data[3],
			radius=["30%", "50%"],
			center=["50%", "50%"],
			rosetype="area",
		)
		.set_global_opts(title_opts=opts.TitleOpts(title="ROC"))
	)

	# 布局
	page = (
		Page(layout=Page.SimplePageLayout, page_title="各国擅长运动可视化")
		.add(c_usa, c_jpn, c_cbr, c_roc)
		.render('各国擅长的运动.html')
		)
	return page

# 数据处理
def medals_change_with_time():
	medal_type = ['golds', 'silvers', 'bronzes ']
	medals_data = []
	for m in medal_type:
		file = pd.ExcelFile(f'东京奥运会数据/{m}.xlsx')
		df = file.parse()
		df = df[~(df['日期'].isnull())]  # 删掉空行	
		countryids = ['USA','CHN','JPN','GBR','ROC']
		all_data =pd.DataFrame(columns=['日期'])
		for i in countryids:
			data = df[df['countryid']==f'{i}']
			data = pd.pivot_table(data, index=['日期'], columns=['countryid'], values=["名次"], aggfunc=[len])
			all_data = pd.merge(all_data, data, left_on='日期', right_on='日期',how='outer')
		all_data.columns = ['日期', 'USA','CHN','JPN','GBR','ROC']# 重命名列
		all_data.sort_values(by='日期',ascending=True, inplace=True)# 排序
		all_data = all_data.fillna(0)
		# all_data = all_data.T
		medals_data.append(all_data)
	return medals_data
	

# 数据可视化
def medals_change_with_view(data):
	a = medals_data[0].T
	b = medals_data[1].T
	c = medals_data[2].T
	a_temp_list = [14, 0, 1, 2, 3, 4, 15, 5, 6, 7, 8, 9, 10, 11, 12, 13]
	b_temp_list = [15, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
	c_temp_list = [13, 0, 14, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
	golds_num = [0, 0, 0, 0, 0]
	silvers_num = [0, 0, 0, 0, 0]
	bronzes_num = [0, 0, 0, 0, 0]
	golds_nums, silvers_nums,bronzes_nums = [], [], []
	for x in a_temp_list:
		golds_num = (np.array(golds_num)+np.array(a[x][1:])).tolist()
		# print(golds_num)
		golds_nums.append(golds_num)
	for y in b_temp_list:
		silvers_num = (np.array(silvers_num)+np.array(b[y][1:])).tolist()
		# print(silvers_num)
		silvers_nums.append(silvers_num)
	for z in c_temp_list:
		bronzes_num = (np.array(bronzes_num)+np.array(c[z][1:])).tolist()
		# print(bronzes_num)
		bronzes_nums.append(bronzes_num)
	bronzes_num = (np.array(bronzes_num)+np.array([0, 0, 0, 0, 0])).tolist()
	bronzes_nums.append(bronzes_num)

	tl = Timeline(init_opts=opts.InitOpts(width="100%", height="750px", page_title="东京奥运会奖牌榜"))
	# tl = Timeline()
	time_line = ['07-24','07-25','07-26','07-27','07-28','07-29','07-30','07-31','08-01','08-02','08-03','08-04','08-05','08-06','08-07','08-08']
	# print(time.strftime("%Y-%m-%d",time_line[0])
	for i in range(0,16):
		# 东京奥运会奖牌变化条形图
		bar = (
			Bar(init_opts=opts.InitOpts(chart_id=1))
			.add_xaxis(['USA','CHN', 'JPN','GBR','ROC'])
			.add_yaxis("金牌", golds_nums[i], label_opts=opts.LabelOpts(position="right"))
			.add_yaxis("银牌", silvers_nums[i], label_opts=opts.LabelOpts(position="right"))
			.add_yaxis("铜牌", bronzes_nums[i], label_opts=opts.LabelOpts(position="right"))
			.reversal_axis()
			.set_global_opts(
				title_opts=opts.TitleOpts("东京奥运会奖牌榜 (时间: 2021年)")
			)
		)
		# 仪表盘
		gauge =(
			Gauge()
			.add("", [("\n\n\n\n比赛进度", int((i/15)*100))], radius="50%")
		)
		# 布局
		grid_chart = (
			Grid()
			.add(
				bar, 
				grid_opts=opts.GridOpts(
					pos_left="35px", pos_right="60%", pos_top="10%",pos_bottom="1%"
				),
			)
			.add(
				gauge, 
				grid_opts=opts.GridOpts(
					pos_left="75%",pos_bottom="50%"
				),
			)

		)

		tl.add_schema(
			symbol='diamond',
			is_auto_play=True,
			orient="vertical",
			# play_interval=5000, 
			width="60",
			pos_left="null",
        	pos_right="10%",
        	pos_top="20",
        	pos_bottom="20"
        )
		tl.add(grid_chart, "{}".format(time_line[i]))
		tl.render('东京奥运会奖牌榜.html')
	return tl



if __name__ == "__main__":
	data = data_reading()
	page = good_projects_view(good_projects(data))
	medals_data = medals_change_with_time()
	tl = medals_change_with_view(medals_data)

			