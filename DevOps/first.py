# 系统性能信息模块psutil
# 应用于系统监控，分析和限制系统资源及进程的管理
import psutil

# 1、获取系统性能信息
# CPU信息
print(psutil.cpu_times())
print(psutil.cpu_times().user)
# 获取CPU的逻辑个数，默认logical=True
print(psutil.cpu_count())
# 获取CPU的物理个数
print(psutil.cpu_count(logical=False))
