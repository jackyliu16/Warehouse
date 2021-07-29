"""
Author： 刘逸珑
Time：   2021/7/21 22:08
"""
from Processingmodel import *
import csv

# ------------------------------------------------------------------------------
'''偷懒专用数据供给'''
Timeindex_a = 1
Timeindex_b = 0
Moneyindex_a = 4
Moneyindex_b = 5
#-------------------------------------------------------------------------------




print("""
本程序只能对于如2020/7/20和2020/7/20 20:26的时间(位于同一列）进行处理
同时对于CSV文件进行导入
""")
print("第一步，我们将进行主数据【自己记录的数据】导入")
#qianjiname = input("请输入你记录的账本名称\n >")
qianjiname = "Qian_Ji_日常生活_2021-07-21_151916.csv"

'''钱迹文件导入'''
csvFile = open(qianjiname,"r",encoding="utf-8")
csvFile.seek(3)                                         # 这个其实是为了解决不知道为什么在文本前面出现的奇怪语句
reader = csv.reader(csvFile)
a = list(reader)

'''还没想出来的index获取'''
# Timeindex_a = int(input("请输入你的文件中Time所在的列数\n>"))-1
# Moneyindex_a = int(input("请输入你的文件中Money所在的列数\n>"))-1

'''对于数据进行一个简单的清洗'''
if ':' in a[2][Timeindex_a] :
    a = num_clear(a,Timeindex_a)
    Timeindex_a = -1
    Moneyindex_a -= 1

"""最终将钱迹所提供的数据进行一个简单的排列，使Date作为Key，然后当天消费额度作为value"""
Dict_qianji,DatePay_qianji = Process_Data(a,Timeindex_a,Moneyindex_a)


# -------------------------------------------------------------------------------
print("第二部我们进行第二个文档的导入")

# ReconciliationName = input("请输入第二个文件名称：")
ReconciliationName = '微信支付账单(20210501-20210721).csv'

csvFile = open(ReconciliationName,"r",encoding="utf-8")
csvFile.seek(3)
reader = csv.reader(csvFile)
b = list(reader)

'''index获取'''
# Timeindex_b = int(input("请输入你的第二个文件中Time所在的列数\n>"))-1
# Moneyindex_b = int(input("请输入你的第二个文件中Money所在的列数\n>"))-1

'''对于数据进行一个简单的清洗'''
if ':' in b[2][Timeindex_b] :
    b = num_clear(b,Timeindex_b)
    Timeindex_b = -1
    Moneyindex_b -= 1
    '''这个Moneyindex在转化成为编程要求的0开始外还减多了一个1原因是受到pop的影响'''


"""最终将钱迹所提供的数据进行一个简单的排列，使Date作为Key，然后当天消费额度作为value"""
Dict_bank,DatePay_bank = Process_Data(b,Timeindex_b,Moneyindex_b)


# print("您的第一个文件中的数据清单",Dict_qianji)
# print("您的第二个文件中的数据清单",Dict_bank)


'''对于两个不同文件中的交易日进行一个简单的求差集
这个地方需要考虑一个问题就是时间的最大最小限制，但是看了下Datetime和time相关的库有点没有很能弄明白这个是咋进行才可以对于最大最小进行一个简单的判定'''
ErrorA2B,ErrorB2A,SamePayDay = compareset(DatePay_qianji,DatePay_bank)
print("A账本没有记录的B账本中的交易日为:",ErrorA2B)
print("B账本没有记录的A账本中的交易日为:",ErrorB2A)
ErrorPay = {}


'''这个部分的想法是通过遍历的方式诸葛从list中遍历元素，来确保其确实是存在的'''
for i in SamePayDay:
    print("-----------------------------------------------------------")
    print(i,Dict_bank.get(i))
    print(i,Dict_qianji.get(i))
    for things in  Dict_bank.get(i):
        if things in Dict_qianji.get(i):
            pass
        elif ErrorPay.get(i,"None") == "None":
            ErrorPay[i] = [things]
        elif ErrorPay.get(i,"None") != "None":
            ErrorPay[i].append(things)
    # print(ErrorPay)




'''这个地方是对于内容的逐项判断'''
'''首先是对于交易日残缺的进行判断'''



    # if Dict_bank.get(i).sort() == Dict_qianji.get(i).sort():
    #     print("YES")
    # else:
    #     print("wrong")
    # else:
    #     for EC in Dict_bank.get(i):
    #         if EC in Dict_qianji:
    #             pass
    #         elif ErrorPay.get(EC,"None") != "None":
    #             ErrorPay[i] = EC
    #         elif ErrorPay.get(EC,"None") == "None":
    #             ErrorPay[i].append(EC)






