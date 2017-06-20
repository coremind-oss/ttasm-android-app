from pyzbar.pyzbar import decode
from PIL import Image

# decoded qr code image from folder qr_img/

decoded_image = decode(Image.open('/tmp/Danijel 2784d7d3f826ccb98677863c0215403f.png'))
print(decoded_image)

#credentials from list presented in bytes
credentials_in_bytes = decoded_image[0][0]
print(decoded_image[0][0])

#credentials in string
credentials_in_string = credentials_in_bytes.decode()
print(credentials_in_string)

splited_string = str.split(credentials_in_string)
# print('\nUsername: {} \nPassword: {}'.format(splited_string[0], splited_string[1]))


    
