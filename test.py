# -*- coding: utf-8 -*-

# @File    : test.py
# @Date    : 2020-08-11
# @Author  : CuiMin

import time

ticks = time.time()
print("now time:", ticks)

# 获取当时时间
localtime = time.localtime(time.time())
print("本地时间：", localtime)

# 格式化时间
localtime = time.asctime(time.localtime(time.time()))
print("本地时间：", localtime)

##############  常用时间  #######################
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))

print(time.perf_counter())  # 返回系统时间

time.sleep(secs=5)  # 推迟调用线程的运行，secs为秒
