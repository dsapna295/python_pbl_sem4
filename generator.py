
import qrcode
import os.path

f = open('1.csv', 'r')
lines = f.read().split('\n')
for i in lines:
    s = i + '.png'
    
    file_exists = os.path.exists(s)
    if file_exists:
        pass

    else:
        img=qrcode.make(i)
        img.save(s)