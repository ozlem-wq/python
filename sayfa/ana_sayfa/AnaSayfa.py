import tkinter as tk
from PIL import Image, ImageTk

class AnaSayfa:
    """Ana Sayfa frame'dir."""

    def __init__(self, window, fon_rengi, relief=tk.SUNKEN, side=tk.LEFT):
        # AnaSayfa sınıfının başlatıcı metodu

        self.frame = tk.Frame(
            master=window,
            name='anaSayfa',
            relief=relief,# Çerçeve stili (tk.SUNKEN, tk.RAISED, tk.FLAT, tk.SOLID, tk.GROOVE, tk.RIDGE)
            bg=fon_rengi # Arka plan rengi
        )
        self.side = side
        self.frame_icerigi()# Çerçeve içeriğini oluşturan metodu çağır
        self.frame_ekle() # Çerçeveyi ana pencereye ekle


    def frame_ekle(self):
        self.frame.pack(side=self.side, fill=tk.BOTH, expand=True)

    def frame_icerigi(self):

        tanitim = tk.Label(self.frame,
                           text='',
                           font=('Helvetica', 18, 'bold'),
                           bg='orange')
        tanitim.place(x=315, y=50)

        isim = tk.Label(self.frame,
                        text='(Özlem)',
                        font=('Helvetica', 18, 'bold'),
                        bg='orange')
        isim.place(x=324, y=105)

        self.render_image()

        proje = tk.Label(self.frame,
                        text='Staj Projesi: Tkinter ile Film Kütüphanesi',
                        font=('Helvetica', 18, 'bold'),
                        bg='black',
                        fg='white')
        proje.place(x=140, y=765)


    def render_image(self):
        load = Image.open("images/home/python_logo.png")
        render = ImageTk.PhotoImage(load)# Tkinter için uygun formata dönüştür
        img_lbl = tk.Label(self.frame, image=render, bg='orange')
        img_lbl.image = render
        img_lbl.place(x=136, y=180)