# _*_coding:utf-8 _*_
"""
@Time    :2018/7/1 18:06
@Author  :weicm
#@Software: PyCharm
"""
# 复习随机函数 random 时间函数 time 的用法
import random,time


# 算法特性：输入，输出，有穷性，确定性，可行性  时间复杂度：基本运算数量总和是描述算法时间上的效率
# 最坏时间复杂度表示时间复杂度  最优时间复杂度是特殊情况
# 时间复杂度计算方法 只有常数项时间复杂度O(1)  顺序结构：加法  判断结构：取最大值  循环结构：乘法
#                     只取操作数量最高次项，其它次要项和常数项忽略，一般指最坏时间复杂度
# 题：a+b+c=1000,a**2+b**2 == c**2 求a,b,c
# 枚举法
print("="*20+"枚举法题目开始运行"+"="*20)
start = time.time()
#  外层循环决定要做1000次
for a in range(1001):
    #  内层循环决定要做1000次
    for b in range(1001):
        c = 1000-a-b
        # 需要执行四步也可以看成一步
        if a**2+b**2 == c**2:
            print("a,b,c:%d, %d ,%d"%(a,b,c))
# 时间复杂度 T = 1000*1000*1   T(n) = O(n*n)  运算过程中不需要分析的十分细致
# 大小关系  O(1)<O(logn)<O(n)<O(nlogn)<O(n^2)<O(n^3)<O(2^n)<O(n!)<O(n^n)
end = time.time()
use_time = end - start
print("use_time:%f"%use_time)



# random模块学习
print("="*20+"random模块开始运行"+"="*20)

# random.random()返回随机生成的一个实数，在(0,1)之间 不需要参数
a = random.random()
print("a:%f"%a)

# random.randint(a,b) 返回a到b之间的整数随机数
b = random.randint(0,10)
print("b:%d"%b)

# random.choice() 从序列中随机选择一个元素
d = "weicm"
c = random.choice(d)
print("c:%s"%c)

# random.randrange(1,100,2) 随机生成从1到100的间隔为2的随机整数
e = random.randrange(1,100,2)
print("e:%d"%e)

# random.uniform(1.1,5.4) 产生1.1到5.4之间的随机浮点数  区间内可以不是整数
f = random.uniform(1.1,5.4)
print("f:%f"%f)

# random.shuffle(a)将序列重新打乱
g = [1,2,3,4,5]
# 不需要赋值操作 只是对自身的操作
random.shuffle(g)
print(g)



# time模块学习
print("="*20+"time模块开始运行"+"="*20)

# time.time() 返回当前时间内的时间戳（1970年纪元后的浮点数-秒数）
now_time = time.time()
# 输出 now_time:1530444482.834074
print("now_time:%f"%now_time)

local_time = time.localtime(now_time)
# 输出 time.struct_time(tm_year=2018, tm_mon=7, tm_mday=1,
# tm_hour=19, tm_min=28, tm_sec=2, tm_wday=6, tm_yday=182, tm_isdst=0)
print(local_time)
print(local_time.tm_year)
print(local_time.tm_mon)

asc_time = time.asctime(local_time)
# 输出 asc_time:Sun Jul  1 19:28:02 2018
print("asc_time:"+asc_time)

# 总运行结果
"""
====================枚举法题目开始运行====================
a,b,c:0, 500 ,500
a,b,c:200, 375 ,425
a,b,c:375, 200 ,425
a,b,c:500, 0 ,500
use_time:0.826580
====================random模块开始运行====================
a:0.414469
b:5
c:e
e:9
f:2.245345
[2, 5, 3, 1, 4]
====================time模块开始运行====================
now_time:1530444614.268606
time.struct_time(tm_year=2018, tm_mon=7, tm_mday=1, tm_hour=19, tm_min=30, tm_sec=14, tm_wday=6, tm_yday=182, tm_isdst=0)
2018
7
asc_time:Sun Jul  1 19:30:14 2018
"""
