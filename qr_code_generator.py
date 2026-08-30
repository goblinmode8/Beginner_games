# A Quick Response code is a two-dimensional pictographic code used for its fast
#     readability and comparatively large storage capacity. The code consists of
#     black modules arranged in a square pattern on a white background. The
#     information encoded can be made up of any kind of data \

# python3 -m venv venv = set up virtual environment
# .venv folder now available
# inside bin is executables
#  venv/bin/activate        this allows you to download packages only for this project
#  deactivate

import qrcode

print("Welcome to the QR Code Generator")

data = input("Enter the text or URl : ").strip()
filename = input("Enter the filename: ").strip()

qr = qrcode.QRCode(box_size = 10, border = 4)
qr.add_data(data)
image = qr.make_image(fill_color="black", back_color="white")
image.save(filename)

print(f"QR code saved as: + {filename}")

# → third-party libraries + virtual environments + file output
