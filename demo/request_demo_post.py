# -*-coding:utf-8 -*-
import requests
post_url = 'http://127.0.0.1:8000/api/add_student/'
payload2 = {
    'StuID':'20210630001', 'StuName':'张三', 'Sex':'男', 'BrithDate':'1996-08-08',
            'Native':'杭州', 'EntranceTime':'2002-09-01', 'politicalFee':'无',
            'PerPhone':'13811000011', 'IDnum':'412724199812125695', 'ClassID':'003',
            'DormitoryID':'301', 'National':'汉', 'EmploymcntStatus':'无',
            'HPhone':'13811000011', 'Address':'杭州'
}
r = requests.post(post_url, data= payload2, timeout = 1) #post请求传参数时，使用data关键字
# print('r.json()===', r.json())
print('r.status_code===', r.status_code)