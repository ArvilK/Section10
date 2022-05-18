import qrcode

data = 'Hello I am Arvil, add me on instagram as \'kajevicvk'
# this is simpler
# img = qrcode.make(data)

# img.save('C:/Users/arvil.kajevic/Desktop/New folder/myqrcode.png')

qr = qrcode.QRCode(version = 1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color = 'red', back_color = 'white')

img.save('C:/Users/arvil.kajevic/Desktop/New folder/myqrcode.png')