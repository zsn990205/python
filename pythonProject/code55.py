
import qrcode
# 将自己要写的内容放进去
img = qrcode.make('我可真是小机灵鬼!')
img.save('hhh.png')
