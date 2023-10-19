# 实现一个命令版本的学生管理系统
import os.path
import sys
# 使用这个全局变量来管理学生
# 这个列表的每一个元素都是一个字典 每个字典分别表示了一个同学
students = []

def save():
    """
    用于存档
    """
    # 此处的路径不是"绝对路径" D:// 而是相对路径
    # 此处这个写法的含义就是让record.txt的路径和code58.py在同一目录下
    with open('record.txt', 'w', encoding='utf8') as f:
        for s in students:
            f.write(f"{s['studentId']}\t{s['name']}\t{s['gender']}\t{s['className']}\n")
        print(f'存档成功,共存储了{len(students)}条记录')

def load():
    # 用于读档
    # 如果存档文件不存在,则直接跳过存档程序
    # 为了避免读方式打开文件的时候,文件不存在异常
    # 用于路径上的判定
    if not os.path.exists('record.txt'):
        return
    # 读档的时候要先把旧的清理干净
    global students
    # 清空
    students = []
    with open('record.txt', 'r', encoding='utf8') as f:
        for line in f:
            # 针对这行数据 按照\t进行切分
            # 切分之前要去除末尾的换行
            # 这个方法去掉字符串开头末尾的空白符(空格 回车 换行 制表...)
            line = line.strip()
            tokens = line.split('\t')
            if len(tokens) != 4:
                print('当前行格式存在问题,'f'line={line}')
                continue
            student = {
                 'studentId': tokens[0],
                 'name': tokens[1],
                 'gender': tokens[2],
                 'className': tokens[3]
             }
            students.append(student)
        print(f'读档成功共读取了{len(students)}条记录')

def menu():
    print('1.新增学生')
    print('2.显示学生')
    print('3.查找学生')
    print('4.删除学生')
    print('0.退出程序')
    choice = input('请输入您的选项:')
    return choice

def insert():
    print('[新增学生] 开始!')
    studentId = input('请输入学生的学号: ')
    name = input('请输入学生的姓名: ')
    gender = input('请输入学生的性别: ')
    if gender not in ('男', '女'):
        print('您的性别输入有误!新增失败')
        return
    className = input('请输入学生的班级: ')
    # 使用一个字典把上述的信息聚合起来
    student = {
        'studentId': studentId,
        'name': name,
        'gender': gender,
        'className': className
    }
    # 声明全局变量
    global students
    students.append(student)
    # 增加一个保存
    save()
    print('[新增学生] 完毕!')

def show():
    # 遍历全局变量的列表,把每个学生的信息打印出来
    print('[显示学生] 开始!')
    for s in students:
        print(f"[{s['studentId']}]\t{s['name']}\t{s['gender']}\t{s['className']}")
    print(f'[显示学生] 完毕! 共显示了{len(students)}条数据')

def find():
    print('[查找学生] 开始!')
    name = input('请输入您要查找的学生姓名: ')
    count = 0
    for s in students:
        if name == s['name']:
            print(f"[{s['studentId']}]\t{s['name']}\t{s['gender']}\t{s['className']}")
            count += 1
    print(f'查找学生结束!共找到了{count}个匹配的学生!')
    print('[查找学生] 结束!')

def delete():
    print('[删除学生] 开始!')
    studentId = input('请输入您要输入的学生学号: ')
    # 看看这个学生对应的是哪个字典,然后在字典中进行对应的删除
    for s in students:
        if studentId == s['studentId']:
            print(f"删除{s['name']}同学的信息!")
            students.remove(s)
    save()
    print('[删除学生] 结束!')

def main():
    """
    入口函数
    """

    # 通过控制台和用户交互
    print('-----------------------------')
    print('     欢迎来到学生管理系统      ')
    print('-----------------------------')
    load()
    while True:
        # 通过menu函数打印出菜单项
        choice = menu()
        if choice == '1':
        # 新增学生
            insert()
        elif choice == '2':
        # 显示学生
            show()
        elif choice == '3':
        # 查找学生
            find()
        elif choice == '4':
        # 删除学生
            delete()
        elif choice == '0':
        # 退出程序
            print('goodbye')
            sys.exit(0)
        else:
            print('您的输入有误请重新输入')


main()

