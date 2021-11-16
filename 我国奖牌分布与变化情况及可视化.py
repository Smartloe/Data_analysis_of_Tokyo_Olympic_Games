import pandas as pd

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


# 可视化part1：折线图
def line_chart(data):
	# 透视数据
	df_p1 = data[0].pivot_table(index='日期',    # 透视的行，分组依据
						  values='名次',    # 值
						  aggfunc='sum'    # 聚合函数
						 )
	df_p2 = data[1].pivot_table(index='日期',    # 透视的行，分组依据
						  values='名次',    # 值
						  aggfunc='sum'    # 聚合函数
						 )
	df_p3 = data[2].pivot_table(index='日期',    # 透视的行，分组依据
						  values='名次',    # 值
						  aggfunc='sum'    # 聚合函数
						 )
	print(df_p3)



if __name__ == "__main__":
	line_chart(data_pre_processing())
