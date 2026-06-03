"""
Etkinlik Kayit Sistemi - Modern Grafik Arayuz (customtkinter)
Dark mode, yuvarlatilmis koseli, modern bir GUI.
siniflar.py icindeki Etkinlik, Katilimci ve Bilet siniflarini kullanir.
"""

import customtkinter as ctk
from tkinter import ttk, messagebox
import tkinter as tk
from siniflar import Etkinlik, Katilimci, Bilet


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

BG = "#1a1a1a"
CARD_BG = "#212121"
ROW_BG = "#2b2b2b"
ROW_ALT = "#262626"
TEXT = "#e6e6e6"
SUBTEXT = "#9a9a9a"
ACCENT = "#8b5cf6"  # mor
SUCCESS = "#22c55e"
WARNING = "#f59e0b"


class EtkinlikArayuz(ctk.CTk):
    """Modern dark-themed etkinlik kayit arayuzu."""

    def __init__(self):
        super().__init__()
        self.title("Etkinlik Kayıt Sistemi")
        self.geometry("1000x660")
        self.minsize(940, 620)

        self.etkinlikler = []
        self.katilimcilar = []
        self.biletler = []

        self._tema_treeview()
        self._ust_bar()
        self._tab_view()

        self._ornek_veri_yukle()
        self._tablolari_yenile()

    def _tema_treeview(self):
        style = ttk.Style()
        style.theme_use("default")
        style.configure(
            "Modern.Treeview",
            background=ROW_BG, foreground=TEXT,
            fieldbackground=ROW_BG, rowheight=30, borderwidth=0,
            font=("SF Pro Display", 12),
        )
        style.configure(
            "Modern.Treeview.Heading",
            background=CARD_BG, foreground=SUBTEXT,
            relief="flat", font=("SF Pro Display", 11, "bold"),
        )
        style.map("Modern.Treeview",
                  background=[("selected", ACCENT)],
                  foreground=[("selected", "white")])
        style.map("Modern.Treeview.Heading", background=[("active", CARD_BG)])

    def _ust_bar(self):
        header = ctk.CTkFrame(self, height=70, corner_radius=0, fg_color=CARD_BG)
        header.pack(fill="x", side="top")
        header.pack_propagate(False)

        ic = ctk.CTkFrame(header, fg_color="transparent")
        ic.pack(side="left", padx=24, fill="y")
        ctk.CTkLabel(
            ic, text="🎟  Etkinlik Kayıt Sistemi",
            font=ctk.CTkFont(size=22, weight="bold"), text_color=TEXT
        ).pack(side="left", pady=18)
        ctk.CTkLabel(
            ic, text="  •  OOP Ödev Projesi",
            font=ctk.CTkFont(size=13), text_color=SUBTEXT
        ).pack(side="left", pady=18)

        sag = ctk.CTkFrame(header, fg_color="transparent")
        sag.pack(side="right", padx=24, fill="y")

        self.rozet_etkinlik = self._rozet_olustur(sag, "📅", "0", "Etkinlik")
        self.rozet_etkinlik.pack(side="left", padx=6, pady=12)
        self.rozet_katilimci = self._rozet_olustur(sag, "👥", "0", "Katılımcı")
        self.rozet_katilimci.pack(side="left", padx=6, pady=12)
        self.rozet_bilet = self._rozet_olustur(sag, "🎫", "0", "Bilet")
        self.rozet_bilet.pack(side="left", padx=6, pady=12)

    def _rozet_olustur(self, parent, ikon, deger, baslik):
        kart = ctk.CTkFrame(parent, fg_color=BG, corner_radius=10, width=110, height=46)
        kart.pack_propagate(False)
        ic = ctk.CTkFrame(kart, fg_color="transparent")
        ic.pack(expand=True)
        ctk.CTkLabel(ic, text=f"{ikon} ", font=ctk.CTkFont(size=14)) \
            .grid(row=0, column=0, rowspan=2, padx=(6, 2))
        lbl_deger = ctk.CTkLabel(
            ic, text=deger, font=ctk.CTkFont(size=16, weight="bold"), text_color=TEXT
        )
        lbl_deger.grid(row=0, column=1, sticky="w")
        ctk.CTkLabel(ic, text=baslik, font=ctk.CTkFont(size=10),
                     text_color=SUBTEXT).grid(row=1, column=1, sticky="w")
        kart.deger_label = lbl_deger
        return kart

    def _tab_view(self):
        self.tabs = ctk.CTkTabview(
            self, fg_color=BG, segmented_button_selected_color=ACCENT
        )
        self.tabs.pack(fill="both", expand=True, padx=20, pady=(12, 20))

        self.tabs.add("Etkinlikler")
        self.tabs.add("Katılımcılar")
        self.tabs.add("Bilet Oluştur")
        self.tabs.add("Katılım Raporu")

        self._sayfa_etkinlikler(self.tabs.tab("Etkinlikler"))
        self._sayfa_katilimcilar(self.tabs.tab("Katılımcılar"))
        self._sayfa_bilet(self.tabs.tab("Bilet Oluştur"))
        self._sayfa_rapor(self.tabs.tab("Katılım Raporu"))

    # -------- Form yardimcisi --------
    def _form_alani(self, parent, label):
        ctk.CTkLabel(parent, text=label, font=ctk.CTkFont(size=11),
                     text_color=SUBTEXT, anchor="w").pack(fill="x", padx=18, pady=(6, 2))
        e = ctk.CTkEntry(parent, height=36, corner_radius=8,
                         fg_color=BG, border_color="#333", text_color=TEXT)
        e.pack(fill="x", padx=18, pady=(0, 4))
        return e

    # -------- Sayfa: Etkinlikler --------
    def _sayfa_etkinlikler(self, parent):
        sol = ctk.CTkFrame(parent, fg_color=CARD_BG, corner_radius=12)
        sol.pack(side="left", fill="both", expand=True, padx=(0, 10), pady=8)

        ctk.CTkLabel(sol, text="Etkinlik Listesi",
                     font=ctk.CTkFont(size=15, weight="bold"),
                     text_color=TEXT).pack(anchor="w", padx=16, pady=(14, 6))

        tablo_cer = ctk.CTkFrame(sol, fg_color=ROW_BG, corner_radius=8)
        tablo_cer.pack(fill="both", expand=True, padx=16, pady=(0, 16))

        sutunlar = ("id", "ad", "tarih", "doluluk", "kapasite")
        self.tablo_etkinlik = ttk.Treeview(
            tablo_cer, columns=sutunlar, show="headings",
            style="Modern.Treeview", height=18
        )
        for s, baslik, gen in [
            ("id", "ID", 50), ("ad", "Etkinlik", 240),
            ("tarih", "Tarih", 110), ("doluluk", "Kayıtlı", 90),
            ("kapasite", "Kapasite", 90)
        ]:
            self.tablo_etkinlik.heading(s, text=baslik)
            self.tablo_etkinlik.column(s, width=gen, anchor="w")
        self.tablo_etkinlik.pack(fill="both", expand=True, padx=2, pady=2)

        sag = ctk.CTkFrame(parent, fg_color=CARD_BG, corner_radius=12, width=300)
        sag.pack(side="right", fill="y", pady=8)
        sag.pack_propagate(False)

        ctk.CTkLabel(sag, text="Yeni Etkinlik Ekle",
                     font=ctk.CTkFont(size=15, weight="bold"),
                     text_color=TEXT).pack(anchor="w", padx=18, pady=(18, 12))

        self.giris_etk_ad = self._form_alani(sag, "Etkinlik Adı")
        self.giris_etk_tarih = self._form_alani(sag, "Tarih (gg.aa.yyyy)")
        self.giris_etk_kapasite = self._form_alani(sag, "Kapasite")

        ctk.CTkButton(
            sag, text="＋  Etkinlik Ekle", height=42, corner_radius=10,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color=ACCENT, hover_color="#7c3aed",
            command=self._etkinlik_ekle
        ).pack(fill="x", padx=18, pady=(8, 18))

    def _etkinlik_ekle(self):
        ad = self.giris_etk_ad.get().strip()
        tarih = self.giris_etk_tarih.get().strip()
        kap_s = self.giris_etk_kapasite.get().strip()
        if not (ad and tarih and kap_s):
            messagebox.showwarning("Eksik bilgi", "Tüm alanları doldurun.")
            return
        try:
            kapasite = int(kap_s)
            if kapasite <= 0:
                raise ValueError
        except ValueError:
            messagebox.showerror("Hata", "Kapasite pozitif tam sayı olmalı.")
            return
        e_id = len(self.etkinlikler) + 1
        self.etkinlikler.append(Etkinlik(e_id, ad, tarih, kapasite))
        for entry in [self.giris_etk_ad, self.giris_etk_tarih, self.giris_etk_kapasite]:
            entry.delete(0, "end")
        self._tablolari_yenile()

    # -------- Sayfa: Katilimcilar --------
    def _sayfa_katilimcilar(self, parent):
        sol = ctk.CTkFrame(parent, fg_color=CARD_BG, corner_radius=12)
        sol.pack(side="left", fill="both", expand=True, padx=(0, 10), pady=8)

        ctk.CTkLabel(sol, text="Katılımcı Listesi",
                     font=ctk.CTkFont(size=15, weight="bold"),
                     text_color=TEXT).pack(anchor="w", padx=16, pady=(14, 6))

        tablo_cer = ctk.CTkFrame(sol, fg_color=ROW_BG, corner_radius=8)
        tablo_cer.pack(fill="both", expand=True, padx=16, pady=(0, 16))

        sutunlar = ("id", "ad", "email", "bilet")
        self.tablo_katilimci = ttk.Treeview(
            tablo_cer, columns=sutunlar, show="headings",
            style="Modern.Treeview", height=18
        )
        for s, baslik, gen in [
            ("id", "ID", 50), ("ad", "Ad Soyad", 220),
            ("email", "Email", 260), ("bilet", "Bilet", 80)
        ]:
            self.tablo_katilimci.heading(s, text=baslik)
            self.tablo_katilimci.column(s, width=gen, anchor="w")
        self.tablo_katilimci.pack(fill="both", expand=True, padx=2, pady=2)

        sag = ctk.CTkFrame(parent, fg_color=CARD_BG, corner_radius=12, width=300)
        sag.pack(side="right", fill="y", pady=8)
        sag.pack_propagate(False)

        ctk.CTkLabel(sag, text="Yeni Katılımcı Ekle",
                     font=ctk.CTkFont(size=15, weight="bold"),
                     text_color=TEXT).pack(anchor="w", padx=18, pady=(18, 12))

        self.giris_kat_ad = self._form_alani(sag, "Ad Soyad")
        self.giris_kat_email = self._form_alani(sag, "Email")

        ctk.CTkButton(
            sag, text="＋  Katılımcı Ekle", height=42, corner_radius=10,
            font=ctk.CTkFont(size=13, weight="bold"),
            fg_color=ACCENT, hover_color="#7c3aed",
            command=self._katilimci_ekle
        ).pack(fill="x", padx=18, pady=(8, 18))

    def _katilimci_ekle(self):
        ad = self.giris_kat_ad.get().strip()
        email = self.giris_kat_email.get().strip()
        if not (ad and email):
            messagebox.showwarning("Eksik bilgi", "Ad ve email gerekli.")
            return
        k_id = len(self.katilimcilar) + 1
        self.katilimcilar.append(Katilimci(k_id, ad, email))
        self.giris_kat_ad.delete(0, "end")
        self.giris_kat_email.delete(0, "end")
        self._tablolari_yenile()

    # -------- Sayfa: Bilet Olustur --------
    def _sayfa_bilet(self, parent):
        ust = ctk.CTkFrame(parent, fg_color=CARD_BG, corner_radius=12)
        ust.pack(fill="x", pady=(8, 8))

        ctk.CTkLabel(ust, text="🎫  Yeni Bilet Oluştur",
                     font=ctk.CTkFont(size=15, weight="bold"),
                     text_color=TEXT).pack(anchor="w", padx=18, pady=(18, 12))

        form_alt = ctk.CTkFrame(ust, fg_color="transparent")
        form_alt.pack(fill="x", padx=18, pady=(0, 18))

        ctk.CTkLabel(form_alt, text="Etkinlik",
                     font=ctk.CTkFont(size=11), text_color=SUBTEXT,
                     anchor="w").grid(row=0, column=0, sticky="w", padx=(0, 6))
        self.combo_etkinlik = ctk.CTkComboBox(
            form_alt, height=38, state="readonly", width=380,
            fg_color=BG, border_color="#333",
            button_color=ACCENT, dropdown_fg_color=CARD_BG
        )
        self.combo_etkinlik.grid(row=1, column=0, sticky="we", padx=(0, 12))
        self.combo_etkinlik.set("")

        ctk.CTkLabel(form_alt, text="Katılımcı",
                     font=ctk.CTkFont(size=11), text_color=SUBTEXT,
                     anchor="w").grid(row=0, column=1, sticky="w", padx=(0, 6))
        self.combo_katilimci = ctk.CTkComboBox(
            form_alt, height=38, state="readonly", width=300,
            fg_color=BG, border_color="#333",
            button_color=ACCENT, dropdown_fg_color=CARD_BG
        )
        self.combo_katilimci.grid(row=1, column=1, sticky="we", padx=(0, 12))
        self.combo_katilimci.set("")

        ctk.CTkButton(
            form_alt, text="🎫  Bilet Oluştur", height=38, corner_radius=10,
            font=ctk.CTkFont(size=12, weight="bold"),
            fg_color=SUCCESS, hover_color="#16a34a",
            command=self._bilet_olustur
        ).grid(row=1, column=2, sticky="w")

        # Olusturulan biletler tablosu
        alt = ctk.CTkFrame(parent, fg_color=CARD_BG, corner_radius=12)
        alt.pack(fill="both", expand=True, pady=8)

        ctk.CTkLabel(alt, text="Oluşturulan Biletler",
                     font=ctk.CTkFont(size=15, weight="bold"),
                     text_color=TEXT).pack(anchor="w", padx=18, pady=(18, 8))

        tablo_cer = ctk.CTkFrame(alt, fg_color=ROW_BG, corner_radius=8)
        tablo_cer.pack(fill="both", expand=True, padx=18, pady=(0, 18))

        sutunlar = ("id", "etkinlik", "katilimci")
        self.tablo_bilet = ttk.Treeview(
            tablo_cer, columns=sutunlar, show="headings",
            style="Modern.Treeview", height=12
        )
        for s, baslik, gen in [
            ("id", "Bilet #", 80), ("etkinlik", "Etkinlik", 320),
            ("katilimci", "Katılımcı", 240)
        ]:
            self.tablo_bilet.heading(s, text=baslik)
            self.tablo_bilet.column(s, width=gen, anchor="w")
        self.tablo_bilet.pack(fill="both", expand=True, padx=2, pady=2)

    def _bilet_olustur(self):
        e_secim = self.combo_etkinlik.get()
        k_secim = self.combo_katilimci.get()
        e_degerler = list(self.combo_etkinlik.cget("values"))
        k_degerler = list(self.combo_katilimci.cget("values"))
        if e_secim not in e_degerler or k_secim not in k_degerler:
            messagebox.showwarning("Eksik seçim", "Etkinlik ve katılımcı seçin.")
            return
        etkinlik = self.etkinlikler[e_degerler.index(e_secim)]
        katilimci = self.katilimcilar[k_degerler.index(k_secim)]

        if len(etkinlik.katilimcilar) >= etkinlik.kapasite:
            messagebox.showerror("Hata",
                                 f"'{etkinlik.ad}' dolu (kapasite {etkinlik.kapasite}).")
            return
        if katilimci in etkinlik.katilimcilar:
            messagebox.showerror("Hata",
                                 f"{katilimci.ad} zaten bu etkinliğe kayıtlı.")
            return

        b_id = len(self.biletler) + 1
        bilet = Bilet(b_id, etkinlik, katilimci)
        if bilet.bilet_olustur(self.biletler):
            messagebox.showinfo("Tamam", f"Bilet #{bilet.bilet_id} oluşturuldu.")
        self._tablolari_yenile()

    # -------- Sayfa: Rapor --------
    def _sayfa_rapor(self, parent):
        kart = ctk.CTkFrame(parent, fg_color=CARD_BG, corner_radius=12)
        kart.pack(fill="both", expand=True, pady=8)

        ust = ctk.CTkFrame(kart, fg_color="transparent")
        ust.pack(fill="x", padx=18, pady=(18, 8))

        ctk.CTkLabel(ust, text="📊  Katılım Raporu",
                     font=ctk.CTkFont(size=15, weight="bold"),
                     text_color=TEXT).pack(side="left")

        ctk.CTkButton(
            ust, text="↻  Yenile", height=32, corner_radius=8,
            fg_color=BG, hover_color="#2a2a2a", text_color=TEXT,
            command=self._raporu_yenile
        ).pack(side="right")

        # Rapor karti icinde scrollable frame
        self.rapor_alani = ctk.CTkScrollableFrame(kart, fg_color=BG, corner_radius=8)
        self.rapor_alani.pack(fill="both", expand=True, padx=18, pady=(0, 18))

    def _raporu_yenile(self):
        # Eski iceriği temizle
        for w in self.rapor_alani.winfo_children():
            w.destroy()

        if not self.etkinlikler:
            ctk.CTkLabel(self.rapor_alani, text="Etkinlik yok.",
                         text_color=SUBTEXT).pack(pady=20)
            return

        for e in self.etkinlikler:
            oran = (e.katilimci_sayisi() / e.kapasite) * 100 if e.kapasite else 0
            kart = ctk.CTkFrame(self.rapor_alani, fg_color=CARD_BG, corner_radius=10)
            kart.pack(fill="x", padx=4, pady=6)

            ust = ctk.CTkFrame(kart, fg_color="transparent")
            ust.pack(fill="x", padx=14, pady=(12, 6))

            ctk.CTkLabel(ust, text=e.ad,
                         font=ctk.CTkFont(size=14, weight="bold"),
                         text_color=TEXT).pack(side="left")
            ctk.CTkLabel(ust, text=f"  {e.tarih}",
                         font=ctk.CTkFont(size=11),
                         text_color=SUBTEXT).pack(side="left")
            ctk.CTkLabel(
                ust, text=f"{e.katilimci_sayisi()} / {e.kapasite}  •  %{oran:.0f}",
                font=ctk.CTkFont(size=12, weight="bold"),
                text_color=ACCENT
            ).pack(side="right")

            # Progress bar
            bar = ctk.CTkProgressBar(kart, height=8, corner_radius=4,
                                     progress_color=ACCENT, fg_color=BG)
            bar.set(min(oran / 100, 1.0))
            bar.pack(fill="x", padx=14, pady=(4, 8))

            if e.katilimcilar:
                isimler = ", ".join(k.ad for k in e.katilimcilar)
                ctk.CTkLabel(kart, text=isimler,
                             font=ctk.CTkFont(size=11),
                             text_color=SUBTEXT, anchor="w",
                             wraplength=800, justify="left").pack(
                    fill="x", padx=14, pady=(0, 12))
            else:
                ctk.CTkLabel(kart, text="(kayıtlı katılımcı yok)",
                             font=ctk.CTkFont(size=11),
                             text_color=SUBTEXT, anchor="w").pack(
                    fill="x", padx=14, pady=(0, 12))

    # -------- Yenileme --------
    def _ornek_veri_yukle(self):
        self.etkinlikler.append(Etkinlik(1, "Python Workshop", "20.06.2026", 3))
        self.etkinlikler.append(Etkinlik(2, "Veri Bilimi Konferansı", "15.07.2026", 100))
        self.etkinlikler.append(Etkinlik(3, "Yapay Zeka Semineri", "01.08.2026", 50))
        self.katilimcilar.append(Katilimci(1, "Ahmet Yılmaz", "ahmet@mail.com"))
        self.katilimcilar.append(Katilimci(2, "Ayşe Demir", "ayse@mail.com"))
        self.katilimcilar.append(Katilimci(3, "Mehmet Kaya", "mehmet@mail.com"))
        self.katilimcilar.append(Katilimci(4, "Zeynep Çelik", "zeynep@mail.com"))

    def _tablolari_yenile(self):
        # Etkinlik tablosu
        self.tablo_etkinlik.delete(*self.tablo_etkinlik.get_children())
        for i, e in enumerate(self.etkinlikler):
            tag = "evn" if i % 2 == 0 else "odd"
            self.tablo_etkinlik.insert(
                "", "end",
                values=(e.etkinlik_id, e.ad, e.tarih, e.katilimci_sayisi(), e.kapasite),
                tags=(tag,)
            )
        self.tablo_etkinlik.tag_configure("evn", background=ROW_BG)
        self.tablo_etkinlik.tag_configure("odd", background=ROW_ALT)

        # Katilimci tablosu
        self.tablo_katilimci.delete(*self.tablo_katilimci.get_children())
        for i, k in enumerate(self.katilimcilar):
            tag = "evn" if i % 2 == 0 else "odd"
            self.tablo_katilimci.insert(
                "", "end",
                values=(k.katilimci_id, k.ad, k.email, len(k.biletler)),
                tags=(tag,)
            )
        self.tablo_katilimci.tag_configure("evn", background=ROW_BG)
        self.tablo_katilimci.tag_configure("odd", background=ROW_ALT)

        # Bilet tablosu
        self.tablo_bilet.delete(*self.tablo_bilet.get_children())
        for i, b in enumerate(self.biletler):
            tag = "evn" if i % 2 == 0 else "odd"
            self.tablo_bilet.insert(
                "", "end",
                values=(b.bilet_id, b.etkinlik.ad, b.katilimci.ad),
                tags=(tag,)
            )
        self.tablo_bilet.tag_configure("evn", background=ROW_BG)
        self.tablo_bilet.tag_configure("odd", background=ROW_ALT)

        # Combobox'lar
        self.combo_etkinlik.configure(values=[
            f"[{e.etkinlik_id}] {e.ad}  ({e.katilimci_sayisi()}/{e.kapasite})"
            for e in self.etkinlikler
        ] or [""])
        self.combo_etkinlik.set("")

        self.combo_katilimci.configure(values=[
            f"[{k.katilimci_id}] {k.ad}" for k in self.katilimcilar
        ] or [""])
        self.combo_katilimci.set("")

        # Rozetler
        self.rozet_etkinlik.deger_label.configure(text=str(len(self.etkinlikler)))
        self.rozet_katilimci.deger_label.configure(text=str(len(self.katilimcilar)))
        self.rozet_bilet.deger_label.configure(text=str(len(self.biletler)))

        # Rapor varsa tazele
        if hasattr(self, "rapor_alani"):
            self._raporu_yenile()


if __name__ == "__main__":
    app = EtkinlikArayuz()
    app.mainloop()
