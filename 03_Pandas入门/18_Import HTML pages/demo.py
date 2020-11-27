import pandas as pd

"""基本使用说明"""
'''
pd.read_html()
    io:字符串，文件路径，也可以是URL链接。网址不接受https，可尝试去掉https中的s再尝试。
'''
'''
    使用read_html方法前，首先要确定网页表格是否为table标签。例如，下列NBA网页中右键该网页中的表格，在弹出的菜单中选择"检查元素"
        查看是否含有表格标签<table>···</table>的字样。
'''
df = pd.DataFrame()
url_list = ['http://www.espn.com/nba/salaries/_/seasontype/4']
for i in range(2, 13):
    url = 'http://www.espn.com/nba/salaries/_/page/%s/seasontype/4' % i
    url_list.append(url)
# 遍历网页中的table读取网页表格数据
for url in url_list:
    df = df.append(pd.read_html(url), ignore_index=True)
# 列表解析：遍历dataframe第3列，以子字符串$开头
df = df[[x.startswith('$') for x in df[3]]]
print(df)
df.to_csv('../../data/0318.csv', header=['RK', 'NAME', 'TEAM', 'SALARY'], index=False)
