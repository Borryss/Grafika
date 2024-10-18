from PIL import Image
import numpy as np

def rysuj_ramki_szare(w, h, grub, kolor):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    koef = min(int(w / (2*grub)), int(h / (2*grub)))
    print(koef)
    for i in range(0, koef):

        if(i % 2 == 0):
            tab[grub*i:(h - grub*i), grub*i:(w - grub*i)] = (kolor + 15*i) % 256

        else:
            tab[grub*i:(h - grub*i), grub*i:(w - grub*i)] = (120 + 10*i) % 256

    return Image.fromarray(tab)

#rysuj_ramki_szare(400, 600, 20, 50).show()

def rysuj_pasy_pionowe_szare(w, h, grub, kolor):
    t = (h, w)
    tab = np.ones(t, dtype=np.uint8)
    ile = int(w / grub)
    print(ile)
    for k in range(ile):
        for g in range(grub):
            i = k * grub + g
            for j in range(h):
                tab[j, i] = kolor
        kolor = (kolor + 15) % 256
    return Image.fromarray(tab)

rysuj_pasy_pionowe_szare(300, 400, 50, 50).show()
