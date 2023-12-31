#Import Data Transaksi
import Module
from Module import *
#Membuat sebuah objek dari Data Transaksi
transct_123 = Data()

#menu utama
while True:
    print("*" * 60)
    print("Selamat datang di Fall Distro. \n"
          "Pilih 1 untuk memasukkan daftar belanja anda:")
    print("1. Tambahkan item")
    print("2. Update nama item")
    print("3. update Jumlah item")
    print("4. Update harga item")
    print("5. Hapus item")
    print("6. Reset transaksi")
    print("7. Cek order kembali")
    print("8. Selesai, silahkan bayar")
    menu_choice = input("pilih menu")

    if menu_choice == '1':
        add = True
        while add:
            try:
                nama_item = input("Masukkan nama item:")
                jumlah_item = int(input("Masukkan jumlah item:"))
                harga_item = int(input("Masukkan harga per item:"))

            except ValueError:
                print("Jumlah item dan harga item harus diisi dengan data integer")
                nama_item = input("Masukkan nama item:")
                jumlah_item = int(input("Masukkan jumlah item:"))
                harga_item = int(input("Masukkan harga per item:"))

            #Tambahkan item ke transaksi
            transct_123.add_item([nama_item, jumlah_item, harga_item])

            #Tanya user untuk menambah item
            add_more = input("Tambah item? (y/n):")
            if add_more.lower() == 'y':
                pass
            elif add_more.lower() == 'n':
                print("Anda akan kembali ke menu utama")
                break
            else:
                print("Input anda salah, \nmasukkan nilai 'y' atau 'n' ")
                print("Anda akan kembali ke menu utama")
                break
    elif menu_choice == '2':
        nama_item_lama = input("Masukkan nama item: ")
        nama_item_baru = input("Masukkan nama item baru: ")
        transct_123.update_item_name(nama_item_lama, nama_item_baru)
    elif menu_choice == '3':
        try:
            nama_item = input("Masukkan nama item: ")
            jumlah_item_baru = int(input("Masukkan jumlah item baru: "))
        except ValueError:
            print("Jumlah item harus diisi dengan data integer")
            nama_item = input("Masukkan nama item: ")
            jumlah_item_baru = int(input("Masukkan jumlah item baru: "))
        transct_123.update_item_qty(nama_item, jumlah_item_baru)
    elif menu_choice == '4':
        try:
            nama_item = input("Masukkan nama item: ")
            harga_item_baru = int(input("Masukkan harga item baru: "))
        except ValueError:
            print("Harga item harus diisi dengan data integer")
            nama_item = input("Masukkan nama utem: ")
            harga_item_baru = int(input("Masukkan jumlah item baru: "))
        transct_123.update_item_qty(nama_item, harga_item_baru)
    elif menu_choice == '5':
        nama_item = input("Masukkan nama item: ")
        transct_123.delete_item(nama_item)
    elif menu_choice == '6':
        transct_123.reset_transaction()
    elif menu_choice == '7':
        transct_123.check_order()
    elif menu_choice == '8':
        break 

#Cetak detail order
transct_123.check_order()

#Cetak harga total

total = transct_123.total_price()