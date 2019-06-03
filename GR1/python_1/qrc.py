# encoding=utf-8
import qrcode
from PIL import Image
def url(url):
    img = qrcode.make(url)#已经生成二维码图片对象
    img.save('static/qrimg/1.png')#保存二维码图片
    return 'static/qrimg/1.png'