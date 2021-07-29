"""
Author： 刘逸珑
Time：   2021/7/21 21:32
"""


# IndexOfTime = 1
# IndexOfMoney = 4
# is_time_include_min = True
# nameoftable = a

# class Data_Processing(object):
#     def __init__(self,nameoftable):
#         Data_Processing.a = nameoftable
#         # Data_Processing.Timeindex = IndexOfTime
#         # Data_Processing.Moneyindex = IndexOfMoney
#         # Data_Processing.includemin = is_time_include_min
#
#     def ProcessingTime(self,is_time_include_min):
#         if is_time_include_min == True:
#             for i in Data_Processing.a:
#                 i.append(i[0].split(' ')[0])
#                 i.pop(0)
#         else:
#             pass
#
#     def ProcessData(self):
#         Date_Pay = set(i[1] for i in a)
#         DictPay = {}
#         for Date in Date_Pay:
#             for Date_list in Data_Processing.a:
#                 if Date in Date_list and DictPay.get(Date,"None") == "None":
#                     DictPay[Date] = [Date_list[IndexOfTime]]
#                 elif Date in Date_list and DictPay.get(Date,"None") != "None":
#                     DictPay[Date].append(Date_list[0])
#                 else:
#                     continue
#         return DictPay




'''
nest:等同于CSV导出的嵌套list
'''

def num_clear(nest,Timeindex):
    if " " in nest[1][Timeindex]:
        for i in nest:
            i.append(i[Timeindex].split(' ')[0])
            i.pop(Timeindex)

    '''本来尝试想通过list[Moneyindex]对于整个功能进行一个简单的replace（“￥”，“）
    但是不知道为什么没有办法对于list中的元素进行这个replace'''
    # if "$" in nest[1][Moneyindex]:
    #     for i in nest:
    #         i.replace

    return nest

def Process_Data(nest,Timeindex,Moneyindex):
    Date_Pay = set(i[Timeindex] for i in nest)
    '''对于发生交易的天数进行一个简单的集合处理，使之存在唯一'''
    DictPay = {}
    for Date in Date_Pay:
        for Date_list in nest:
            if Date in Date_list and DictPay.get(Date, "None") == "None":
                '''进行两部判定，第一步，判断set中所存在的交易日具体在nest的哪个index上的list中
                【这个地方不需要得到index】，然后对于我们是否已经创建了当天的字典进行一个判断
                如果没有创建这个字典则进行创建，如果已经创建了，就在原先所有的list后用append的方法
                添加新元素'''
                DictPay[Date] = [Date_list[Moneyindex]]
            elif Date in Date_list and DictPay.get(Date, "None") != "None":
                DictPay[Date].append(Date_list[Moneyindex])
            else:
                continue
    return DictPay,Date_Pay

def compareset(a,b):
    '''这个地方本来打算尝试一下使用datetime，和time两个模块来进行一个简单的比较的'''
    Error_DatePay_a = a - b
    Error_DatePay_b = b - a
    SamePayDay = a & b

    Error_DatePayA = list(Error_DatePay_a)
    Error_DatePayB = list(Error_DatePay_b)

    Error_DatePayA.sort(reverse=True)
    Error_DatePayB.sort(reverse=True)

    return Error_DatePayA,Error_DatePayB,SamePayDay


# Error_DatePay_a = list(a - b).sort(reverse=True)
#     Error_DatePay_b = list(b - a).sort(reverse=True)