class Hewan():
    def sifat_alami(self):
       print("Hewan adalah mahluk ciptaan tuhan")
    def suara(self):
      print("Ada berbagai jenis suara dari hewan")

class Domba(Hewan): 
    def suara(self):
       print("Embek")
    def harapan_hidup(self): 
      print("Rat-rata harapan hidup domba adalah 10-15 tahun.") 
    def warna_tubuh(self): 
      print("Warna tubuh kambing pada umumnya adalah putih") 
   
class Kucing(Hewan): 
    def suara(self):
      print("Meow")
    def harapan_hidup(self): 
      print("Rata-rata harapan hidup kucing adalah 10 tahun.") 
   
    def warna_tubuh(self): 
      print("Warna tubuh kucing pada umumnya adalah kuning") 
   
objek_1 = Domba() 
objek_2 = Kucing() 
for type in (objek_1, objek_2): 
    type.sifat_alami()
    type.suara()
    type.harapan_hidup() 
    type.warna_tubuh() 
    print("")