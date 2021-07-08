# -*-coding:utf-8 -*-
import requests
import json

class RunMain:
    def send_get(self, url, data):
        res = requests.get(url= url, params= data)
        print('res=====',res)
        return res

    def send_post(self, url, data):
        res = requests.post(url= url, data= data).json()
        return res

    def run_main(self, url, method, data = None):
        print('2222222222')
        res = None
        print('11111111111')
        if method == 'GET':
            res = self.send_get(url, data)
        else:
            res = self.send_post(url, data)

        return res

if __name__ == '--main__':
    # url = 'http://192.168.0.53:7001/CommonService/api/control/controlProgress/query.v'
    url = 'http://127.0.0.1:8000/student_manage/'
    data = {
        'stuId': '2021062910'
    }
    run = RunMain() #实例化时不需要带参数
    results = run.run_main(url, 'GET')
    print(results)