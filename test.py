import datetime
import random

from pyecharts import options as opts
from pyecharts.charts import Calendar


begin = datetime.date(2021, 7, 24)
end = datetime.date(2021, 8, 8)
data = [
    [str(begin + datetime.timedelta(days=i)), random.randint(1000, 25000)]
    for i in range((end - begin).days + 1)
]

c = (
    Calendar()
    .add(
        "",
        data,
        calendar_opts=opts.CalendarOpts(
            range_="2021",
            daylabel_opts=opts.CalendarDayLabelOpts(name_map="cn"),
            monthlabel_opts=opts.CalendarMonthLabelOpts(name_map="cn"),
        ),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="Calendar-2021年微信步数情况(中文 Label)"),
        visualmap_opts=opts.VisualMapOpts(
            max_=20000,
            min_=500,
            orient="horizontal",
            is_piecewise=True,
            pos_top="230px",
            pos_left="100px",
        ),
    )
    .render("calendar_label_setting.html")
)
