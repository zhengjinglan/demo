# _*_encoding:'utf-8' _*_
import json

import requests
import time
import pandas
times = int(time.time() * 1000)
url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%{}'.format(times)
# print(times)
resturl = requests.get(url)
# print(resturl)
res = json.loads(resturl.json()['data'])
china_data = res['areaTree'][0]['children']
# print(china_data)
data_set = []
#遍历列表
for i in china_data:
    data_dict = {}
    #地区名称
    data_dict['province'] = i['name']
    #新增确诊人数
    data_dict['nowConfirm'] = i['total']['nowConfirm']
    #累计确诊
    data_dict['confirm'] = i['total']['confirm']
    #死亡
    data_dict['dead'] = i['total']['dead']
    #治愈
    data_dict['heal'] = i['total']['heal']
    #死亡率
    data_dict['deadRate'] = i['total']['deadRate']
    #治愈率
    data_dict['healRate'] = i['total']['healRate']
    data_set.append(data_dict)
print(data_set)
#保存
df = pandas.DataFrame(data_set)
print(df)
# df.to_csv(r'国内疫情数据.csv')

#可视化
from pyecharts import options as opts
from pyecharts.charts import Map

china_map = (
    Map()
    .add("现有确诊人数", [list(i) for i in zip(df['province'].values.tolist(),df['nowConfirm'].values.tolist())])
    .set_global_opts(
        title_opts= opts.TitleOpts(title="各省确诊人数", pos_top="48%", pos_left= "55%"),
        visualmap_opts= opts.VisualMapOpts(max_= 200, is_inverse= True),
        legend_opts= opts.LegendOpts(pos_left="90%", pos_top="60%"),
    )

)
china_map.render()
