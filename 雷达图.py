import pandas as pd
import json
from pyecharts import options as opts
from pyecharts.charts import Radar


# 数据读取
def data_reading():
	# 读取Excel文件
	file = pd.ExcelFile('东京奥运会数据/national_medal.xlsx')
	data = file.parse()
	data = data.head()
	golds = data['金牌'].to_list()
	silvers = data['银牌'].to_list()
	bronzes = data['铜牌'].to_list()
	data = [
		[{"value": [golds[0],silvers[0], bronzes[0],], "name": data['国家'][0],}],
		[{"value": [golds[1],silvers[1], bronzes[1],], "name": data['国家'][1],"symbol": 'rect',"symbolSize": 12,"lineStyle": {"type": 'dashed'},}],
		[{"value": [golds[2],silvers[2], bronzes[2],], "name": data['国家'][2]}],
		[{"value": [golds[3],silvers[3], bronzes[3],], "name": data['国家'][3]}],
		[{"value": [golds[4],silvers[4], bronzes[4],], "name": data['国家'][4]}],
	]
	return data


# 雷达图
def radar_chart(medals_data):
	c_schema = [
		{"name": "金牌", "max": 45, "min": 0},
		{"name": "银牌", "max": 45, "min": 0},
		{"name": "铜牌", "max": 45, "min": 0},
	]
	radar = Radar(init_opts=opts.InitOpts(width="100%",height="750px", page_title='雷达图'))
	radar.add_schema(
			schema=c_schema,
			shape="circle",
			center=["50%", "50%"],
			radius="80%",
			angleaxis_opts=opts.AngleAxisOpts(
				min_=0,
				max_=360,
				is_clockwise=False,
				interval=5,
				axistick_opts=opts.AxisTickOpts(is_show=False),
				axislabel_opts=opts.LabelOpts(is_show=False),
				axisline_opts=opts.AxisLineOpts(is_show=False),
				splitline_opts=opts.SplitLineOpts(is_show=False),
			),
			radiusaxis_opts=opts.RadiusAxisOpts(
				min_=0,
				max_=45,
				interval=9,
				splitarea_opts=opts.SplitAreaOpts(
					is_show=True, 
					areastyle_opts=opts.AreaStyleOpts(opacity=0.8,color=['#f7ede2', '#f6bd60', '#f5cac3', '#f28482', '#84a59d', ],)
				),
			),
			polar_opts=opts.PolarOpts(),
			splitarea_opt=opts.SplitAreaOpts(is_show=False),
			splitline_opt=opts.SplitLineOpts(is_show=False),
		)
	radar.add(
			series_name="USA",
			color="#003049",
			data=medals_data[0],
			areastyle_opts=opts.AreaStyleOpts(opacity=0.1),
			linestyle_opts=opts.LineStyleOpts(width=2),
		)
	radar.add(
			series_name="CHN",
			color="red",
			data=medals_data[1],
			areastyle_opts=opts.AreaStyleOpts(opacity=0.3),
			linestyle_opts=opts.LineStyleOpts(width=5),
		)
	radar.add(
			series_name="JPN",
			color="#000000",
			data=medals_data[2],
			areastyle_opts=opts.AreaStyleOpts(opacity=0.1),
			linestyle_opts=opts.LineStyleOpts(width=2),
		)
	radar.add(
			series_name="GBR",
			color="#000000",
			data=medals_data[3],
			areastyle_opts=opts.AreaStyleOpts(opacity=0.1),
			linestyle_opts=opts.LineStyleOpts(width=2),
		)
	radar.add(
			series_name="ROC",
			color="#000000",
			data=medals_data[4],
			areastyle_opts=opts.AreaStyleOpts(opacity=0.1),
			linestyle_opts=opts.LineStyleOpts(width=2),
		)
	radar.render("雷达图.html")



if __name__ == "__main__":
	data = data_reading()
	radar_chart(data)