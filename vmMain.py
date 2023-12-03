from customtkinter import *
from PIL import Image
from vmString import*

string = ''
total_saldo = 0

def welcome_page(asd):
    asd.destroy()
    window = CTkToplevel()
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

    welcomeBG = Image.open('assets/welcomeBG.png')
    welcomeBG_img = CTkImage(light_image=welcomeBG, size=(400, 600))
    CTkLabel(master=window, image=welcomeBG_img, text='').place(x=1, y=0)

    saldo_label = CTkLabel(master=window, text='Saldo sekarang: Rp 0', fg_color='#003D29', text_color='#BAF0BC')
    saldo_label.place(x=20, y=30)

    limaRibu = Image.open('assets/5ribu.png')
    limaRibu_img = CTkImage(light_image=limaRibu, size=(110, 60))
    limaRibu_button = CTkButton(master=window, image=limaRibu_img, text='', fg_color='transparent', hover=False, command=lambda value = 'x': inputUang_string(value, saldo_label))
    limaRibu_button.tkraise()
    limaRibu_button.place(x=10, y=425)

    sepuluhRibu = Image.open('assets/10ribu.png')
    sepuluhRibu_img = CTkImage(light_image=sepuluhRibu, size=(110, 60))
    sepuluhRibu_button = CTkButton(master=window, image=sepuluhRibu_img, text='', fg_color='transparent', hover=False, command=lambda value = 'y': inputUang_string(value, saldo_label))
    sepuluhRibu_button.tkraise()
    sepuluhRibu_button.place(x=130, y=425)

    duapuluhRibu = Image.open('assets/20ribu.png')
    duapuluhRibu_img = CTkImage(light_image=duapuluhRibu, size=(110, 60))
    duapuluhRibu_button = CTkButton(master=window, image=duapuluhRibu_img, text='', fg_color='transparent', hover=False, command=lambda value = 'z': inputUang_string(value, saldo_label))
    duapuluhRibu_button.tkraise()
    duapuluhRibu_button.place(x=250, y=425)

    next = Image.open('assets/next.png')
    next_img = CTkImage(light_image=next, size=(250, 50))
    next_button = CTkButton(master=window, image=next_img, text='', fg_color='transparent', hover=False, command=lambda: (MixBuah_page(window)))
    next_button.tkraise()
    next_button.place(x=65, y=535)

    window.mainloop()

def inputUang_string(value, saldo_label):
    global total_saldo
    global string

    if total_saldo == 20000:
        return
    
    string += value
    print(f"string masukan uang: {string}")
    
    if total_saldo == 0:
        if value == 'x':
            total_saldo += 5000
        elif value == 'y':
            total_saldo += 10000
        elif value == 'z':
            total_saldo += 20000
        saldo_label.configure(text=f"Saldo sekarang: Rp {total_saldo}")
    elif total_saldo == 5000:
        if value == 'x':
            total_saldo += 5000
        elif value == 'y':
            total_saldo += 10000
        saldo_label.configure(text=f"Saldo sekarang: Rp {total_saldo}")
    elif total_saldo == 10000:
        if value == 'x':
            total_saldo += 5000
        if value == 'y':
            total_saldo += 10000
        saldo_label.configure(text=f"Saldo sekarang: Rp {total_saldo}")
    elif total_saldo == 15000:
        if value == 'x':
            total_saldo += 5000
        saldo_label.configure(text=f"Saldo sekarang: Rp {total_saldo}")
    elif total_saldo == 20000:
        saldo_label.configure(text=f"Saldo sekarang: Rp {total_saldo}")

