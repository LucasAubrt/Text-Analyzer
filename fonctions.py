import matplotlib.pyplot as plt #importation du module permettant de réaliser des graphiques
import customtkinter #importation du module permettant de réaliser des interfaces graphiques
from tkinter import filedialog as fd #importation du fialdialog en tant que fd
from PIL import Image #importation du module qui permet d'ouvrir/charger des images

def count_letters(txt:str) -> dict:
	assert type(txt) == str, "txt doit être de type string."

	"""
	Fonction permettant de dénombrer le nombre d'apparition de chaque lettre de l'alphabet dans le texte à analyser (autrement dit leur fréquence d'apparition).
	args:
		-txt:str, texte à analyser
	"""

	alphabet = {x : 0 for x in "abcdefghijklmnopqrstuvwxyz"} #dictionnaire contenant la fréquence d'apparition de chaque lettre

	#on parcourt un à un chaque caractère (qu'on 'minisculise') pour compter leur nombre d'apparition
	for i in txt:
		if i.lower() in alphabet: #condition qui permet de vérifier si le caractère est une lettre (et non pas un caractère spécial)
			alphabet[i.lower()] += 1

	total = 0 #variable contenant le nombre total de lettre
	for i in alphabet.values(): #on parcourt tous les nombres d'apparitions de chaque lettre pour les ajouter au total
		total += i
	for i in alphabet:
		alphabet[i] = (alphabet[i] / total) * 100 #on change la valeur (on passe de nombre d'apparition a fréquence d'apparition en pourcentage)

	return alphabet

def find_most_present_letter(alphabet:dict) -> str:
	assert type(alphabet) == dict, "alphabet doit être un dictionnaire afin de pouvoir faire l'analyse."
	"""
	Fonction permettant de retrouver la lettre la plus présente dans le dictionnaire passé en paramètre.
	args:
		-alphabet:dict, dictionnaire contenant la fréquence d'apparition de chaque lettre
	"""

	maxi = max(alphabet.values()) #renvoie le nombre de récurrence maximale atteint par au moins une lettre.

	most_present_letter = ""
	for i in alphabet: #on parcout une à une chaque lettre dans le dictionnaire
		if alphabet[i] == maxi: #si la lettre apparait le maximum de fois déterminé précédemment.
			most_present_letter += i

	return most_present_letter

def count_words(txt:str) -> dict:
	"""
	Fonction permettant de compter le nombre d'apparition de chaque mot dans le texte à analyser
	args:
		-txt:str, texte à analyser
	"""

	words = {} #dictionnaire contenant le nombre d'apparition de chaque mot présent

	for i in txt.split(): #on parcourt chaque mot du texte grâce à la fonctions split() qui créer un dictionnaire à partir d'une chaîne de caractère.
		if i in words:
			words[i] += 1 #on ajoute 1 si le mot est déja contenu dans le dictionnaire
		else:
			words[i] = 1 #sinon on ajoute une nouvelle clef et on lui assigne 1

	return words

def find_language(txt:str):
	"""
	Fonction qui permet de trouver l'origine d'une langue en faisant la somme de la fréquence d'apparition de chaque lettre (on répète la même opération pour les autres langues).
	Puis on choisi la langue dont la somme est la plus grande.
	args:
		-txt:str, texte à analyser
	"""

	#dictionnaire qui contient la fréquence d'apparition de chaque lettre pour chauque langue
	frequences = {
    "français": {"a":7.636, "b":0.901, "c":3.260, "d":3.669, "e":14.715, "f":1.066, "g":0.866, "h":0.737, "i":7.529, "j":0.545, "k":0.049, "l":5.456, "m":2.968, "n":7.095, "o":5.796, "p":2.521, "q":1.362, "r":6.693, "s":7.948, "t":7.244, "u":6.311, "v":1.838, "w":0.074, "x":0.427, "y":0.128, "z":0.326},
    "anglais": {"a":8.167, "b":1.492, "c":2.782, "d":4.253, "e":12.702, "f":2.228, "g":2.015, "h":6.094, "i":7.546, "j":0.153, "k":0.772, "l":4.025, "m":2.406, "n":6.749, "o":7.507, "p":1.929, "q":0.095, "r":5.987, "s":6.327, "t":9.056, "u":2.758, "v":0.978, "w":2.360, "x":0.150, "y":1.974, "z":0.074},
    "espagnol": {"a":12.525, "b":1.493, "c":2.215, "d":5.860, "e":13.681, "f":0.692, "g":1.768, "h":0.703, "i":6.247, "j":0.493, "k":0.011, "l":4.967, "m":3.157, "n":6.712, "o":8.683, "p":2.510, "q":0.877, "r":6.871, "s":7.977, "t":4.632, "u":2.927, "v":1.138, "w":0.017, "x":0.215, "y":1.008, "z":0.467},
    "allemand": {"a":5.577, "b":1.886, "c":3.267, "d":5.082, "e":17.396, "f":1.656, "g":3.009, "h":4.577, "i":6.550, "j":0.268, "k":1.417, "l":3.437, "m":2.534, "n":9.776, "o":2.594, "p":0.670, "q":0.018, "r":7.003, "s":7.270, "t":6.154, "u":4.166, "v":0.846, "w":1.921, "x":0.034, "y":0.039, "z":1.134}
    }

	#on initialise les fréquences pour chaque langue à 0
	freq_fr = 0
	freq_en = 0
	freq_es = 0
	freq_de = 0

	txt = txt.lower().replace(" ", "") #on convertit le texte en minuscule et on retire les espaces

	for lettre in txt: #on parcout une à une chaque lettre du texte et on ajoute la fréquence d'apparition de la lettre selon la langue
		freq_fr += frequences["français"].get(lettre, 0)
		freq_en += frequences["anglais"].get(lettre, 0)
		freq_es += frequences["espagnol"].get(lettre, 0)
		freq_de += frequences["allemand"].get(lettre, 0)

    #on détermine la fréquence la plus grande pour retrouver la langue du texte
	max_freq = max(freq_fr, freq_en, freq_es, freq_de) #on établie la fréquence max et on la compare avec chaque langue
	if max_freq == freq_fr:
		return "français"
	elif max_freq == freq_en:
		return "anglais"
	elif max_freq == freq_es:
		return "espagnol"
	else:
		return "allemand"

