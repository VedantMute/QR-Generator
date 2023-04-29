import tkinter as tk
import qrcode as qr

class QRCodeApp:
    def __init__(self, master):
        self.master = master
        self.master.geometry("600x400")

        #variables to store value
        self.qr_var = tk.StringVar()
        self.save_var = tk.StringVar()

        # creating a label for QR url
        qr_label = tk.Label(self.master, text='Enter QR url', font=('calibre', 10, 'bold'))
        # creating input box for url
        self.qr_entry = tk.Entry(self.master, textvariable=self.qr_var, font=('calibre', 10, 'normal'))
        # creating a label to save file name
        save_label = tk.Label(self.master, text='Enter File Name', font=('calibre', 10, 'bold'))
        # creating a input box to save name
        self.save_entry = tk.Entry(self.master, textvariable=self.save_var, font=('calibre', 10, 'normal'))
        # creating a button using the widget to call submit function

        
        sub_btn = tk.Button(self.master, text='Submit', command=self.submit)

        # placing the label and entry in the required position using grid method
        qr_label.grid(row=0, column=0)
        self.qr_entry.grid(row=0, column=1)
        save_label.grid(row=1, column=0)
        self.save_entry.grid(row=1, column=1)
        sub_btn.grid(row=2, column=1)

    def submit(self):
        qr_url = self.qr_var.get()
        saveord = self.save_var.get()

        img = qr.make(qr_url)
        img.save(f"{saveord}.png")
        self.qrimg = tk.PhotoImage(file=f"{saveord}.png")
        self.qrimg_label = tk.Label(self.master, image=self.qrimg)
        self.qrimg_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        print(f"QR is generated successfully and saved with filename{saveord}.png")

        self.qr_var.set("")
        self.save_var.set("")

if __name__ == '__main__':
    root = tk.Tk()
    app = QRCodeApp(root)
    root.mainloop()