def MixBuah_page(asd):
    asd.destroy()
    window = CTkToplevel()
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

    single = Image.open('assets/1buah.png')
    single_img = CTkImage(light_image=single, size=(270, 110))
    single_button = CTkButton(master=window, image=single_img, text='', fg_color='transparent', hover=False, command=lambda value = 'r': (MixBuah_string(window, value)))
    single_button.tkraise()
    single_button.place(x=60, y=110)

    mixtwo = Image.open('assets/2buah.png')
    mixtwo_img = CTkImage(light_image=mixtwo, size=(270, 110))
    mixtwo_button = CTkButton(master=window, image=mixtwo_img, text='', fg_color='transparent', hover=False, command=lambda value = 's': (MixBuah_string(window, value)))
    mixtwo_button.tkraise()
    mixtwo_button.place(x=60, y=245)

    mixthree = Image.open('assets/3buah.png')
    mixthree_img = CTkImage(light_image=mixthree, size=(270, 110))
    ixthree_button = CTkButton(master=window, image=mixthree_img, text='', fg_color='transparent', hover=False, command=lambda value = 't': (MixBuah_string(window, value)))
    ixthree_button.tkraise()
    ixthree_button.place(x=60, y=380)

    window.mainloop()

def MixBuah_string(asd, invalue):
    asd.destroy
    global string
    string+= invalue
    print(f"string pilihan mix buah : {string}")
    if invalue in ['r', 's', 't']:
        PilihBuah_page(asd)

def PilihBuah_page(asd):
    asd.destroy()
    window = CTkToplevel()
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

    pepaya = Image.open('assets/pepaya.png')
    pepaya_img = CTkImage(light_image=pepaya, size=(150, 150))
    pepaya_button = CTkButton(master=window, image=pepaya_img , text='', fg_color='transparent', hover=False)
    pepaya_button.tkraise()
    pepaya_button.place(x=32, y=115)

    alpukat = Image.open('assets/alpukat.png')
    alpukat_img = CTkImage(light_image=alpukat, size=(150, 150))
    alpukat_button = CTkButton(master=window, image=alpukat_img, text='', fg_color='transparent', hover=False)
    alpukat_button.tkraise()
    alpukat_button.place(x=205, y=115) 

    semangka = Image.open('assets/semangka.png')
    semangka_img = CTkImage(light_image=semangka, size=(150, 150))
    semangka_button = CTkButton(master=window, image=semangka_img, text='', fg_color='transparent', hover=False)
    semangka_button.tkraise()
    semangka_button.place(x=32, y=312)

    pisang = Image.open('assets/pisang.png')
    pisang_img = CTkImage(light_image=pisang, size=(150, 150))
    pisang_button = CTkButton(master=window, image=pisang_img, text='', fg_color='transparent', hover=False)
    pisang_button.tkraise()
    pisang_button.place(x=205, y=312)

    checkboxvar_pepaya = StringVar(value = 'off')
    checkbox_pepaya = CTkCheckBox(master=window, onvalue='on', offvalue='off', border_color='#003D29', text='', fg_color='#003D29', variable=checkboxvar_pepaya)
    checkbox_pepaya.place(x=100, y=272)

    checkboxvar_alpukat = StringVar(value = 'off')
    checkbox_alpukat = CTkCheckBox(master=window, onvalue='on', offvalue='off', border_color='#003D29', text='', fg_color='#003D29', variable=checkboxvar_alpukat)
    checkbox_alpukat.place(x=273, y=272)

    checkboxvar_semangka = StringVar(value = 'off')
    checkbox_semangka = CTkCheckBox(master=window, onvalue='on', offvalue='off', border_color='#003D29', text='', fg_color='#003D29', variable=checkboxvar_semangka)
    checkbox_semangka.place(x=100, y=470)

    checkboxvar_pisang = StringVar(value = 'off')
    checkbox_pisang = CTkCheckBox(master=window, onvalue='on', offvalue='off', border_color='#003D29', text='', fg_color='#003D29', variable=checkboxvar_pisang)
    checkbox_pisang.place(x=273, y=470)

    next = Image.open('assets/next.png')
    next_img = CTkImage(light_image=next, size=(250, 50))
    next_button = CTkButton(master=window, image=next_img, text='', fg_color='transparent', hover=False, command=lambda: (PilihBuah_string(window, checkbox_pepaya, checkbox_alpukat, checkbox_semangka, checkbox_pisang)))
    next_button.tkraise()
    next_button.place(x=65, y=535)

    window.mainloop()

