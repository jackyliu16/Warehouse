"""
Author： 刘逸珑
Time：   2021/7/21 16:10
"""
'''似乎是CSV文件的标准导入流程?'''
import csv
csvFile = open("qianji.csv","r",encoding="utf-8")
csvFile.seek(3)                                         # 这个其实是为了解决不知道为什么在文本前面出现的奇怪语句
reader = csv.reader(csvFile)
a = list(reader)

'''去除原始数据中有关于时间的相关内容'''
for i in a:
    i.append(i[0].split(' ')[0])
    i.pop(0)
    '''这个地方的想法应该是'''
    # print(i)#

Date_Pay = set(i[1] for i in a )
# print(Date_Pay)         #这个地方的作用是生成一个日期集合，方便我就每天进行交易的次数以及金额数目进行核对

DictPay = {}            #这个是我最终整理出的Dict，大概结果是Dict = { day1:["103,0",'12.4','4'],day2 : ["12.0"]...}
for Date in Date_Pay:                                                           # 从set（Date_Pay)中的每一个进行循环
    for Date_list in a:                                                         # 对于列表进行循环判断Date是否在其中
        # print(Date)
        # print(Date_list)
        # print("--------------------------------------")
        if Date in Date_list and DictPay.get(Date,"None") == "None" :
            '''if Date in Date_list 的作用是判断这个list是否是set中我们所选取的那个日子所对应的list
            然后DictPay.get(Date,"None")判断的是DictPay中是否已经建立了对应的key
            如果已经建立了，那么就直接对于其进行一个list.append 的处理，否则创建key:value'''
            DictPay[Date] = [Date_list[0]]                                        # 将Date作为key，支付金额作为Value
            # print(DictPay)
            # print(DictPay[Date])
        elif Date in Date_list and DictPay.get(Date,"None") != "None":
            DictPay[Date].append(Date_list[0])
            # print(DictPay[Date])
        else:
            continue
print(DictPay)
