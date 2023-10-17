import xlrd

# 1.先打开xlsx文件
xlsx = xlrd.open_workbook('E:/Python环境/test.xlsx')
# 2.获取到指定的标签页  根据下标确定
table = xlsx.sheet_by_index(0)
# 3.获取到表格中有多少行
nrows = table.nrows
# 4.进行循环统计操作
total = 0
count = 0
for i in range(1, nrows):
    # 拿到当前同学的班级id
    classId = table.cell_value(i, 1)  # 第一行是班级
    if classId == 100:
        total += table.cell_value(i, 2) # 第二行是分数
        count += 1
print(f'总成绩={total}')
print(f'总人数={count}')
print(f'平均分={total/count}')