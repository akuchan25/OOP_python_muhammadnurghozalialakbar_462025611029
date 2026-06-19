class SaldoMinimalError(Exception):
    def __init__(self, pesan="Penarikan gagal! Saldo tidak mencukupi atau di bawah batas minimal."):
        self.pesan = pesan
        super().__init__(self.pesan)

class InputNegatifError(Exception):
    def __init__(self, pesan="Nominal transaksi tidak boleh negatif atau nol!"):
        self.pesan = pesan
        super().__init__(self.pesan)

class RekeningBank:
    def __init__(self, pemilik, saldo_awal):
        self.pemilik = pemilik
        self.__saldo = saldo_awal

    def get_saldo(self):
        return self.__saldo

    def tarik_tunai(self, jumlah):
        print(f"\n--- Memulai Proses Penarikan Rp{jumlah:,} ---")
        if jumlah <= 0:
            raise InputNegatifError(f"Gagal: Anda mencoba memasukkan nominal Rp{jumlah:,}.")
        if jumlah > self.__saldo:
            raise SaldoMinimalError(f"Gagal: Saldo Anda Rp{self.__saldo:,}, tidak cukup untuk menarik Rp{jumlah:,}.")
        self.__saldo -= jumlah
        print(f"Berhasil! Penarikan Rp{jumlah:,} sukses.")
        print(f"Sisa saldo Anda saat ini: Rp{self.__saldo:,}")

if __name__ == "__main__":
    akun_user = RekeningBank("budi", 1000000)
    daftar_transaksi = [200000, -50000, 1500000]

    for nominal in daftar_transaksi:
        try:
            akun_user.tarik_tunai(nominal)
        except InputNegatifError as e:
            print(f"[ERROR INPUT] {e}")
        except SaldoMinimalError as e:
            print(f"[ERROR SALDO] {e}")
        except Exception as e:
            print(f"[ERROR SYSTEM] Terjadi kesalahan tak terduga: {e}")
        finally:
            print("Pesan Sistem: Proses pemeriksaan transaksi selesai dilakukan.")
            print("="*50)