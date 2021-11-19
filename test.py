from pyecharts import options as opts
from pyecharts.charts import PictorialBar

location = ["山西", "四川", "西藏", "北京", "上海", "内蒙古", "云南", "黑龙江", "广东", "福建"]
values = [13, 42, 67, 81, 86, 94, 166, 220, 249, 262]



c = (
    PictorialBar()
    .add_xaxis(location)
    .add_yaxis(
        "",
        values,
        label_opts=opts.LabelOpts(is_show=False),
        symbol_size=22,
        symbol_repeat="fixed",
        symbol_offset=[0, -5],
        is_symbol_clip=True,
        symbol='image://data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBzdGFuZGFsb25lPSJubyI/PjwhRE9DVFlQRSBzdmcgUFVCTElDICItLy9XM0MvL0RURCBTVkcgMS4xLy9FTiIgImh0dHA6Ly93d3cudzMub3JnL0dyYXBoaWNzL1NWRy8xLjEvRFREL3N2ZzExLmR0ZCI+PHN2ZyB0PSIxNjM3MzEyODI3MDk5IiBjbGFzcz0iaWNvbiIgdmlld0JveD0iMCAwIDEwMjQgMTAyNCIgdmVyc2lvbj0iMS4xIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHAtaWQ9IjI4MTciIHhtbG5zOnhsaW5rPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5L3hsaW5rIiB3aWR0aD0iMjAwIiBoZWlnaHQ9IjIwMCI+PGRlZnM+PHN0eWxlIHR5cGU9InRleHQvY3NzIj48L3N0eWxlPjwvZGVmcz48cGF0aCBkPSJNODA2LjQgMjY4LjhjNjMuNiAwIDExNS4yIDUxLjYgMTE1LjIgMTE1LjJTODcwIDQ5OS4yIDgwNi40IDQ5OS4yIDY5MS4yIDQ0Ny42IDY5MS4yIDM4NHM1MS42LTExNS4yIDExNS4yLTExNS4yTTE0OS4yIDQxNy44bDI0Mi0xMTAuMUw0NTcuNSA0NTUgMTI4IDY1Mi44aDYyMS44bC0yOTcuNi00MzhjLTEzLjktMjAuOS00MC45LTI4LjYtNjMuOC0xOC4ybC0yODEuNiAxMjhjLTI2LjEgMTAuOS0zOC40IDQwLjktMjcuNSA2NyAxMC45IDI2LjEgNDAuOSAzOC40IDY3IDI3LjUgMS0wLjQgMS45LTAuOSAyLjktMS4zeiIgZmlsbD0iI0ZGQkE1NyIgcC1pZD0iMjgxOCI+PC9wYXRoPjxwYXRoIGQ9Ik0xMDI0IDYyNy4yYy00MSAzLjItODAuNC0xNi41LTEwMi40LTUxLjItMjIgMzQuNy02MS40IDU0LjQtMTAyLjQgNTEuMi00MSAzLjItODAuNC0xNi41LTEwMi40LTUxLjItMjIgMzQuNy02MS40IDU0LjQtMTAyLjQgNTEuMi00MSAzLjItODAuNC0xNi41LTEwMi40LTUxLjItMjIgMzQuNy02MS40IDU0LjQtMTAyLjQgNTEuMi00MSAzLjItODAuNC0xNi41LTEwMi40LTUxLjItMjIgMzQuNy02MS40IDU0LjQtMTAyLjQgNTEuMi00MSAzLjItODAuNC0xNi41LTEwMi40LTUxLjJDODAuNCA2MTAuNyA0MSA2MzAuNCAwIDYyNy4yVjgzMmgxMDI0VjYyNy4yeiIgZmlsbD0iIzdFOENDRiIgcC1pZD0iMjgxOSI+PC9wYXRoPjxwYXRoIGQ9Ik0xMDI0IDY3OC40Yy00MSAzLjItODAuNC0xNi41LTEwMi40LTUxLjItMjIgMzQuNy02MS40IDU0LjQtMTAyLjQgNTEuMi00MSAzLjItODAuNC0xNi41LTEwMi40LTUxLjItMjIgMzQuNy02MS40IDU0LjQtMTAyLjQgNTEuMi00MSAzLjItODAuNC0xNi41LTEwMi40LTUxLjItMjIgMzQuNy02MS40IDU0LjQtMTAyLjQgNTEuMi00MSAzLjItODAuNC0xNi41LTEwMi40LTUxLjItMjIgMzQuNy02MS40IDU0LjQtMTAyLjQgNTEuMi00MSAzLjItODAuNC0xNi41LTEwMi40LTUxLjJDODAuNCA2NjEuOSA0MSA2ODEuNiAwIDY3OC40VjgzMmgxMDI0VjY3OC40eiIgZmlsbD0iI0M1Q0FFOSIgcC1pZD0iMjgyMCI+PC9wYXRoPjwvc3ZnPg==',
    )
    .reversal_axis()
    .set_global_opts(
        title_opts=opts.TitleOpts(title="PictorialBar-自定义 Symbol"),
        xaxis_opts=opts.AxisOpts(is_show=False),
        yaxis_opts=opts.AxisOpts(
            axistick_opts=opts.AxisTickOpts(is_show=False),
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(opacity=0)
            ),
        ),
    )
    .render("pictorialbar_custom_symbol.html")
)
