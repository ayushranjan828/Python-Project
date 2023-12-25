import segno
# Input for QR Code development
i = input("Enter your URL or Text: ")
size = int(input("Enter Size of QR Code Picture: "))
br = int(input("Enter Border Size of QR Code: "))
bg = input("Enter Background Colour of QR code: ")
cl = input("Enter colour of QR code Pattern: ")
qrbg = input("Enter QR Code Border colour: ")

# Option asking for QR Code rotation
opt = str(input("Did you want to rotate your QR code (YES/NO): "))

if(opt == "YES"):
    deg = int(input("Enter degree of rotation: "))
    url = segno.make_qr(i)
    url_rotate = url.to_pil( scale = size, border = br, light = bg, dark = cl, quiet_zone = qrbg).rotate(deg, expand = True)
    url_rotate.save("Rotated QR Code.png")
else:
    url = segno.make_qr(i)
    url.save("Not Rotated QR Code.png", scale = size, border = br, light = bg, dark = cl, quiet_zone = qrbg)
