class jus :
    def __init__(self):
        self.nama = ""
        self.saldo = 0
        self.harga = 0
        self.kembalian = 0
        self.buah = []
        self.jumlah_buah = 0
        self.es = ""
        self.gula = ""
        self.topping = ""

    def setNama(self, nama):
        self.nama = nama
    def setSaldo(self, saldo):
        self.saldo = saldo
    def setHarga(self, harga):
        self.harga = harga
    def setKembalian(self, kembalian):
        self.kembalian = kembalian

    def addBuah(self, buah):
        self.buah.append(buah)
        self.jumlah_buah += 1

    def setEs(self, es):
        self.es = es
    def setGula(self, gula):
        self.gula = gula
    def setTopping(self, topping):
        self.topping = topping
    
    def printDetail(self):
        print(self.nama)
        print(self.saldo)
        print(self.harga)
        print(self.kembalian)
        print(self.buah)
        print(self.es)
        print(self.gula)
        print(self.topping)

class DFA :
    def __init__(self):
        self.initial_state = 'Q0'
        self.state_5000 = 'A'
        self.state_10000 = 'B'
        self.state_15000 = 'C'
        self.state_20000 = 'V'
        self.state_menyiapkan_wadah = 'R'
        self.state_pepaya = 'D'
        self.state_alpukat = 'E'
        self.state_semangka = 'F'
        self.state_pisang = 'G'
        self.state_pakai_es = 'H'
        self.state_tidak_pakai_es = 'I'
        self.state_menyiapkan_gula = 'J'
        self.state_sweet_sugar = 'K'
        self.state_normal_sugar = 'L'
        self.state_less_sugar = 'M'
        self.state_no_sugar = "N"
        self.state_vanilla_milk = 'O'
        self.state_chocolate_milk = 'P'
        self.final_state = 'Q1'
        self.current_state = 'Q0'
        self.saldo = 0
        self.harga = 0
        self.kembalian = 0
        self.selected_menu = None
        