def PilihBuah_string(asd, checkbox_pepaya, checkbox_alpukat, checkbox_semangka, checkbox_pisang):
    asd.destroy()
    global string
    pepaya_choice = checkbox_pepaya.get()
    alpukat_choice = checkbox_alpukat.get()
    semangka_choice = checkbox_semangka.get()
    pisang_choice = checkbox_pisang.get()

    if pepaya_choice == 'on':
        string += 'd'
    if alpukat_choice == 'on':
        string += 'e'
    if semangka_choice == 'on':
        string += 'f'
    if pisang_choice == 'on':
        string += 'g'
    
    print(f'string jenis buah: {string}')
    PilihEs_page(asd)

def PilihEs_page(asd):
    asd.destroy()
    window = CTkToplevel()
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

    ice = Image.open('assets/yesIce.png')
    ice_img = CTkImage(light_image=ice, size=(150, 150))
    button_ice = CTkButton(master=window, image=ice_img, text='', fg_color='transparent', hover=False, command=lambda value = 'hj': (PilihEs_string(window, value)) )
    button_ice.tkraise()
    button_ice.place(x=33, y=225)

    noIce_data = Image.open('assets/noIce.png')
    noIce_button = CTkImage(light_image=noIce_data, size=(150, 150))
    noIce_button = CTkButton(master=window, image=noIce_button, text='', fg_color='transparent', hover=False, command=lambda value = 'ij': (PilihEs_string(window, value)))
    noIce_button.tkraise()
    noIce_button.place(x=200, y=225)

    window.mainloop()

def PilihEs_string(asd, invalue):
    asd.destroy
    global string
    string+= invalue
    print(f"string pilihan es : {string}")
    if invalue in ['hj', 'ij']:
        PilihKemanisan_page(asd)

def PilihKemanisan_page(asd):
    asd.destroy()
    window = CTkToplevel()
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

    sweet = Image.open('assets/sugar_sweet.png')
    sweet_img = CTkImage(light_image=sweet, size=(300, 60))
    sweet_button = CTkButton(master=window, image=sweet_img, text='', fg_color='transparent', hover=False, command=lambda value = 'k': (PilihKemanisan_string(window, value)))
    sweet_button.tkraise()
    sweet_button.place(x=40, y=173)

    normal = Image.open('assets/sugar_normal.png')
    normal_img = CTkImage(light_image=normal, size=(300, 60))
    normal_button = CTkButton(master=window, image=normal_img, text='', fg_color='transparent', hover=False, command=lambda value = 'l': (PilihKemanisan_string(window, value)))
    normal_button.tkraise()
    normal_button.place(x=40, y=241)

    lesssugar = Image.open('assets/sugar_less.png')
    lesssugar_img = CTkImage(light_image=lesssugar, size=(300, 60))
    lesssugar_button = CTkButton(master=window, image=lesssugar_img, text='', fg_color='transparent', hover=False, command=lambda value = 'm': (PilihKemanisan_string(window, value)))
    lesssugar_button.tkraise()
    lesssugar_button.place(x=40, y=309)

    nosugar = Image.open('assets/sugar_no.png')
    nosugar_img = CTkImage(light_image=nosugar, size=(300, 60))
    nosugar_button = CTkButton(master=window, image=nosugar_img, text='', fg_color='transparent', hover=False, command=lambda value = 'n': (PilihKemanisan_string(window, value)))
    nosugar_button.tkraise()
    nosugar_button.place(x=40, y=377)

    window.mainloop()

def PilihKemanisan_string(asd, invalue):
    asd.destroy
    global string
    string+= invalue
    print(f"string tingkat kemanisan : {string}")
    if invalue in ['k', 'l', 'm', 'n']:
        PilihTopping_page(asd)

