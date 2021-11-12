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
def data_pre_processing(data):
	data[0] = data[0][~(data[0]['日期'].isnull())]  # 删掉空行
	print(data[0])
data_pre_processing(to_read_data())