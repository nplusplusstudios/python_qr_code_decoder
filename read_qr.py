# Author Mohamed Nuzrath

import cv2
# Load image
img = cv2.imread("qr_demo.png")

# debug code
# you should see False if the Library properly installed
print(img is None) 

# convert to greyscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# invert colors
gray = cv2.bitwise_not(gray)
                 
# create detector
detector = cv2.QRCodeDetector()

# detect and decode
data, bbox, _ = detector.detectAndDecode(img)

if data:
    print("QR Code Data : ", data)
else:
    print("QR Code not detected")