def choose_file(label):
	"""
	Fonction permettant de choisir le fichier texte à analyser
	args:
		-label:widget, label à modifier pour indiquer quel fichier a été choisi
	"""

	filetypes = (('text files', '*.txt')), (('All files', '*.*')) #prise en charge uniquement des .txt

	filename = fd.askopenfilename(
		title = "Ouvrir le fichier à analyser",
		initialdir = '/', #on se place dans le répertoire racine
		filetypes = filetypes
		)

	global path_file #on récupère la variable globale afin de lui assigner le chemin du fichier à chiffrer
	path_file = filename

	filename = filename.split('/') #permet de créer une liste en séparant le chemin tous les "/"

	compteur = 0
	while compteur < len(filename)-1: #on parcourt la liste dans une boucle while pour s'assurer que la liste ne contient que des strings et que le programme ait le résultat attendu.
		assert type(filename[compteur]) == str, "Le dictionnaire filename doit contenir que des éléments de type string."
		compteur += 1

	filename = filename[-1] #permet de sélectionner le dernier élément de la liste sans connaître son index

	label.configure(text=f"{filename}") #change le text(e) du label en fonction du path du fichier choisi


def launch(menu_option, text_box, lb_image, lb_most_present_letter, lb_language, app,) -> None:
	"""
	Cette fonction applique toutes les précedentes et les affiches de manière concrète dans la fenêtre graphique
	args:
		-menu_option:widget, menu_option dont la valeur indiquée va nous servir à savoir si l'utilisateur à utiliser un fichier ou la textbox
		-text_box:widget, si l'utilisateur à utilser la textbox alors on va récupérer le texte contenu à l'intérieur
		-lb_image:widget, label contenant l'image du graphique généré
		-lb_most_present_letter:widget, label dans lequel sera affiché la lettre la plus présente dans le texte analysé
		-lb_language:widget, label dans lequel sera affiché la langue du texte analysé
		-app:window, fenêtre customtkinter dans laquelle tous nos windgets sont placés
	"""

	global path_file #on récupère la variable globale qui contient le chemin du fichier texte à analyser (si l'utilisateur en a choisi un)

	if menu_option.get() == "Texte": #on vérifie si l'utilisateur à utiliser la textbox ou un fichier txt
		txt = text_box.get(1.0, 'end') #permet de récupérer tout le contenu de la textbox
	else:
		file = open(path_file, "r") #ouvre le fichier txt à analyser en mode lecture
		txt = file.read() #recupère le contenu dans la variable txt
		file.close() #et fermeture du fichier

	
	donnees = count_letters(txt) #dictionnaire contenant la fréquence d'apparition de chaque lettre
	plt.clf() #permet de supprimer toutes les données précédemment stockés dans le graphique afin d'en recommencer un (si l'utilisateur se sert du programme plusieurs fois à la suite)
	plt.bar(donnees.keys(), donnees.values(), color='g') #fonction permettant de tracer le graphique
	plt.savefig("graph.png", dpi=300) #enregistrement de l'image du graphique

	graph = customtkinter.CTkImage(light_image=Image.open("graph.png"), #on charge l'image du graphique
                                  dark_image=Image.open("graph.png"),
                                  size=(300,300))
	lb_image.configure(image=graph) #on l'applique au label

	lb_most_present_letter.configure(text=f"Lettre la plus présente : {find_most_present_letter(donnees)}") #on affiche la lettre la plus présente dans le label

	mots = count_words(txt)#dictionnaire contenant le nombre d'apparition de chaque mots

	#on détermine la langue du texte grâce à la fonction
	langue = find_language(txt)
	lb_language.configure(text=f"Langue : {langue}")

	phr1 = "" #on créer une chaîne de caractère mise en forme pour afficher par la suite le nombre d'apparition de chaque lettres contenus dans le texte à analyser
	for k,v in donnees.items(): #on parcourt chaque clé et sa valeur qui lui est associée
		phr1 = phr1 + f"{k} : {v}\n"

	phr2 = "" #on créer une chaîne de caractère mise en forme pour afficher par la suite le nombre d'apparition de chaque mots contenus dans le texte à analyser 
	for k,v in mots.items(): #on parcourt chaque clé et sa valeur qui lui est associée
		phr2 = phr2 + f"{k} : {v}\n"

	#on ouvre en mode "écrasement" un fichier faisant le bilan de l'analyse, en combinant les deux chaînes de caractère générées précédemment.
	file = open("bilan.txt", "w")
	file.write(f"---Lettres (en %)---\n{phr1}\n---Mots (en nombre)---\n{phr2}\n\nLettre la plus présente : {find_most_present_letter(donnees)}\n\nLangue : {langue}") #on écrit le bilan dans le fichier
	file.close() #on ferme le fichier