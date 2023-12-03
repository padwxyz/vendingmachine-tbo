from customtkinter import *
from PIL import Image
from vmMain import*

window = CTk()
window.title("Vending Machine Jus Buah (VIVO)")

lebar = 400
tinggi = 600

screenwidth = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()
newx = int((screenwidth/2) - (lebar/2))
newy = int((screenheight/2) - (tinggi/2))
window.geometry(f"{lebar}x{tinggi}+{newx}+{newy}")

window.resizable(False, False)
window.configure(fg_color='#BAF0BC')

landing = Image.open('assets/landing.png')
landing_img = CTkImage(light_image=landing, size=(400, 600))
CTkLabel(master=window, text='', image=landing_img).place(x=-0, y=0)

start = Image.open('assets/start.png')
start_img = CTkImage(light_image=start, size=(250, 50))
start_button = CTkButton(master=window, image=start_img, text='', fg_color='transparent', hover=False, command=lambda: (welcome_page(window)))
start_button.tkraise()
start_button.place(x=68, y=535)

window.mainloop()