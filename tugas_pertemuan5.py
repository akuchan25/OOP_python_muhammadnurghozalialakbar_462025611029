class AkunGame:
    def __init__(self, nickname, email, password):
        self.nickname = nickname
        
        self.__email = email
        self.__password = password
        self.__level = 1

    def get_email(self, konfirmasi_pass):
        if konfirmasi_pass == self.__password:
            return self.__email
        else:
            return "Password Salah! Akses ditolak."

    def set_level(self, level_baru):
        if level_baru > self.__level:
            self.__level = level_baru
            print(f"Selamat! Level berhasil naik menjadi: {self.__level}")
        else:
            print("Gagal: Level baru harus lebih tinggi dari level saat ini!")

player1 = AkunGame("Ghozali_Akbar", "ghozali@email.com", "pass123")

print(f"Player Nickname: {player1.nickname}")
print("-" * 35)

print("Cek Email (Password Salah) :", player1.get_email("salah_ketik"))
print("Cek Email (Password Benar) :", player1.get_email("pass123"))
print("-" * 35)

player1.set_level(0)
player1.set_level(10)