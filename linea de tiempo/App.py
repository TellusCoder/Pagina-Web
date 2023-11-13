import  qrcode
from PIL import Image

#Tamaño de imagen
qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_H, box_size=10, border=4)
#llenamos de datos el codigo QR
url= "https://forms.office.com/r/X9rpZfzbLX?origin=lprLink"
qr.add_data(url)
qr.make(fit =True)

# Le damos un color qr y color a fondo
qrimg = qr.make_image(fill_color = "white", back_color=(69, 50, 46))
type(qrimg)

# guardar la imagen
qrimg.save("qr_code.png")


