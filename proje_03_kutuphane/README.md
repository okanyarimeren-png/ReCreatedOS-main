# Proje 3: Dijital Kütüphane Sistemi

## Amaç
Bir kütüphanedeki kitapların üyelere ödünç verilmesini ve iade edilmesini takip eden basit bir sistem. Konsol tabanlı menü ile yönetilir, tüm veriler bellekte (liste) tutulur.

## Sistemin İşlevleri
- Kitap ekleme ve listeleme
- Üye ekleme ve listeleme
- Bir üyeye kitap ödünç verme
- Kitabı iade alma
- Tüm ödünç işlemlerinin geçmişini görüntüleme

## Kullanıcı Türleri
- **Yönetici (operatör)**: Konsoldan menüyü kullanan kişidir. Kitap ve üye ekler, ödünç/iade işlemlerini yapar.
- **Üye**: Sisteme kayıtlı kütüphane kullanıcısıdır (`Üye` sınıfı ile temsil edilir).

## Sınıflar

### `Kitap` (siniflar.py)
| Özellik | Açıklama |
|---|---|
| `kitap_id` | Benzersiz kitap kimliği |
| `ad` | Kitap adı |
| `yazar` | Yazar adı |
| `kategori` | Roman, Bilim Kurgu vb. |
| `durum` | "musait" veya "odunc" |

**Metod:** `kitap_durumu_degistir(yeni_durum)` — kitabın durumunu günceller.

### `Üye` (siniflar.py)
| Özellik | Açıklama |
|---|---|
| `uye_id` | Üye kimliği |
| `ad` | Ad soyad |
| `email` | E-posta |
| `aktif_oduncler` | Üyenin elindeki ödünç kayıtları (List) |

**Metodlar:**
- `kitap_odunc_al(kitap, odunc_listesi)` → yeni `Odunc` nesnesi üretir.
- `kitap_iade_et(odunc)` → ödünç kaydı kapatılır, kitap tekrar müsait olur.

### `Ödünç` (siniflar.py)
| Özellik | Açıklama |
|---|---|
| `odunc_id` | Ödünç işlemi kimliği |
| `kitap` | İlgili Kitap nesnesi |
| `uye` | İlgili Üye nesnesi |
| `odunc_tarihi` | Ödünç alındığı tarih (datetime) |
| `son_iade_tarihi` | Planlanan iade tarihi (14 gün sonra) |
| `iade_tarihi` | Gerçek iade tarihi (None ise iade edilmemiş) |

## Veri Yapıları
- `kitaplar` (List) — tüm kitaplar
- `uyeler` (List) — tüm üyeler
- `oduncler` (List) — tüm ödünç işlemleri
- Her üyenin `aktif_oduncler` özelliği kendi ödünçlerini tutar (List)

## Çalıştırma

**Konsol arayüzü:**
```bash
cd proje_03_kutuphane
python3 main.py
```

**Grafik arayüz (customtkinter — modern dark theme):**
```bash
cd proje_03_kutuphane
pip install -r requirements.txt   # ilk seferde
python3 arayuz.py
```

Açılışta 5 örnek kitap ve 3 örnek üye otomatik yüklenir.

> `customtkinter` kütüphanesi `tkinter` üzerine kuruludur. Eğer `pip install` "externally-managed-environment" hatası verirse: `pip install --break-system-packages -r requirements.txt` veya bir venv kullanabilirsin.

## Örnek Senaryo
1. Menüden **1** → kitap listesini gör.
2. Menüden **5** → "Suç ve Ceza" (ID 1) kitabını "Ahmet Yılmaz" (ID 1) üyesine ödünç ver.
3. Menüden **1** → "Suç ve Ceza" kitabının durumu artık `ODUNC`.
4. Menüden **6** → ödünç ID 1'i iade al.
5. Menüden **7** → tüm ödünç geçmişi görülür (iade edilen + edilmeyen).

## OOP Prensipleri
- **Kapsülleme**: Her sınıf kendi verisini kendi içinde tutar.
- **Sorumluluk ayrımı**: Kitap kendi durumunu, üye kendi ödünçlerini yönetir.
- **İlişki**: Bir `Ödünç`, bir `Kitap` ve bir `Üye` nesnesini referans olarak tutar.
