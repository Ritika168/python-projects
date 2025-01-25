!pip install qrcode[pil]
import qrcode

from IPython.display import Image, display

# Function to generate QR Code
def generate_qr_code(data, filename="qrcode.png"):
  
    # Create a QR Code instance
    qr = qrcode.QRCode(
        version=1,  # Controls the size of the QR Code (1 is the smallest).
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    
    # Add data to the QR Code
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image of the QR Code
    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)
    print(f"QR code saved as {filename}")
    
    # Display the image
    display(Image(filename))

# Example: Generate a QR Code
data = input("enter link")
generate_qr_code(data)
