import pyqrcode
import hashlib


def make_qr():
    name = input('Input username: ')
    password = input('Input password: ')
    password_bytes_hashed = hashlib.md5(password.encode('utf_8'))
    password_string = password_bytes_hashed.hexdigest()
    string = name+'_'+password_string 
    img = pyqrcode.create(string,version=8,encoding='UTF-8')
    img.svg('qr_img/{}'.format(string),scale=8)
    print('Converting for user: {} with password {} is created. Check qr_img folder for currently created qr_images. After that scan generated svg image with any qr code scanner on your mobile to retrieve encoded credentials'.format(name,password_string))
       
make_qr()

