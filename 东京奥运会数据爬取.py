# 东京奥运会奖牌数据
import requests
import pandas as pd
url = 'https://sports.phb123.com/ay/55942.html'
headers = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36 Edg/95.0.1020.30'
}
response = requests.get(url=url,headers=headers)
response.encoding = "utf-8"  # 设置编码格式
if response.status_code == 200:
	page_data = pd.read_html(response.text)
	page_data[0].to_excel('东京奥运会奖牌数据.xlsx',index=False,header=None,encoding='utf-8')