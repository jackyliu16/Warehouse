"""
Author： 刘逸珑
Time：   2021/7/21 23:22
"""
import time
import datetime
import Processingmodel

# timea = '2021/4/27', '2020/12/11', '2021/3/10', '2021/2/27', '2021/4/7'

'''好像可以对于时间代码进行一个简单的读取，最终将str转化成为一个datetime的数据类型'''
date_str = '2019/09/11'
# fmt = '%Y/%m/%d'
# time_tuple = time.strptime(date_str, fmt)
# year, month, day = time_tuple[:3]

# for i in timea:
#     a = date_str.split("/")[0]
#     b = date_str.split("/")[1]
#     c = date_str.split("/")[2]
#     a_date = datetime.date(a,b,c)
# print(a_date, type(a_date))
# print(a_date)

'''得出结论是可以对于结果进行一个简单的排列的'''
# timea = '2021/4/27', '2020/12/11', '2021/3/10', '2021/2/27', '2021/4/7'
# list1 = list(timea)
# print(list1)
# list1.sort(reverse=True)
# print(list1)



set1 = {'2020/12/19', '2021/2/8', '2021/4/10', '2020/12/22', '2021/1/6', '2020/12/4', '2021/1/5', '2021/3/9', '2021/2/7', '2021/4/7', '2020/12/25'}
# list1 = list(set1)
# print(list1)
# list1.sort(reverse=True)
# print(list1)
# a = list(set1).sort(reverse=True)
# print(a)


# dict = {'Name': 'Zara', 'Age': 7}
# for i in dict:
#     print(i)

list1 = ["1fuifq","$12","fewwg"]
print(list1[1])
list1[1].replace("$12","")
print(list1)
