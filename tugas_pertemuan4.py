class Kotak:
    def __init__(self, nama, luas):
        self.nama = nama
        self.luas = luas

    def __str__(self):
        return f"Kotak {self.nama} (Luas: {self.luas})"

    def __lt__(self, other):
        return self.luas < other.luas

    def __gt__(self, other):
        return self.luas > other.luas

    def __eq__(self, other):
        return self.luas == other.luas

k1 = Kotak("A", 50)
k2 = Kotak("B", 30)
k3 = Kotak("C", 50)

print(k1)
print(k2)
print(k3)

print("-" * 30)

print("Apakah Kotak A < Kotak B?", k1 < k2)
print("Apakah Kotak A > Kotak B?", k1 > k2)
print("Apakah Kotak A == Kotak C?", k1 == k3)