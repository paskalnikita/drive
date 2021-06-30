import pyqrcode
url = pyqrcode.create('https://opticool.technology/demo')
url.svg('uca-url.svg', scale=8)
url.eps('uca-url.eps', scale=2)
print(url.terminal(quiet_zone=1))


import pyqrcode
from PIL import Image
url = pyqrcode.QRCode('http://www.eqxiu.com',error = 'H')
url.png('test.png',scale=10)
im = Image.open('test.png')
im = im.convert("RGBA")
logo = Image.open('logo.png')
box = (135,135,235,235)
im.crop(box)
region = logo
region = region.resize((box[2] - box[0], box[3] - box[1]))
im.paste(region,box)
im.show()
# im.save("result.png")