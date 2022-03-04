#Python has a library “qrcode” for generating QR code images. It can be installed using pip. pip install qrcode
#A Quick Response Code or a QR Code is a two-dimensional bar code used for its fast readability and comparatively large storage capacity. 
#It consists of black squares arranged in a square grid on a white background.
# Approch:
#* Import module
#*Create Qrcode with qrcode.make() and it returns a PilImage object.
#*Save into image
# Importing library
import qrcode

# Data to be encoded
data = 'QR Code using make() fuction'

# Encoding data using make() function
img = qrcode.make(data)

# Saving as an image file
img.save('MyQRCode.png')
