import qrcode
import image

qr = qrcode.QRCode(

    version = 5,
    box_size = 5,
    border = 2

)

data = input("Enter the Data to generate QR code : ")

qr.add_data(data)

qr.make(fit = True)

img = qr.make_image(fill = "black", back_color = "White")

img.save("image.png")