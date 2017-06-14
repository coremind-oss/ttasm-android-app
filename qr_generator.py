# hashlib is library for making hash from string
# pyqrcode generates qr code from string
# png is acctually pypng library for making png extension images

import hashlib
import pyqrcode
import png


def make_qr():
#     Input fields for user credentials
    name = input('Input username: ')
    password = input('Input password: ')
    
#     Making password a hash with md5 
    password_bytes_hashed = hashlib.md5(password.encode('utf_8'))
    password_string = password_bytes_hashed.hexdigest()
    
#     Making a string from user's credentials
    string = name+' '+password_string 
    
#     QR image is created and located in qr_img/ folder
    img = pyqrcode.create(string,version=8,encoding='UTF-8')
    img.png('qr_img/{}'.format(string),scale=8)
    print('Converting for user: {} with password {} is created. Check qr_img folder for currently created qr_images. After that scan generated svg image with any qr code scanner on your mobile to retrieve encoded credentials'.format(name,password_string))
       
make_qr()

