class daigaku:
    namae = ''
    gakubu = ''

    @staticmethod
    def kougishitsu():
        print('Fakultas Teknik memiliki laboratorium yang sangat bagus.')

    def touroku(self):
        print(f'Universitas {self.namae} membuka pendaftaran jurusan {self.gakubu}.')

daigaku1 = daigaku()
daigaku1.namae = 'Todai'
daigaku1.gakubu = 'Teknik Informatika'

daigaku2 = daigaku()
daigaku2.namae = 'Kyodai'
daigaku2.gakubu = 'Sistem Informasi'

daigaku.kougishitsu()

print("-" * 50)

daigaku1.touroku()

daigaku2.touroku()