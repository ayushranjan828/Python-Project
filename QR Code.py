import segno
i = input("Enter your URL or Text: ")
size = int(input("Enter Size of QR Code Picture: "))
br = int(input("Enter Border Size of QR Code: "))
bg = input("Enter Background Colour of QR code: ")
cl = input("Enter colour of QR code Pattern: ")
qrbg = input("Enter QR Code Border colour: ")

url = segno.make_qr(i)
url.save("QR Code.png", scale = size, border = br, light = bg, dark = cl, quiet_zone = qrbg)