# _*_coding:utf-8 _*_
import json

import requests
import unittest

class GetStudentListTest(unittest.TestCase):

    #查询学生信息接口
    def setUp(self):
        self.url = 'http://127.0.0.1:8000/student_update/'

    def test_Student_null(self):
        #学生id为空
        r = requests.get(url, params= {'stuId':'0016'})
        r.content.decode("utf-8")
        print(r)
        results = r.json()
        res = json.dumps(results,indent= 4 , sort_keys= True, ensure_ascii= False)
        print(res)
        #断言接口返回值
        self.assertEqual(res['status'], 200)
        self.assertEqual(res['message'], 'success')

if __main__ == '__main__':
    unittest.main()