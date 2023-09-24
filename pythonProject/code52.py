#import datetime
#from datetime import datetime
import datetime as dt
# 1.日期计算器
# 先构造datetime变量
# date1 = datetime.datetime(year=2020, month=12, day=24)
# date2 = datetime.datetime(year=2023, month=6, day=11)
# print(date2-date1)

# date1 = datetime(year=2020, month=12, day=24)
# date2 = datetime(year=2023, month=6, day=11)
# print(date2-date1)

date1 = dt.datetime(year=2020, month=12, day=24)
date2 = dt.datetime(year=2023, month=7, day=5)
print(date2-date1)