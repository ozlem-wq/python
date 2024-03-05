"""
Film Kütüphanesi
Sayfalar:
    1- Ana Sayfa
    2- Film Listesi
    3- Film Detayı
"""

from widget import Window, SolFrame, SagFrame

if __name__ == '__main__':

    # Ana Pencere
    pencere = Window('Film Kütüphanesi')

    # SOL FRAME
    sol_frame = SolFrame(pencere.window, 'solFrame')

    # SAĞ FRAME
    sag_frame = SagFrame(pencere.window, 'sagFrame')

    # pencerimizi başlat -> mainloop()
    pencere.start_window()
