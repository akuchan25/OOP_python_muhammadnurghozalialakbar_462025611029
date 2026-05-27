class Hewan:
    def bersuara(self):
        print("Hewan ini mengeluarkan suara.")

class Kucing(Hewan):
    def bersuara(self):
        print("Meong! Meong!")

class Anjing(Hewan):
    def bersuara(self):
        print("Guk! Guk!")

def cetak_suara(objek_hewan):
    objek_hewan.bersuara()

pet1 = Kucing()
pet2 = Anjing()

print("=== UJI METHOD OVERRIDING ===")
pet1.bersuara()
pet2.bersuara()

print("\n=== UJI DUCK TYPING ===")
cetak_suara(pet1)
cetak_suara(pet2)