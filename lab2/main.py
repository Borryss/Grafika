from PIL import Image  # Python Imaging Library
import numpy as np

inicjaly = Image.open("bs.bmp")
t_inicjaly = np.asarray(inicjaly)


def rysuj_ramke_w_obrazie(obraz, grub):
    tab_obraz = np.asarray(obraz).astype(np.uint8)  # wczytanie tablicy obrazu i zamiana na int
    h, w = tab_obraz.shape
    for i in range(h):
        for j in range(grub):
            tab_obraz[i][j] = 0
        for j in range(w - grub, w):
            tab_obraz[i][j] = 0
    for j in range(w):
        for i in range(grub):
            tab_obraz[i][j] = 0
        for i in range(h - grub, h):
            tab_obraz[i][j] = 0
    tab = tab_obraz.astype(bool)  # zapisanie tablicy w typie bool (obrazy czarnobiałe)
    return Image.fromarray(tab)

rysuj_ramke_w_obrazie(inicjaly, 5).show()

def  rysuj_ramki(w,h,grub):
    t = (h, w)  # rozmiar tablicy
    tab = np.zeros(t, dtype=np.uint8)  # deklaracja tablicy wypełnionej zerami - czarna
    h2 = h/ (2*grub)
    w2 = w/ (2 * grub)

    print(h2)
    print(w2)

    for i in range(w2):
        tab[grub:h - grub, grub:w - grub] = 1
            print(1)

    tab1 = tab.astype(np.bool_)
    return Image.fromarray(tab1)

rysuj_ramki(200, 100, 20).show()















