"""
Etkinlik Kayit Sistemi - Sinif Tanimlari
Bu dosyada Etkinlik, Katilimci ve Bilet siniflari yer alir.
"""


class Etkinlik:
    """Sistemdeki bir etkinligi temsil eder."""

    def __init__(self, etkinlik_id, ad, tarih, kapasite):
        self.etkinlik_id = etkinlik_id
        self.ad = ad
        self.tarih = tarih  # Ornek: "20.06.2026"
        self.kapasite = kapasite
        # Etkinlige kayitli katilimci nesneleri
        self.katilimcilar = []

    def katilimci_ekle(self, katilimci):
        """Etkinlige yeni bir katilimci ekler. Kapasite kontrolu yapar."""
        if len(self.katilimcilar) >= self.kapasite:
            print(f"HATA: '{self.ad}' etkinligi dolu (kapasite {self.kapasite}).")
            return False
        if katilimci in self.katilimcilar:
            print(f"HATA: {katilimci.ad} zaten bu etkinlige kayitli.")
            return False
        self.katilimcilar.append(katilimci)
        print(f"{katilimci.ad}, '{self.ad}' etkinligine eklendi.")
        return True

    def katilimci_sayisi(self):
        """Etkinlige kayitli katilimci sayisini doner."""
        return len(self.katilimcilar)

    def __str__(self):
        return f"[{self.etkinlik_id}] {self.ad} - {self.tarih} ({self.katilimci_sayisi()}/{self.kapasite})"


class Katilimci:
    """Bir katilimciyi temsil eder."""

    def __init__(self, katilimci_id, ad, email):
        self.katilimci_id = katilimci_id
        self.ad = ad
        self.email = email
        # Katilimcinin biletleri
        self.biletler = []

    def __str__(self):
        return f"[{self.katilimci_id}] {self.ad} - {self.email}"


class Bilet:
    """Bir etkinlik biletini temsil eder."""

    def __init__(self, bilet_id, etkinlik, katilimci):
        self.bilet_id = bilet_id
        self.etkinlik = etkinlik
        self.katilimci = katilimci

    def bilet_olustur(self, bilet_listesi):
        """Bileti olusturup ilgili listelere ekler."""
        # Once katilimciyi etkinlige eklemeye calis
        eklendi = self.etkinlik.katilimci_ekle(self.katilimci)
        if not eklendi:
            return False
        self.katilimci.biletler.append(self)
        bilet_listesi.append(self)
        print(f"Bilet olusturuldu: #{self.bilet_id}")
        return True

    def __str__(self):
        return f"Bilet #{self.bilet_id} | {self.etkinlik.ad} | {self.katilimci.ad}"
