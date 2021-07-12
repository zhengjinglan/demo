# _*_encoding:'utf-8' _*_
import yaml

#yaml文件读取操作
file = open('test1.yaml', 'r', encoding='utf8')
res = yaml.load(file, Loader=yaml.FullLoader)
print(type(res))
for l in res:
    print(l)
    print(type(l))