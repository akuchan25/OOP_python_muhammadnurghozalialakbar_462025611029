from abc import ABC, abstractmethod

class MasterClassException(Exception): 
    pass

class User(ABC):
    def __init__(self, uid, nama, pwd):
        self.uid = uid
        self.nama = nama
        self.__pwd = pwd

    def check_pwd(self, pwd):
        return self.__pwd == pwd

    @abstractmethod
    def menu(self): 
        pass

class MasterClass:
    def __init__(self, id_k, judul, mentor, harga, kuota):
        self.id_k = id_k
        self.judul = judul
        self.mentor = mentor
        self.harga = harga
        self.kuota = kuota

    def __str__(self):
        return f"[{self.id_k}] {self.judul} ({self.mentor}) - Rp{self.harga:,.0f} | Sisa Kuota: {self.kuota}"

class Peserta(User):
    def __init__(self, uid, nama, pwd):
        super().__init__(uid, nama, pwd)
        self.riwayat = []

    def menu(self):
        print(f"\n--- MENU PESERTA ({self.nama}) ---\n1. Katalog  2. Daftar Kelas  3. Riwayat  4. Logout")

class Admin(User):
    def menu(self):
        print(f"\n--- MENU ADMIN ({self.nama}) ---\n1. Tambah Kelas  2. Laporan Omset  3. Logout")

class Pendaftaran:
    def __init__(self, id_reg, peserta, kelas):
        self.id_reg = id_reg
        self.peserta = peserta
        self.kelas = kelas
        self.total = kelas.harga

    @staticmethod
    def buat_va(bank, id_reg):
        return f"88000-{bank[:3].upper()}-{id_reg}"

    def pakai_promo(self, kode):
        if kode.upper() == "BIGMOVE03":
            self.total *= 0.85
            print("-> Promo BIGMOVE03 Berhasil! Diskon 15%.")
        else:
            print("-> Kode promo tidak valid, menggunakan harga normal.")

    def bayar(self, bank):
        if self.kelas.kuota <= 0:
            raise MasterClassException("Kuota kelas sudah habis!")
        
        self.kelas.kuota -= 1
        va = Pendaftaran.buat_va(bank, self.id_reg)
        self.peserta.riwayat.append(self)
        print(f"[BANK {bank}] Transfer VA: {va} | Total: Rp{self.total:,.0f} -> SUKSES!")

    def __str__(self):
        return f"{self.id_reg} | {self.kelas.judul} | Total: Rp{self.total:,.0f}"

class App:
    def __init__(self):
        self.kelas = [
            MasterClass("MC-01", "Paket Investors", "Ceasar", 1500000, 10),
            MasterClass("MC-02", "Paket Revalue Investors", "Faza", 2500000, 5),
            MasterClass("MC-03", "Paket TOP G (Hybrid Lunch)", "Jove", 5000000, 3)
        ]
        self.reg_count = 0
        self.transaksi = []
        self.users = {
            "student1": Peserta("U01", "Muhammad Nur Ghozali Al Akbar", "pass123"),
            "admin1": Admin("A01", "Admin Revalue", "admin123")
        }

    def run(self):
        while True:
            u = input("\nUsername: ")
            p = input("Password: ")
            user = self.users.get(u)
            if user and user.check_pwd(p):
                self.session(user)
            else:
                print("Login gagal!")

    def session(self, user):
        while True:
            user.menu()
            p = input("Pilih: ")
            if isinstance(user, Peserta):
                if p == "1":
                    for k in self.kelas: 
                        print(k)
                elif p == "2":
                    for k in self.kelas: 
                        print(k)
                    id_k = input("ID Kelas: ").upper()
                    k_opt = next((k for k in self.kelas if k.id_k == id_k), None)
                    if k_opt:
                        self.reg_count += 1
                        reg = Pendaftaran(f"REG-{self.reg_count}", user, k_opt)
                        if input("Ada promo? (y/n): ").lower() == 'y':
                            reg.pakai_promo(input("Kode Promo: "))
                        bank = input("Pilih Bank (BCA/Mandiri/BRI): ").upper()
                        try:
                            reg.bayar(bank)
                            self.transaksi.append(reg)
                        except MasterClassException as e:
                            print(f"Error: {e}")
                    else:
                        print("Kelas tidak ditemukan!")
                elif p == "3":
                    for r in user.riwayat:
                        print(r)
                elif p == "4": 
                    break
            elif isinstance(user, Admin):
                if p == "1":
                    self.kelas.append(MasterClass(
                        f"MC-0{len(self.kelas)+1}", 
                        input("Judul: "), 
                        input("Mentor: "), 
                        float(input("Harga: ")), 
                        int(input("Kuota: "))
                    ))
                    print("Kelas ditambahkan!")
                elif p == "2":
                    tot = sum(t.total for t in self.transaksi)
                    for t in self.transaksi:
                        print(f"{t.id_reg} | {t.peserta.nama} | {t.kelas.judul} | Rp{t.total:,.0f}")
                    print(f"TOTAL OMSET: Rp{tot:,.0f}")
                elif p == "3": 
                    break

if __name__ == "__main__":
    App().run()
