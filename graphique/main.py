import tkinter as tk
# import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class App(tk.Tk):
    def __init__(self):
        # Créer une fenêtre
        self.fenetre = tk.Tk()
        self.fenetre.title("Ma fenêtre")
        self.fenetre.geometry("1024x600")
        self.fenetre.title("Menu Navigation")
        
        # Définir l'image de fond
        image_de_fond = tk.PhotoImage(file="fond.gif")
        if image_de_fond.width() > 1024 or image_de_fond.height() > 600:
            image = image_de_fond.subsample(max(image_de_fond.width() // 1024, image_de_fond.height() // 600))

        # menu
        canvas = tk.Canvas(self.fenetre, width=1024, height=600)
        canvas.pack(fill="both")
        canvas.create_image(0, 0, image=image, anchor="nw")

        # var pour dire si il exite deja self.fenetreactuelle
        self.deja=0
        

    def affichage_stats(self):
        if self.deja:
            self.fenetreactuelle.destroy()
        self.deja=1

        self.fenetreactuelle = tk.Frame(self.fenetre, relief=tk.FLAT, bd=0,width=1024,height=600)
        self.fenetreactuelle.place(x=0,y=0,anchor="nw")
        
        # Créer une figure Matplotlib
        figH = Figure(figsize=(5, 4), dpi=100)
        ax = figH.add_subplot(111)
        ax.plot([1, 2, 3, 4, 5], [10, 8, 6, 4, 2], 'ro--')
        ax.set_xlabel('temps')
        ax.set_ylabel('humidity')
        ax.set_title('humidity graphe')

        canvasfig = FigureCanvasTkAgg(figH, master=self.fenetreactuelle)
        # canvasfig = FigureCanvasTkAgg(figV, master=self.fenetreactuelle)
        # affiche dans graphe
        canvasfig.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        canvasfig.draw()

        # Définir les boutons self.menu
        bouton1 = tk.Button(self.fenetreactuelle, text="retour", bg="white", fg="black",width=5,height=2,command=lambda : self.affichage_menu())
        bouton1.place(x=0, y=0, anchor="nw")

        self.fenetreactuelle.place(x=0,y=0,anchor="nw")

    def affichage_menu(self):
        if self.deja:
            self.fenetreactuelle.destroy()
        self.deja=1

        self.fenetreactuelle = tk.Frame(self.fenetre, relief=tk.FLAT, bd=0,width=1024,height=600)
        self.fenetreactuelle.place(x=0,y=0,anchor="nw")
        
        # Définir les boutons self.menu
        bouton1 = tk.Button(self.fenetreactuelle, text="state", bg="white", fg="black",width=5,height=2,command=self.affichage_stats)
        bouton1.place(x=0, y=0, anchor="nw")

        bouton2 = tk.Button(self.fenetreactuelle, text="eta actuelle", bg="white", fg="black",width=5,height=2,command=lambda : print("hello"))
        bouton2.place(x=100, y=0, anchor="nw")

        bouton3 = tk.Button(self.fenetreactuelle, text="action", bg="white", fg="black",width=5,height=2,command=lambda : print("hello"))
        bouton3.place(x=200, y=0, anchor="nw")


if __name__ == "__main__":
    s=App()
    s.affichage_menu()
    #actualiser 
    s.fenetre.mainloop()






# # ! action bouton

# def resetcanvas():
#     # menu.pack_forget()
#     # graphe.pack_forget()
#     pass

# def page_etap():
#     print("etat bai")
#     resetcanvas()

# def page_menu():
#     print("menu")
#     resetcanvas()
#     # menu.place(x=0,y=0,anchor="nw")
#     graphe.pack_forget()
    

# def page_action():
#     print("etat bai")
#     resetcanvas()

# def page_state():
#     print("state bai")
#     # resetcanvas()
#     graphe.place(x=0,y=0,anchor="nw")

# # ! menu
# menu = tk.Frame(fenetre, relief=tk.FLAT, bd=0,width=1024,height=600)

# # Définir l'image de fond
# image_de_fond = tk.PhotoImage(file="fond.gif")

# max_width = 1024
# max_height = 600
# if image_de_fond.width() > max_width or image_de_fond.height() > max_height:
#     image = image_de_fond.subsample(max(image_de_fond.width() // max_width, image_de_fond.height() // max_height))

# # menu
# canvas = tk.Canvas(menu, width=1024, height=600)
# canvas.pack(fill="both")
# canvas.create_image(0, 0, image=image, anchor="nw")


# # Définir les boutons menu
# bouton1 = tk.Button(menu, text="state", bg="white", fg="black",width=5,height=2,command=lambda : page_state())
# bouton1.place(x=0, y=0, anchor="nw")

# bouton2 = tk.Button(menu, text="eta actuelle", bg="white", fg="black",width=5,height=2,command=lambda : page_etap())
# bouton2.place(x=100, y=0, anchor="nw")

# bouton3 = tk.Button(menu, text="action", bg="white", fg="black",width=5,height=2,command=lambda : page_action())
# bouton3.place(x=200, y=0, anchor="nw")

# # Définir les boutons menu
# bouton4 = tk.Button(graphe, text="menu", bg="white", fg="black",width=5,height=2,command=lambda : page_menu())
# bouton4.place(x=200, y=0, anchor="nw")


# # ! main 
# if __name__ == "__main__":
#     # page_menu()
#     menu.place(x=0,y=0,anchor="nw")

#     # Lancer la fenêtre
#     fenetre.mainloop()

