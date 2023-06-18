import random

#人生重开模拟器
import sys
import time

print('+------------------------------------+')
print('|                                    |')
print('|     花有重开日,人无在少年            |')
print('|                                    |')
print('|   欢迎来到人生重开模拟器             |')
print('|                                    |')
print('+------------------------------------+')

#设置初始属性
#颜值 体质 家境 智力 总和不能超过20 每一项取值都是在1-10之间

#使用循环,玩家在输入错误的时候可以重新输入
while True:
    print('请设置初始属性(可用点数总数为20)')
    face = int(input('请输入颜值(1-10):'))
    strong = int(input('请输入体质(1-10):'))
    iq = int(input('请输入智力(1-10):'))
    home = int(input('请输入家境(1-10):'))
    #对用户输入的内容进行校验 通过条件语句进行校验检查
    #此时使用if continue和elif功能类似
    if face < 1 or face > 10:
        print('颜值输入错误,请重新输入')
        continue

    if strong < 1 or strong > 10:
        print('体质设置有误,请重新输入')
        continue

    if iq < 1 or iq > 10:
        print('智力设置有误,请重新输入')
        continue

    if home < 1 or home > 10:
        print('家境输入有误,请重新输入')
        continue

    if (face + strong + iq + home) > 20:
        print('总的属性和超过20,请重新输入')
        continue

    #代码走到这个位置的时候,表示用户的输入全部是正确的
    print('初始属性输入完毕!')
    print(f'颜值:{face}、体质:{strong}、智力:{iq}、家境:{home}')
    break  #跳出当前循环

#生成角色的性格
#使用random.randint(beg,int),就能生成[beg,int]的随机整数
point = random.randint(1,6)
# print(f'point={point}')
if point % 2 == 1:
    gender = 'boy'
    print('你是个男孩儿')
else:
    gender = 'girl'
    print('你是个女孩儿')

#家境+随机数
#家境10 第一档 属性加成
#家境7-9 第二档 也会属性加成
#家境4-6 第三档 少属性加成
#家境1-3 第四档 扣属性

#设定角色的出生点
#为了简单,直接生成一个[1,3]的随机数
point = random.randint(1,3)
if home == 10:
    #第一档
    print('你出生在帝都,你的父母都是高管政要:')
    home += 1
    iq += 1
    face += 1
elif 7 <= home <= 9:
    #第二档
    if point == 1:
        print('你出生在大都市,父母是公务员')
        face += 2
    elif point == 2:
        print('你出生在大都市,父母是企业高管')
        home += 2
    else:
        print('你出生在大都市,父母是大学教授')
        iq += 2
elif 4 <= home <= 6:
    #第三档
    if point == 1:
        print('你出生在三线城市,父母都是医生')
        strong += 1
    elif point == 2:
        print('你出生在镇上,父母都是老师')
        iq += 1
    else:
        print('你出生在镇上,父母是个体户')
        home += 1
else:
    #第四档
    if point == 1:
        print('你出生在农村,父母都是农民')
        strong += 1
        face -= 2
    elif point == 2:
        print('你出生在穷乡僻壤,父母是无业游民')
        home -= 1
    else:
        print('你出生在镇上,父母离异')
        strong -= 1
print(f'颜值{face} 体质{strong} 智力{iq} 家境{home}')

#幼年阶段 [1,10] 可塑性强
#青年阶段 [11,20] 求学
#壮年阶段 [20,50] 平稳
#老年阶段50以上 颜值和体质和智力显著退化

#幼年阶段
for age in range(1,11):
    #把一整年的打印都整理到一个字符串中,在这一年的结尾统一打印
    info = f'你今年{age}岁'
    #生成一个[1,3]的随机整数
    point = random.randint(1,3)
    #性别触发的事件
    if gender == 'girl' and home <= 3 and point == 1:
        info += f'你的家里重男轻女的思想比较严重.你被遗弃了!'
        print(info)
        print('游戏结束')
        sys.exit(0)
    #体质触发的事件
    #使用elif是保证每年只触发一共事件
    elif strong < 6 and point < 3:
        info += f'你生了一场病'
        if home >= 5:
            info += f'在父母的精心照顾下,你康复了'
            strong += 1
            home -= 1
        else:
            info += f'你的父母没精力管你,你的情况更糟糕了'
            strong -= 1
    #颜值触发的事件
    elif face <= 4 and age >= 7:
        info += f'你长的太丑了,别的小朋友不喜欢你'
        if iq > 5:
             info += f'你决定用学习填充自己'
        else:
            if gender == 'boy':
                info += f'你和别的小朋友经常打架'
                strong += 1
                iq -= 1
            else:
                info += f'你经常被别的小孩欺负'
                strong -= 1
    #通过智商触发的事件
    elif iq < 5:
        info += f'你看起来傻傻的'
        if home >= 8 and age >= 6:
            info += f'你的父母把你送到更好的学校学习'
            iq += 1
        elif 4 <= home <= 7:
            if gender =='boy':
                info += f'你的父母鼓励你多运动,成为一名运动员'
                strong += 1
            else:
                info += f'你的父母鼓励你多打扮自己'
                face += 1
        else:  #家境不好的人
            info += f'你的父母为此经常吵架'
            if point == 1:
                strong -= 1
            elif point == 2:
                iq -= 1
            else:
                pass
    #健康成长事件
    else:
        info += f'你健康成长'
        if point == 1:
            info += f'你看起来更结实了'
            strong += 1
        elif point == 2:
            info += f'你更好看了'
            face += 1
        else:
            #无事发生
            pass

   #打印这一年发生的事件
    print(info)
    print(f'颜值{face} 体质{strong} 智力{iq} 家境{home}')
    print('--------------------------------------------------')
    #为了方便观察,加一个小小的暂停操作 暂停1秒
    time.sleep(1)