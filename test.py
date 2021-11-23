import pyecharts.options as opts
from pyecharts.charts import MapGlobe

data = [['United States', 113], ['China', 106], ['Japan', 58], ['United Kingdom', 65], ['Russia', 71], ['Australia', 46], ['Netherlands', 36], ['France', 33], ['Germany', 37], ['Italy', 40], ['Canada', 24], ['Brazil', 21], ['New Zealand', 20], ['Cuba', 15], ['Hungary', 20], ['Korea', 20], ['Poland', 14], ['Czech Rep.', 11], ['Kenya', 10], ['Norway', 8], ['Jamaica', 9], ['Spain', 17], ['Sweden', 9], ['Switzerland', 13], ['Denmark', 11], ['Croatia', 8], ['Iran', 7], ['Serbia', 9], ['Belgium', 7], ['Bulgaria', 6], ['Slovenia', 5], ['Uzbekistan', 5], ['Georgia', 8], ['Turkey', 13], ['Greece', 4], ['Uganda', 4], ['Ecuador', 3], ['Israel', 4], ['Ireland', 4], ['Qatar', 3], ['Kosovo', 2], ['Bahamas', 2], ['Ukraine', 19], ['Belarus', 7], ['Romania', 4], ['Venezuela', 4], ['India', 7], ['Philippines', 4], ['Slovakia', 4], ['South Africa', 3], ['Austria', 7], ['Egypt', 6], ['Indonesia', 5], ['Portugal', 4], ['Ethiopia', 4], ['Tunisia', 2], ['Estonia', 2], ['Thailand', 2], ['Fiji', 2], ['Latvia', 2], ['Bermuda', 1], ['Puerto Rico', 1], ['Morocco', 1], ['Colombia', 5], ['Azerbaijan', 7], ['Dominican Rep.', 5], ['Armenia', 4], ['Kyrgyzstan', 3], ['Mongolia', 4], ['Argentina', 3], ['SAN marino', 3], ['Jordan', 2], ['Malaysia', 2], ['Nigeria', 2], ['Turkmenistan', 1], ['North Macedonia', 1], ['Namibia', 1], ['Lithuania', 1], ['Bahrain', 1], ['Saudi Arabia', 1], ['Kazakhstan', 8], ['Mexico', 4], ['Finland', 2], ['Kuwait', 1], ["Côte d'Ivoire", 1], ['Ghana', 1], ['Syria', 1], ['Burkina Faso', 1], ['Grenada', 1], ['Moldova', 1], ['Botswana', 1]]
low, high = 0, 115

c = (
	MapGlobe(init_opts=opts.InitOpts(width="100%", height="750px", page_title='首页', bg_color='#2ca9e1'))
	.add_schema()

	.add(
		maptype="world",
		series_name="奥运奖牌分布图",
		data_pair=data,
		is_map_symbol_show=False,
		label_opts=opts.LabelOpts(formatter="{b}: {c}"),
	)
	.set_global_opts(
		visualmap_opts=opts.VisualMapOpts(
			min_=low,
			max_=high,
			range_text=["max", "min"],
			is_calculable=True,
			range_color=["pink", "lightskyblue", "yellow", "orangered"],
		),
		# tooltip_opts=opts.TooltipOpts(is_show=True, trigger_on='mousemove|click', background_color='whilte')
	)
	.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
	.render("map_globe_base.html")
)
