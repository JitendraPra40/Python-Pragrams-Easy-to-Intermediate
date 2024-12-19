import qrcode
def qrcodemaker(data):
    img = qrcode.make(data)
    img.save('qrcode.png')
data = input("Enter the data to be encoded in the QR code:")
qrcodemaker(data)