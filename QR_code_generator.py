import qrcode
import numpy as np
from PIL import Image, ImageTk
import tkinter as tk

def generate_qr():
    # Get URL from user input field
    url = url_input.get()

    # Create QR code image
    qr_code = qrcode.QRCode(version=1, box_size=10, border=5)
    qr_code.add_data(url)
    qr_code.make(fit=True)
    img = qr_code.make_image(fill='black', back_color='white')

    # Convert image to numpy array
    img_arr = np.array(img)
    img_arr = img_arr[:,  ::-1].copy()  # Convert BGR to RGB
    img_arr = np.ascontiguousarray(img_arr)  # Make numpy array contiguous

    # Convert numpy array to tkinter photo image and display on canvas
    img_tk = ImageTk.PhotoImage(Image.fromarray(img_arr))
    canvas.create_image(0, 0, image=img_tk, anchor=tk.NW)
    canvas.img_tk = img_tk  # Save reference to image to prevent garbage collection

# Create tkinter window and canvas
root = tk.Tk()
canvas = tk.Canvas(root, width=800, height=700)
canvas.pack()

# Create user input field and "Generate QR" button
url_input = tk.Entry(root)
url_input.pack()
generate_button = tk.Button(root, text="Generate QR", command=generate_qr)
generate_button.pack()

root.mainloop()
