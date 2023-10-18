import random
from threading import Thread

from pynput import keyboard
from playsound import playsound

# 创建一个计数器 计算用户按了多少次键盘
count = 0
# 我们想让随机播放
soundList = ['sound/1.mp3', 'sound/2.mp3', 'sound/3.mp3']
def onRelease(key):
    # 这个函数是在用户释放按键的时候会被调用到
    # 这里监听release操作
    # 这个函数不是自己主动调用的,而是将其交给listener由用户释放按键的时候自动调用
    # 程序在合适的时候自动调用 叫回调函数
    print(key)
    global count
    count += 1
    if count % 10 == 0:
        # 播放音频
        # 生成一个随机数
        i = random.randint(0, len(soundList)-1)
        # 由于此处的音频耗时较多,可能会引起卡顿
        # 可以创建一个线程,在线程中播放音频
        t = Thread(target=playsound, args=(soundList[i], ))
        t.start()


# 当我们创建好listener之后用户的键盘按键操作就能被捕获到
# 还希望捕获到之后可以执行一段代码
listener = keyboard.Listener(on_release=onRelease)
listener.start()
listener.join()

