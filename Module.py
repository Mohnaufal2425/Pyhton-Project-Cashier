class Data:
    def __init__(self):
        """
        Inisialisasi objek transaksi dengan atribut item sebagai list kosong untuk menyimpan item-item yang akan dibeli.
        """
        self.items = []

    def add_item(self, item):
        """
        Metode untuk menambahkan item ke dalam list items.
        parameter:
        item (list): List yang berisi nama item, jumlah item, dan harga per item.
        Output : Pesan yang memberitahu bahwa item sudah berhasil ditambahkan ke dalam list item.
        """
        self.items.append(item)
        print("-" * 60)
        print(f"{item} telah berhasil ditambahkan ke keranjang")
        self.show_items()
    def update_item_name(self, old_name, new_name):  
        """
        fungsi untuk mengganti nama item pada list item
        parameter: 
        old_name (string) : Nama item yang akan diganti
        new_name (string) : Nama baru untuk item yang sudah diganti
        Output : pesan yang memberitahu bahwa nama item sudah berhasil diubah
        """

        for item in self.items:
            if item[0]== old_name:
                item[0] == new_name

        print(f"item{old_name} telah berhasil diubah menjadi{new_name}")
        self.show_items()
    def update_item_qty(self, name, qty):
        """
        Fungsi untuk mengganti jumlah item pada list items
        Parameter: 
        Name(string): Nama item yang ingin diubah jumlahnya
        New_qty(int) : Jumlah baru

        Output :
        Pesan yang memberitahu bahwa jumlah item sudah berhasil diubah. 
        """
        for item in self.items:
            if item[0] == name:
                item[1] == qty

        print(f"jumlah{name} telah diubah menjadi{qty}")
        self.show_items()

    def update_item_price(self, name, price):
        """
        Fungsi untuk mengganti harga per item pada list items
        Parameter: 
        Name(string): Nama item yang ingin diubah harganya
        New_price(int) : Harga baru

        Output :harga per item jumlah item sudah berhasil diubah. 
        """
        for item in self.items:
            if item[0] == name:
                item[2] == price

        print(f"harga {name} telah diubah menjadi{price}")
        self.show_items()

    def delete_item(self, name):
        """
        Fungsi untuk menghapus item pada list items
        Parameter: 
        Name(string): Nama item yang ingin dihapus
        Output : item sudah berhasil diubah. 
        """
        for item in self.items:
            if item[0] == name:
                self.items.remove(item)

        print(f"anda telah menghapus : {name}")
        self.show_items()

    def reset_transaction(self):
        """
        Fungsi untuk menghapus semua item pada list items
        Output : item sudah berhasil dihapus
        """
        self.items = []
        print(f"Anda telah mereset transaksi ini. Semua item telah dihapus")
    def check_order(self):
        """
        Fungsi untuk mengecek apakah input data sudah benar atau tidak
        Parameter: 
        Output : 
        Jika semua input data sudah benar, fungsi akan mengeluarkan pesan "pesanan anda sudah benar"
        Jika terdapat kesalahan pada input data, fungsi akan mengeluarkan pesan "terdapat kesalahan input data"
        Jika input data sudah benar, fungsi akan mengeluarkan berupa tabel berisi item, jumlah item, harga satuan, dan total harga 
        """
        error = False
        for item in self.items:
            if (None," " , 0) in item or not all(item):
                error = True
        if error:
            print("Terdapat kesalahan input data")
        else:
            print("Pesanan anda sudah benar")
            self.show_items()

    def show_items(self):
        """
        Fungsi untuk menampilkan nama item, dll
        Output : 
        Tabel nama item, jumlah item, harga satuan, total harga 
        """
        print("=" * 60)
        print("item\t\tjumlah\tharga satuan\ttotal harga")
        print("-" * 60)
        for item in self.items:
            total_price = item[1] * item[2]
            print("{}\t\t{}\t\t{}\t\t\t{}". format(item[0], item[1], item[2], total_price))
        print("-" * 60)

    def total_price(self):
        """
        Fungsi untuk menghitung total harga dari seluruh items pda list items
        Output : 
        Total harga dari seluruh item pada list items 
        """
        total = 0
        for item in self.items:
            total += item[1] * item[2]
        if total > 500000:
            discount = total * 0.1
        elif total > 300000:
            discount = total * 0.08
        elif total > 200000:
            discount = total * 0.05
        else:
            discount = 0
        total -= discount
        print("total harga:{}\ndiskon: {}\ntotal yang harus dibayar: {}". format(total+discount, discount, total))

        