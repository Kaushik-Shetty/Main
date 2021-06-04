import qrcode

code = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L,
                     box_size=50,
                     border=1)
code.add_data("Dummy_Project")
code.make(fit=True)

img = code.make_image(fillcolor='black', backcolor='white')
img.save("QR.png")
