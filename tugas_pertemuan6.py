class Perangkat:
    merek = ""
    daya = ""

    def info_perangkat(self):
        print(f"Merek: {self.merek}, Daya: {self.daya}")

class Laptop(Perangkat):
    ram = ""

    def info_laptop(self):
        print(f"Laptop ini memiliki RAM sebesar {self.ram}")

laptop1 = Laptop()
laptop1.merek = "Asus"
laptop1.daya = "65 Watt"
laptop1.ram = "16 GB"

laptop2 = Laptop()
laptop2.merek = "Lenovo"
laptop2.daya = "45 Watt"
laptop2.ram = "8 GB"

print("=== DATA LAPTOP 1 ===")
laptop1.info_perangkat() 
laptop1.info_laptop()

print("\n=== DATA LAPTOP 2 ===")
laptop2.info_perangkat()
laptop2.info_laptop()