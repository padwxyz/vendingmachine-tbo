from vmString import *

a = DFA()

tes = automata(a, 'ysdgijnov')


if tes is not None:
    for item in tes:
        if isinstance(item, jus):
            print(f"Jus          : {item.nama}")
            print(f"Saldo        : {item.saldo}")
            print(f"Harga        : {item.harga}")
            print(f"Kembalian    : {item.kembalian}")
            print(f"Buah         : {', '.join(item.buah)}")
            print(f"Es           : {item.es}")
            print(f"Takaran Gula : {item.gula}")
            print(f"Topping      : {item.topping}")
else:
    print("Input Yang Anda Masukkan Salah")