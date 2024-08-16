# 系统性能信息模块psutil
# 应用于系统监控，分析和限制系统资源及进程的管理
import datetime

import psutil

# 1.1.1获取系统性能信息
# CPU信息
print(psutil.cpu_times())
print(psutil.cpu_times().user)
# 获取CPU的逻辑个数，默认logical=True
print(psutil.cpu_count())
# 获取CPU的物理个数
print(psutil.cpu_count(logical=False))


# 内存信息
print(psutil.virtual_memory())
# 获取内存总数
print(psutil.virtual_memory().total)
# 获取空闲内存数
print(psutil.virtual_memory().free)
# 获取SWAP分区信息
print(psutil.swap_memory())

# 磁盘信息
# 获取磁盘完整信息
print(psutil.disk_partitions())
# 获取分区参数的使用情况
print(psutil.disk_usage("/"))
# 获取硬盘总的IO个数、读写信息
print(psutil.disk_io_counters())
# 获取单个分区IO个数、读写信息
print(psutil.disk_io_counters(perdisk=True))

# 网络信息
# 获取网络总的IO信息，默认pernic=False
print(psutil.net_io_counters())
# pernic=True输出每个网络接口的IO信息
print(psutil.net_io_counters(pernic=True))

# 其他系统信息
# 返回当前登录系统的用户信息
print(psutil.users())
# 获取开机时间
print(psutil.boot_time())
print(datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))



# 1.1.2系统进程管理方法