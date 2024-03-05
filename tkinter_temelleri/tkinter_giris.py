"""
tkinter
GUI (Graphical User Interface) oluşturma aracı

1- import
2- Ana Sayfa (Main Window)
3- Widget ekle ....
4- Mainloop (sonlandırmaya kadar bekler)
"""

import tkinter as tk

# ana sayfa
m = tk.Tk()


#
# Widget'ler
#


# mainloop
m.mainloop()

"""
Widget'ların tkinter ana sayfası (main window) yerleştirilmesi
1- pack() -> widget'ları ard arda sıralar (yan yana)
2- grid() -> satır, sütun üzerinden yerleştirir
3- place() -> istediğiniz noktaya tam olarak yerleştirir (x=100, y=300 text unit)
"""
