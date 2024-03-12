class Bentuk:
    def intro(self):
        return "Bentuk"

class Segitiga(Bentuk):
    def __init__(self, tinggi, alas):
        self.tinggi = tinggi
        self.alas = alas
    def __add__(self, other):
        return 0.5 * (self.alas * self.tinggi + other.alas * other.tinggi)
    def __sub__(self, other):
        return abs(0.5 * (self.alas * self.tinggi - other.alas * other.tinggi))

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi
    def __add__(self, other):
        return self.sisi**2 + other.sisi**2
    def __sub__(self, other):
        return abs(self.sisi**2 - other.sisi**2)

Segitiga1 = Segitiga(5, 3)
Segitiga2 = Segitiga(4, 2)
Persegi1 = Persegi(4)
Persegi2 = Persegi(2)

print("Hasil penambahan dua segitiga:", Segitiga1 + Segitiga2)
print("Hasil pengurangan dua segitiga:", Segitiga1 - Segitiga2)
print("Hasil penambahan dua persegi panjang:",Persegi1 + Persegi2 )
print("Hasil pengurangan dua persegi panjang:",Persegi1 - Persegi2 )
