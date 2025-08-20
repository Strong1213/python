import qrcode

# Data to encode in the QR code
data = "https://example.com"

# Generate QR code
qr = qrcode.make(data)

# Save it to a file
qr.save("my_qrcode.png")

print("QR code saved as 'my_qrcode.png'")
