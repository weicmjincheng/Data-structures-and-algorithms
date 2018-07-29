# _*_coding:utf-8 _*_
"""
@Time    :2018/7/1 21:37
@Author  :weicm
#@Software: PyCharm
"""
from timeit import Timer

# li1 = [1,2]
# li2 = [23,5]
# li3 = [24,6]
# li1.append(li2)
# # append 相当于添加一个整体对象放到原有的后面
# print(li1)  # [1, 2, [23, 5]]
# # extend 相当于将对象当中的内容添加到列表后
# li3.extend(li2)
# print(li3) # [24, 6, 23, 5]
#
# li = li1+li2
# # 列表生成器
# li4 = [i for i in range(10000)]
# print(li4)
# # py2当中返回列表对象，py3当中返回可迭代对象  py2要是如果要返回可迭代对象用xrange()
# # 把可迭代对象转成列表
# li5 = list(range(10000))
# print(li5)

li6 = []
for _ in range(10000):
    li6.append(_)


def test1():
    li6 = []
    for _ in range(10000):
        li6.append(_)


def test2():
    li7 = []
    for _ in range(10000):
        li7 += [_]


def test3():
    li8 = [i for i in range(10000)]


def test4():
    li5 = list(range(10000))


def test5():
    li9 = []
    for i in range(10000):
        li9.extend([i])


def test6():
    li10 = []
    for i in range(10000):
        li10.insert(0,i)
        # 制定从头部添加元素


"""
timeit 模块中的三个函数

    timeit.timeit(stmt='pass', setup='pass', timer=<default timer>, number=1000000)：创建一个Timer实例，参数分别是stmt（需要测量的语句或函数），setup（初始化代码或构建环境的导入语句），timer（计时函数），number（每一次测量中语句被执行的次数）
    timeit.repeat(stmt='pass', setup='pass', timer=<default timer>, repeat=3, number=1000000)：创建一个Timer实例，指定整个试验的重复次数，返回一个包含了每次试验的执行时间的列表，利用这一函数可以很方便得实现多次试验取平均的方法。
    timeit.default_timer()：默认的计时器，一般是time.perf_counter()，time.perf_counter()方法能够在任一平台提供最高精度的计时器（它也只是记录了自然时间，记录自然时间会被很多其他因素影响，例如计算机的负载）
"""

timer1 = Timer("test1()","from __main__ import test1")
# 执行1000次并打印花费平均时间
print("test1所要花费的时间是：%f"%timer1.timeit(1000))

timer1 = Timer("test2()","from __main__ import test2")
# 执行1000次并打印花费平均时间
print("test2所要花费的时间是：%f"%timer1.timeit(1000))

timer1 = Timer("test3()","from __main__ import test3")
# 执行1000次并打印花费平均时间
print("test3所要花费的时间是：%f"%timer1.timeit(1000))

timer1 = Timer("test4()","from __main__ import test4")
# 执行1000次并打印花费平均时间
print("test4所要花费的时间是：%f"%timer1.timeit(1000))

timer1 = Timer("test5()","from __main__ import test5")
# 执行1000次并打印花费平均时间
print("test5所要花费的时间是：%f"%timer1.timeit(1000))

timer1 = Timer("test6()","from __main__ import test6")
# 执行1000次并打印花费平均时间
print("test6所要花费的时间是：%f"%timer1.timeit(1000))