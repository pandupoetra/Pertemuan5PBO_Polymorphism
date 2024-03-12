class Ammar:
    def sifat(self):
        print("Ammar memilki sifat emosional")
    def umur(self):
        print("umur 17 tahun")
    def hobi(self):
        print("Sepak bola")
    
class Izul:
    def sifat(self):
        print("Izul memilki sifat penyabar")
    def umur(self):
        print("umur 18 tahun")
    def hobi(self):
        print("Badminton")
        
Ammar=Ammar()
Izul=Izul()

for orang in (Ammar,Izul):
    orang.sifat()
    orang.umur()
    orang.hobi()
    print("")