def PilihTopping_page(asd):
    asd.destroy()
    window = CTkToplevel()
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

    vanila = Image.open('assets/vanila.png')
    vanila_img = CTkImage(light_image=vanila, size=(150, 150))
    vanila_button = CTkButton(master=window, image=vanila_img, text='', fg_color='transparent', hover=False, command=lambda value = 'ov': (PilihTopping_string(window, value)))
    vanila_button.tkraise()
    vanila_button.place(x=33, y=225)

    cokelat = Image.open('assets/cokelat.png')
    cokelat_img = CTkImage(light_image=cokelat, size=(150, 150))
    cokelat_button = CTkButton(master=window, image=cokelat_img, text='', fg_color='transparent', hover=False, command=lambda value = 'pv': (PilihTopping_string(window, value)))
    cokelat_button.tkraise()
    cokelat_button.place(x=200, y=225)

    window.mainloop()

def PilihTopping_string(asd, invalue):
    asd.destroy
    global string
    string+= invalue
    print(f"string pilihan topping : {string}")
    if invalue in ['ov', 'pv']:
        Checkout_page(asd)

def Checkout_page(asd):
    global string
    string += 'v'
    a = DFA()
    asd.destroy()
    window = CTkToplevel()
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
    font = CTkFont("Poppins", 15)

    struk = automata(a, string)

    if struk is not None:
        harga_total = 0
        saldo_total = 0
        order_details = ""
        kembalian_total = 0

        for item in struk:
            if isinstance(item, jus):
                harga_total += item.harga
                saldo_total += item.saldo
                kembalian_total += (item.saldo - item.harga)
                order_details += f"Total Saldo                  : Rp {saldo_total}\n"
                order_details += f"Total Harga Pesanan  : Rp {harga_total}\n"
                order_details += f"Total Kembalian          : Rp {kembalian_total}\n"
                order_details += "\n"
                order_details += f"Jus                   : {item.nama}\n"
                order_details += f"Buah                : {', '.join(item.buah)}\n"
                order_details += f"Es                    : {item.es}\n"
                order_details += f"Takaran Gula  : {item.gula}\n"
                order_details += f"Topping          : {item.topping}\n"
        
        keterangan = Image.open('assets/keterangan.png')
        keterangan_img = CTkImage(light_image=keterangan, size=(293,60))
        CTkLabel(master=window, image=keterangan_img, text='').place(x=53, y=50)
            
        label_text = CTkTextbox(master=window, width=300, height=300, font=font, fg_color='#FFFFFF', text_color='black')
        label_text.place(x= 50, y= 140)
        label_text.insert("1.0", order_details)

        confirm = Image.open('assets/confirm.png')
        confirm_img = CTkImage(light_image=confirm, size=(250, 50))
        confirm_button = CTkButton(master=window, image=confirm_img, text='', fg_color='transparent', hover=False, command=lambda: (exit_page(window)))
        confirm_button.tkraise()
        confirm_button.place(x=68, y=535)
        
        window.mainloop()
    else:
        print("Input ERROR!")
        print(string)
    
def exit_next(asd, window):
        asd.destroy()
        global string
        string = ''
        window.deiconify()

def exit_page(asd):
    asd.destroy()
    window = CTkToplevel()
    window.title("Vending Machine Jus Buah")
    
    window = CTkToplevel()
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

    end_page = Image.open('assets/endpage.png')
    end_page_img = CTkImage(light_image=end_page, size=(400, 600))
    CTkLabel(master=window, image=end_page_img, text='').place(x=0, y=0)

    end = Image.open('assets/exit.png')
    end_img = CTkImage(light_image=end, size=(250, 50))
    end_button = CTkButton(master=window, image=end_img, text='', fg_color='transparent', hover=False, command=lambda: (exit_next(window, asd)))
    end_button.tkraise()
    end_button.place(x=68, y=535)