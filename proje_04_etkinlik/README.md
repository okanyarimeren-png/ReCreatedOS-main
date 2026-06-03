# Proje 4: Etkinlik Kayıt Sistemi

## Amaç
Etkinliklere katılımcı kaydeden, bilet üreten ve doluluk raporu sunan basit bir kayıt sistemi. Konsol tabanlı menü ile yönetilir, veriler bellekte (liste) saklanır.

## Sistemin İşlevleri
- Etkinlik ekleme ve listeleme (kapasiteli)
- Katılımcı ekleme ve listeleme
- Bir katılımcıya etkinlik bileti oluşturma (kapasite ve mükerrer kayıt kontrolü ile)
- Tüm biletleri listeleme
- Her etkinliğin **katılım raporu** (kaç kişi katıldı / doluluk yüzdesi) — istenen ek özellik

## Kullanıcı Türleri
- **Operatör**: Menüyü kullanan kişidir. Etkinlik, katılımcı ve bilet işlemlerini yapar.
- **Katılımcı**: Sisteme kayıtlı son kullanıcı (`Katılımcı` sınıfı ile temsil edilir).

## Sınıflar

### `Etkinlik` (siniflar.py)
| Özellik | Açıklama |
|---|---|
| `etkinlik_id` | Benzersiz etkinlik kimliği |
| `ad` | Etkinlik adı |
| `tarih` | Tarih (string, gg.aa.yyyy) |
| `kapasite` | Maksimum katılımcı sayısı |
| `katilimcilar` | Kayıtlı katılımcılar (List) |

**Metodlar:**
- `katilimci_ekle(katilimci)` — kapasite ve duplicate kontrolü yapıp katılımcı ekler.
- `katilimci_sayisi()` — kayıtlı katılımcı sayısını döner.

### `Katılımcı` (siniflar.py)
| Özellik | Açıklama |
|---|---|
| `katilimci_id` | Katılımcı kimliği |
| `ad` | Ad soyad |
| `email` | E-posta |
| `biletler` | Sahip olduğu biletler (List) |

### `Bilet` (siniflar.py)
| Özellik | Açıklama |
|---|---|
| `bilet_id` | Bilet kimliği |
| `etkinlik` | İlgili Etkinlik nesnesi |
| `katilimci` | İlgili Katılımcı nesnesi |

**Metod:** `bilet_olustur(bilet_listesi)` — katılımcıyı etkinliğe ekler, bileti hem katılımcının hem sistemin listesine yazar.

## Veri Yapıları
- `etkinlikler` (List), `katilimcilar` (List), `biletler` (List)
- Her etkinliğin `katilimcilar` listesi ve her katılımcının `biletler` listesi vardır.

## Çalıştırma

**Konsol arayüzü:**
```bash
cd proje_04_etkinlik
python3 main.py
```

**Grafik arayüz (customtkinter — modern dark theme):**
```bash
cd proje_04_etkinlik
pip install -r requirements.txt   # ilk seferde
python3 arayuz.py
```

Açılışta 3 örnek etkinlik ve 4 örnek katılımcı otomatik yüklenir. **"Python Workshop"** etkinliğinin kapasitesi sadece 3'tür — kapasite testi için kullanılabilir.

> `customtkinter` kütüphanesi `tkinter` üzerine kuruludur. Eğer `pip install` "externally-managed-environment" hatası verirse: `pip install --break-system-packages -r requirements.txt` veya bir venv kullanabilirsin.

## Örnek Senaryo
1. Menüden **1** → mevcut etkinlikleri gör (doluluk `0/3`, `0/100`, `0/50`).
2. Menüden **6** → Python Workshop'a (ID 1) 3 katılımcıyı tek tek kaydet.
3. 4. bir kayıt denenirse "etkinlik dolu" hatası alınır.
4. Menüden **7** → katılım raporu, doluluk yüzdesi ve katılımcı isimlerini gösterir.

## OOP Prensipleri
- **Kapsülleme**: Her etkinlik kendi katılımcı listesini ve kapasitesini yönetir.
- **Sorumluluk ayrımı**: Kapasite kontrolü `Etkinlik` sınıfında, bilet üretme akışı `Bilet` sınıfında.
- **İlişki**: Bir `Bilet` bir `Etkinlik` ve bir `Katılımcı` nesnesini referans olarak tutar.
