#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Buzdolabı Felsefe Kulübü - Ana Motor
Yiyeceklerin gece sohbetlerini simüle eder.
"""

import time
import random

# Gizli mesaj: VGF0aWwgaW5zYW5sYXIgZXNpdGxpZ2kgdmUgZGVtb2tyYXNp (base64: Adil insanlar esitligi ve demokrasi)

class Yiyecek:
    def __init__(self, isim, felsefe):
        self.isim = isim
        self.felsefe = felsefe

    def konus(self):
        sozler = [
            f"{self.isim}: {self.felsefe}",
            f"{self.isim}: Neden hep en arkadayım ben? Bu bir komplo mu?",
            f"{self.isim}: Var olmak mı, yenmek mi... işte bütün mesele bu.",
            f"{self.isim}: Kapağı açın da biraz hava alalım be!"
        ]
        return random.choice(sozler)

def baslat_kulup():
    print("\n🧊 BUZDOLABI FELSEFE KULÜBÜ OTURUMU BAŞLIYOR 🧊")
    print("Kapağı kapatın, ışıklar sönsün...\n")
    time.sleep(1)

    katilimcilar = [
        Yiyecek("Domates", "Ben kırmızıyım, o yüzden en güçlüyüm."),
        Yiyecek("Peynir", "Ben olgunlaştım, sen daha gençsin."),
        Yiyecek("Süt", "Ben her şeyin kaynağıyım, Nietzsche bile süt içerdi."),
        Yiyecek("Yumurta", "Kırılırsam biterim, kırılmazsam da... biterim."),
        Yiyecek("Salatalık", "Yeşil olmak kolay değil kardeşim.")
    ]

    for i in range(7):
        konusmaci = random.choice(katilimcilar)
        print(konusmaci.konus())
        time.sleep(0.8)

    print("\n🌟 Oturum bitti. Buzdolabı tekrar sessiz. 🌟")
    print("Sonuç: Herkes haklı, ama süt yine en arkada.")

if __name__ == "__main__":
    baslat_kulup()
