"""
Etkinlik Kayit Sistemi - Ana Program
Konsol tabanli menu ile etkinlik, katilimci ve bilet islemleri yapilir.
"""

from siniflar import Etkinlik, Katilimci, Bilet


# Sistemdeki tum verileri tutan listeler
etkinlikler = []
katilimcilar = []
biletler = []


def ornek_veri_yukle():
    """Test icin baslangic verilerini ekler."""
    etkinlikler.append(Etkinlik(1, "Python Workshop", "20.06.2026", 3))
    etkinlikler.append(Etkinlik(2, "Veri Bilimi Konferansi", "15.07.2026", 100))
    etkinlikler.append(Etkinlik(3, "Yapay Zeka Semineri", "01.08.2026", 50))

    katilimcilar.append(Katilimci(1, "Ahmet Yilmaz", "ahmet@mail.com"))
    katilimcilar.append(Katilimci(2, "Ayse Demir", "ayse@mail.com"))
    katilimcilar.append(Katilimci(3, "Mehmet Kaya", "mehmet@mail.com"))


def etkinlikleri_listele():
    """Tum etkinlikleri ekrana yazdirir."""
    print("\n--- ETKINLIKLER ---")
    if not etkinlikler:
        print("Kayitli etkinlik yok.")
        return
    for e in etkinlikler:
        print(e)


def katilimcilari_listele():
    """Tum katilimcilari ekrana yazdirir."""
    print("\n--- KATILIMCILAR ---")
    if not katilimcilar:
        print("Kayitli katilimci yok.")
        return
    for k in katilimcilar:
        print(k)


def biletleri_listele():
    """Tum biletleri ekrana yazdirir."""
    print("\n--- BILETLER ---")
    if not biletler:
        print("Henuz bilet olusturulmamis.")
        return
    for b in biletler:
        print(b)


def etkinlik_ekle():
    """Yeni etkinlik ekler."""
    etkinlik_id = len(etkinlikler) + 1
    ad = input("Etkinlik adi: ")
    tarih = input("Tarih (gg.aa.yyyy): ")
    try:
        kapasite = int(input("Kapasite: "))
    except ValueError:
        print("Gecersiz kapasite.")
        return
    etkinlikler.append(Etkinlik(etkinlik_id, ad, tarih, kapasite))
    print("Etkinlik eklendi.")


def katilimci_ekle_menu():
    """Yeni katilimci ekler."""
    katilimci_id = len(katilimcilar) + 1
    ad = input("Ad Soyad: ")
    email = input("Email: ")
    katilimcilar.append(Katilimci(katilimci_id, ad, email))
    print("Katilimci eklendi.")


def etkinlik_bul(etkinlik_id):
    """ID ile etkinlik bulur."""
    for e in etkinlikler:
        if e.etkinlik_id == etkinlik_id:
            return e
    return None


def katilimci_bul(katilimci_id):
    """ID ile katilimci bulur."""
    for k in katilimcilar:
        if k.katilimci_id == katilimci_id:
            return k
    return None


def bilet_olustur_menu():
    """Bir katilimciya bilet olusturur."""
    etkinlikleri_listele()
    katilimcilari_listele()
    try:
        e_id = int(input("Etkinlik ID: "))
        k_id = int(input("Katilimci ID: "))
    except ValueError:
        print("Gecersiz giris.")
        return

    etkinlik = etkinlik_bul(e_id)
    katilimci = katilimci_bul(k_id)
    if not etkinlik or not katilimci:
        print("Etkinlik veya katilimci bulunamadi.")
        return

    bilet_id = len(biletler) + 1
    bilet = Bilet(bilet_id, etkinlik, katilimci)
    bilet.bilet_olustur(biletler)


def katilim_raporu():
    """Her etkinlige kac kisi katildigini gosterir (ek ozellik)."""
    print("\n--- KATILIM RAPORU ---")
    if not etkinlikler:
        print("Etkinlik yok.")
        return
    for e in etkinlikler:
        oran = (e.katilimci_sayisi() / e.kapasite) * 100 if e.kapasite else 0
        print(f"{e.ad}: {e.katilimci_sayisi()} / {e.kapasite} kisi (%{oran:.0f} doluluk)")
        for kat in e.katilimcilar:
            print(f"   - {kat.ad}")


def menu():
    """Ana menuyu calistirir."""
    ornek_veri_yukle()
    while True:
        print("\n===== ETKINLIK KAYIT SISTEMI =====")
        print("1. Etkinlikleri listele")
        print("2. Katilimcilari listele")
        print("3. Biletleri listele")
        print("4. Yeni etkinlik ekle")
        print("5. Yeni katilimci ekle")
        print("6. Bilet olustur (etkinlige kayit)")
        print("7. Katilim raporu")
        print("0. Cikis")
        secim = input("Seciminiz: ").strip()

        if secim == "1":
            etkinlikleri_listele()
        elif secim == "2":
            katilimcilari_listele()
        elif secim == "3":
            biletleri_listele()
        elif secim == "4":
            etkinlik_ekle()
        elif secim == "5":
            katilimci_ekle_menu()
        elif secim == "6":
            bilet_olustur_menu()
        elif secim == "7":
            katilim_raporu()
        elif secim == "0":
            print("Cikis yapiliyor...")
            break
        else:
            print("Gecersiz secim, tekrar deneyin.")


if __name__ == "__main__":
    menu()
