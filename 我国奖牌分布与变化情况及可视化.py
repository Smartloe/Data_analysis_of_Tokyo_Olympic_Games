import pandas as pd

# 数据读取
def to_read_data():
	golds = pd.read_excel('东京奥运会数据/golds.xlsx')
	print(golds)
to_read_data()