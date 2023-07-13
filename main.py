import fonctions #importation du fichier fonctions.py qui contient toutes les fonctions que nous avons crée
import customtkinter #importation du module permettant de réaliser des interfaces graphiques

#proprietés de la fenêtre
customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")
app = customtkinter.CTk()
app.title("Text Analyzer")
app.resizable(height=False, width=False)
app.geometry("800x400")


#widgets de la fenêtre

#partie gauche
menu_option = customtkinter.CTkOptionMenu(master=app, values=["Texte","Fichier"]) #on choisit d'écrire un texte dans la textbox ou de choisir un fichier.txt déja existant
menu_option.place(relx=0.1, rely=0.1, anchor=customtkinter.CENTER)

btn_file = customtkinter.CTkButton(master=app, text="Choisir Fichier", command=lambda:fonctions.choose_file(label_fichier)) #bouton permettant de choisir un fichier
btn_file.place(relx=0.1, rely=0.2, anchor=customtkinter.CENTER)

label_fichier = customtkinter.CTkLabel(master=app, text="Fichier choisi :") #label permettant d'afficher le fichier choisi
label_fichier.place(relx=0.063, rely=0.3, anchor=customtkinter.CENTER)

text_box = customtkinter.CTkTextbox(master=app, width=350, wrap='none') #textbox dans laquelle l'utilisateur peut écrire du texte à analyser
text_box.place(relx=0.23, rely=0.6, anchor=customtkinter.CENTER)

btn_start = customtkinter.CTkButton(master=app, text="Analyser", command=lambda:fonctions.launch(menu_option, text_box, lb_image, lb_most_present_letter, lb_language, app)) #bouton permettant de lancer l'analyse
btn_start.place(relx=0.1, rely=0.9, anchor=customtkinter.CENTER)

#partie droite
lb_image = customtkinter.CTkLabel(master=app, image=None, text='') #label contenant l'image du graphique qui va être généré
lb_image.place(relx= 0.8, rely=0.3, anchor=customtkinter.CENTER)

lb_most_present_letter = customtkinter.CTkLabel(master=app, text="") #label permettant d'afficher la lettre la plus présente dans le texte analysé
lb_most_present_letter.place(relx=0.8, rely=0.72, anchor=customtkinter.CENTER)

lb_language = customtkinter.CTkLabel(master=app, text="") #label permettant d'afficher la langue du texte
lb_language.place(relx=0.8, rely=0.8, anchor=customtkinter.CENTER)

app.mainloop() #fonction permettant d'afficher la fenêtre