def automata(DFA, string):
    order_list = []
    for letter in string:

        # Dari initial state Q0
        if DFA.current_state == 'Q0':
            current_order = jus()
            if letter == 'x':
                DFA.current_state = 'A'
                current_order.setSaldo(5000)
            elif letter == 'y':
                DFA.current_state = 'B'
                current_order.setSaldo(10000)
            elif letter == 'z':
                DFA.current_state = 'V'
                current_order.setSaldo(20000)

        # Jika Jumlah Saldo 5000
        elif DFA.current_state == 'A':
            if letter == 'x':
                DFA.current_state = 'B'
                current_order.setSaldo(10000)
            elif letter == 'y':
                DFA.current_state = 'C'
                current_order.setSaldo(15000)
            elif letter == 'r':
                DFA.current_state = 'R'

        # Jika Jumlah Saldo 10000
        elif DFA.current_state == 'B':
            if letter == 'x':
                DFA.current_state = 'C'
                current_order.setSaldo(15000)
            elif letter == 'y':
                DFA.current_state = 'V'
                current_order.setSaldo(20000)
            elif letter == 'r':
                DFA.current_state = 'R'
            elif letter == 's':
                DFA.current_state = 'R'


        # Jika Jumlah Saldo 15000
        elif DFA.current_state == 'C':
            if letter == 'x':
                DFA.current_state = 'V'
                current_order.setSaldo(20000)
            if letter == 'r':
                DFA.current_state = 'R'
            elif letter == 's':
                DFA.current_state = 'R'
            elif letter == 't':
                DFA.current_state = 'R'

        # Jika Jumlah Saldo 20000
        if DFA.current_state == 'V':
            if letter == 'r':
                DFA.current_state = 'R'
            elif letter == 's':
                DFA.current_state = 'R'
            elif letter == 't':
                DFA.current_state = 'R'

        # Memilih Kombinasi Buah
        if DFA.current_state == 'R':
            if letter == 'd':
                DFA.current_state = 'D'
                current_order.addBuah("Pepaya")
                current_order.harga += 5000
            elif letter == 'e':
                DFA.current_state = 'E'
                current_order.addBuah("Alpukat")
                current_order.harga += 5000
            elif letter == 'f':
                DFA.current_state = 'F'
                current_order.addBuah("Semangka")
                current_order.harga += 5000
            elif letter == 'g':
                DFA.current_state = 'G'
                current_order.addBuah("Pisang")
                current_order.harga += 5000
        if DFA.current_state == 'D':
            if letter == 'e':
                DFA.current_state = 'E'
                current_order.addBuah("Alpukat")
                current_order.harga += 5000
            elif letter == 'f':
                DFA.current_state = 'F'
                current_order.addBuah("Semangka")
                current_order.harga += 5000
            elif letter == 'g':
                DFA.current_state = 'G'
                current_order.addBuah("Pisang")
                current_order.harga += 5000
            elif letter == 'h':
                DFA.current_state = 'H'
                current_order.setEs("Pakai Es")
                current_order.harga += 5000
            elif letter == 'i':
                DFA.current_state = 'I'
                current_order.setEs("Tidak Pakai Es")
        if DFA.current_state == 'E':
            if letter == 'd':
                DFA.current_state = 'D'
                current_order.addBuah("Pepaya")
                current_order.harga += 5000
            elif letter == 'f':
                DFA.current_state = 'F'
                current_order.addBuah("Semangka")
                current_order.harga += 5000
            elif letter == 'g':
                DFA.current_state = 'G'
                current_order.addBuah("Pisang")
                current_order.harga += 5000
            elif letter == 'h':
                DFA.current_state = 'H'
                current_order.setEs("Pakai Es")
            elif letter == 'i':
                DFA.current_state = 'I'
                current_order.setEs("Tidak Pakai Es")
        if DFA.current_state == 'F':
            if letter == 'd':
                DFA.current_state = 'D'
                current_order.addBuah("Pepaya")
                current_order.harga += 5000
            elif letter == 'e':
                DFA.current_state = 'E'
                current_order.addBuah("Alpukat")
                current_order.harga += 5000
            elif letter == 'g':
                DFA.current_state = 'G'
                current_order.addBuah("Pisang")
                current_order.harga += 5000
            elif letter == 'h':
                DFA.current_state = 'H'
                current_order.setEs("Pakai Es")
            elif letter == 'i':
                DFA.current_state = 'I'
                current_order.setEs("Tidak Pakai Es")
        if DFA.current_state == 'G':
            if letter == 'd':
                DFA.current_state = 'D'
                current_order.addBuah("Pepaya")
                current_order.harga += 5000
            elif letter == 'e':
                DFA.current_state = 'E'
                current_order.addBuah("Alpukat")
                current_order.harga += 5000
            elif letter == 'f':
                DFA.current_state = 'F'
                current_order.addBuah("Semangka")
                current_order.harga += 5000
            elif letter == 'h':
                DFA.current_state = 'H'
                current_order.setEs("Pakai Es")
            elif letter == 'i':
                DFA.current_state = 'I'
                current_order.setEs("Tidak Pakai Es")
        if DFA.current_state == 'H':
            if letter == 'j':
                DFA.current_state = 'J'
        if DFA.current_state == 'I':
            if letter == 'j':
                DFA.current_state = 'J'
        
        # Memilih Takaran Gula
        if DFA.current_state == 'J':
            if letter == 'k':
                DFA.current_state = 'K'
                current_order.setGula("Sweet")
            elif letter == 'l':
                DFA.current_state = 'L'
                current_order.setGula("Normal")
            elif letter == 'm':
                DFA.current_state = 'M'
                current_order.setGula("Less Sugar")
            elif letter == 'n':
                DFA.current_state = 'N'
                current_order.setGula("No Sugar")

        # Memilih Topping
        if DFA.current_state in {'K', 'L', 'M', 'N'}:
            if letter == 'o':
                DFA.current_state = 'O'
                current_order.setTopping("Susu Kental Manis Vanilla")
            elif letter == 'p':
                DFA.current_state = 'P'
                current_order.setTopping("Susu Kental Manis Coklat")
        if DFA.current_state in {'O', 'P'}:
            if letter == 'v':
                DFA.current_state = 'Q1'
                if current_order.harga <= current_order.saldo:
                    current_order.setKembalian(current_order.saldo - current_order.harga)
                else:
                    return
                if current_order.jumlah_buah == 1:
                    current_order.setNama("Jus 1 Buah")
                    order_list.append (current_order)
                elif current_order.jumlah_buah == 2:
                    current_order.setNama("Mix 2 Buah")
                    order_list.append (current_order)
                elif current_order.jumlah_buah == 3:
                    current_order.setNama("Mix 3 Buah")
                    order_list.append (current_order)
                elif current_order.jumlah_buah == 4:
                    print("Error")

        if DFA.current_state in DFA.final_state:
            return order_list
    else:
        return None