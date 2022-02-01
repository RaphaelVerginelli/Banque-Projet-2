import tkinter as tk
import os.path 
import matplotlib.pyplot as plt                                #Bibliothèque pour gérer documents textes et graphiques
import numpy as np
from tkinter import ttk
from tkinter import * 
from tkinter.messagebox import showinfo

class CompteBancaire():
    "création d'une simulation de banque et de ses fonctions"
    
    def __init__(self, name, iden, mdp):
        self.name = name
        self.iden = iden
        self.mdp = mdp
                #Création du repertoire et des données de l'utilisateur
        writer = open("repertoire.txt", "a")  
        writer.write(self.iden + " ")
        writer.write(self.mdp + " ")
        writer.write(self.name+" ")
        writer.write("None")
        writer.write(" ")
        writer.write("None")
        writer.write("\n")

        writer.close()  #on ferme le fichier
            
        
    def affiche(self):
        fds=open("repertoire.txt", "r")             #affiche le document texte repertoire contenant les données
        if fds.mode == 'r':
            contents = fds.readlines()
        fds.close()
        print(contents)
            
    def identite(self):
        #méthode pour se connecter et avoir accés à uniquement ses données et pas celle des autres
        self.condition_de_boucle = False   
        #on stocke dans une variable le contenu des lignes 
        f = open("repertoire.txt", 'r')
        if f.mode == 'r':
            self.contenu = f.readlines()
        f.close()
        for i in range(len(self.contenu)):
            #On utilise les données du document et on les transforme de manière à les exploiter
            self.ligne = self.contenu[i]
            self.coupe = self.ligne.split(" ")
            self.pseudo = self.coupe[0]
            self.motdepasse=self.coupe[1]
#on vérifie si les mots de passe et utlisateurs sont bons, pas besoin de rentrer de nouveaux ses codes grace aux self.verif
            if self.pseudo == self.verif and self.motdepasse == self.verif2:
                self.pseudo = self.verif
                self.motdepasse = self.verif2
                self.condition_de_boucle = True
                break
                    

    def creer_compte_courant(self):
        #méthode pour créer un compte courant
        self.condition_de_boucle = False
        #on stocke dans une variable le contenu des lignes 
        f = open("repertoire.txt", 'r')
        if f.mode == 'r':
            self.contenu = f.readlines()
        f.close()
        for i in range(len(self.contenu)):
            #On utilise les données du docuement et on les transforme de manière à les exploiter
            self.ligne = self.contenu[i]
            self.coupe = self.ligne.split(" ")
            pseudo = self.coupe[0]
            motdepasse=self.coupe[1]
            nom = self.coupe[2]
#on vérifie si les mots de passe et utlisateurs sont bons, pas besoin de rentrer de nouveaux ses codes grace aux self.verif
            if pseudo == self.verif and motdepasse == self.verif2:
                #Pour modifier la lignes du documents on l'efface et on l'écris de nouveau avec les modification
                self.contenu[i]=""
                self.banque = '0'
                self.contenu.append(pseudo + " " + motdepasse + " " + nom + " " + self.banque + " " + 'None'+ '\n')
#la commande "write" permet d'effacer tout le document et de réecrire, ici avec les modification dans self.contenu
                writer = open('repertoire.txt','w+')
                for z in range(len(self.contenu)):
                    writer.write(self.contenu[z])
                writer.close()
    
    def creer_compte_épargne(self):
        #même méthode que la précedente mais pour le compte épargne
        self.condition_de_boucle = False
        f = open("repertoire.txt", 'r')
        if f.mode == 'r':
            self.contenu = f.readlines()
        f.close()
#seule différence on exige la création d'un compte courant avant un compte épargne, condition d'utilisation de la banque
        if self.banque == '0':
            for i in range(len(self.contenu)):
                #On utilise les données du docuement et on les transforme de manière à les exploiter
                self.ligne = self.contenu[i]
                self.coupe = self.ligne.split(" ")
                pseudo = self.coupe[0]
                motdepasse=self.coupe[1]
                nom = self.coupe[2]
#on vérifie si les mots de passe et utlisateurs sont bons, pas besoin de rentrer de nouveaux ses codes grace aux self.verif
                if pseudo == self.verif and motdepasse == self.verif2:
                    self.contenu[i]=""
                    self.contenu.append(pseudo + " " + motdepasse + " " + nom + " " + '0' + " " + '0' + '\n')
#la commande "write" permet d'effacer tout le document et de réecrire, ici avec les modification dans self.contenu
                    writer = open('repertoire.txt','w+')
                    for z in range(len(self.contenu)):
                        writer.write(self.contenu[z])
                    writer.close()
        else:
            print("Veuillez crée un compte courant avant un compte épargne")
                

    
    def depot(self):
        #méthodes pour ajouter de l'argent sur un des 2 comptes
        #on stocke dans une variable le contenu des lignes 
        f = open("repertoire.txt", 'r')
        if f.mode == 'r':
            self.contenu = f.readlines()
        f.close()
        self.condition_de_boucle2 = False
        for i in range(len(self.contenu)):
#on relit le fichier et on stock les nouvelles informations dans la variable (afin d'éxécuter la fonction 
#plusieurs fois sans erreur)
            f = open("repertoire.txt", 'r')
            if f.mode == 'r':
                self.contenu = f.readlines()
            f.close()
            #On utilise les données du docuement et on les transforme de manière à les exploiter
            self.ligne = self.contenu[i]
            self.coupe = self.ligne.split(" ")
            pseudo = self.coupe[0]
            motdepasse=self.coupe[1]
            nom = self.coupe[2]
#on vérifie si les mots de passe et utlisateurs sont bons, pas besoin de rentrer de nouveaux ses codes grace aux self.verif
            if pseudo == self.verif and motdepasse == self.verif2:
                #on ouvre le document historique courant pour stocker les modifications pour la création de graphique
                fw = open('historique_courant_'+motdepasse+'_.txt', 'a')
#création d'une variable qui transforme la réposne en str ce qui correspond à la vérification de la condition
                if self.condition == "compte courant" or self.condition == "Compte courant" or self.condition == '1':
                        #on effectue les opérations pour ajouter l'argent et on modifie les données de self.contenu
                    result = int(self.coupe[3])+ int(self.depot)
                    self.coupe[3] = str(result)
                    self.contenu[i]=""
                    self.contenu.append(pseudo + " " + motdepasse + " " + nom + " " + self.coupe[3] + " " + self.coupe[4])
    #on écrit dans le fichier historique la valeur du compte après la modification, un espace et of ferme le fichier
                    fw.write(self.coupe[3])
                    fw.write(' ')
                    fw.close()
    #la commande "write" permet d'effacer tout le document et de réecrire, ici avec les modification dans self.contenu
                    file = open('repertoire.txt','w+')
                    for z in range(len(self.contenu)):
                        file.write(self.contenu[z])
                    file.close()
                    self.condition_de_boucle2 = True
                    #on effectue les mêmes opérations pour le compte épargne et avec le fichier historique épargne
                elif self.condition == "compte epargne" or self.condition == "Compte epargne" or self.condition == '2':
                    fw1 = open('historique_epargne.txt', 'a')
                    result2 = int(self.coupe[4])+ int(self.depot)
                    self.coupe[4] = str(result2)
                    
                    self.contenu[i]=""
                    self.contenu.append(pseudo + " " + motdepasse + " " + nom + " " + self.coupe[3] + " " + self.coupe[4])
                    fw1.write(self.coupe[4])
                    fw.write(' ')
                    fw1.close()
                    file = open('repertoire.txt','w+')
                    for z in range(len(self.contenu)):
                        file.write(self.contenu[z])
                    file.close()
                    self.condition_de_boucle2 = True            
    
    def retrait(self):
        #même méthode que pour le dépot mais cette fois on retire de l'argent
        f = open("repertoire.txt", 'r')
        if f.mode == 'r':
            self.contenu = f.readlines()
        f.close()
        self.condition_de_boucle3 = False
        for i in range(len(self.contenu)):
            f = open("repertoire.txt", 'r')
            if f.mode == 'r':
                self.contenu = f.readlines()
            f.close()
            self.ligne = self.contenu[i]
            self.coupe = self.ligne.split(" ")
            pseudo = self.coupe[0]
            motdepasse=self.coupe[1]
            nom = self.coupe[2]
            if pseudo == self.verif and motdepasse == self.verif2:
                fw = open('historique_courant_'+motdepasse+'_.txt', 'a')
                if self.condition == "compte courant" or self.condition == "Compte courant" or self.condition == '1':   
                    result = int(self.coupe[3])- int(self.retrait)
                    self.condition_de_boucle3 = True
                    if result < 0 :
                         showinfo(message ="Vous n'avez pas assez d'argent sur ce compte pour effectuer ce retrait")   
                    else:
                        self.coupe[3] = str(result)
                        self.contenu[i]=""
                        self.contenu.append(pseudo + " " + motdepasse + " " + nom + " " + self.coupe[3] + " " + self.coupe[4])
                        fw.write(self.coupe[3])
                        fw.write(' ')
                        fw.close()
                        file = open('repertoire.txt','w+')
                        for z in range(len(self.contenu)):
                            file.write(self.contenu[z])
                        file.close()        
                elif self.condition == "compte epargne" or self.condition == "Compte epargne" or self.condition == '2':
                    result2 = int(self.coupe[4])-int(self.retrait)
                    self.condition_de_boucle3 = True
                    if result2 < 0 :
                        showinfo(message ="Vous n'avez pas assez d'argent sur ce compte pour effectuer ce retrait")
                    else:
                        self.coupe[4] = str(result2)
                        self.contenu[i]=""
                        self.contenu.append(pseudo + " " + motdepasse + " " + nom + " " + self.coupe[3] + " " + self.coupe[4])
                        file = open('repertoire.txt','w+')
                        for z in range(len(self.contenu)):
                            file.write(self.contenu[z])
                        file.close()
                    
    def afficher_compte(self):
        #méthode qui permet de visualiser son comtpte courant et son compte épargne
        f = open("repertoire.txt", 'r')
        if f.mode == 'r':
            self.contenu = f.readlines()
        f.close()
        for i in range(len(self.contenu)):
            self.ligne = self.contenu[i]
            self.coupe = self.ligne.split(" ")
            pseudo = self.coupe[0]
            motdepasse=self.coupe[1]
            nom = self.coupe[2]         
            if pseudo == self.verif and motdepasse == self.verif2:
                return self.coupe[3], self.coupe[4]
            
    def creer_historique(self):
        #fonction qui permet de créer les fichiers contenant les variations des comptes (pour les graphiques)
        f = open("repertoire.txt", 'r')
        if f.mode == 'r':
            self.contenu = f.readlines()
        f.close()
        for i in range(len(self.contenu)):
            #On utilise les données du docuement et on les transforme de manière à les exploiter
            self.ligne = self.contenu[i]
            self.coupe = self.ligne.split(" ")
            pseudo = self.coupe[0]
            motdepasse=self.coupe[1]
        #on vérifie si les mots de passe et utlisateurs sont bons, pas besoin de rentrer de nouveaux ses codes grace aux self.verif
            if pseudo == self.verif and motdepasse == self.verif2:
                writer = open("historique_courant_"+motdepasse+"_.txt", "a")
    
    
    def graphique_courant(self):
        #méthodes qui crée un graphiques du compte courant 
        liste = []
        indice = []
        f = open("repertoire.txt", 'r')
        if f.mode == 'r':
            self.contenu = f.readlines()
        f.close()
        for i in range(len(self.contenu)):
            #On utilise les données du docuement et on les transforme de manière à les exploiter
            self.ligne = self.contenu[i]
            self.coupe = self.ligne.split(" ")
            pseudo = self.coupe[0]
            motdepasse=self.coupe[1]
            #on vérifie si les mots de passe et utlisateurs sont bons, pas besoin de rentrer de nouveaux ses codes grace aux self.verif
            if pseudo == self.verif and motdepasse == self.verif2:
                bowl = open("historique_courant_"+motdepasse+"_.txt",'r')
                if bowl.mode == 'r':
                    hist = bowl.readlines()
                bowl.close()
                for i in range(len(hist)):
                    ligne = hist[i]
                    coupe = ligne.split(' ')
                for i in range(len(coupe)):
                    liste.append(coupe[i])
                    indice.append(i)
                del liste[-1]
                del indice[-1]
                ints = [int(item) for item in liste]
                x = np.array(indice)
                y = np.array(ints)
                plt.plot(x,y)
                plt.show()
        
def effacer_compte():
    #fonction qui permet de supprimer le répertoire, et de repartir à zéro
    os.remove('repertoire.txt')

class App(tk.Tk,CompteBancaire):
    def __init__(self):
        super().__init__()

        # configure the root window
        self.title('une super banque')
        self.geometry('10000x10000')
        # label
        self.texte1 = ttk.Label (self, text = "Bienvenus chez notre banque")
        self.texte1.pack()

        self.question = ttk.Label(self, text="Avez vous deja un compte ?")
        self.question.pack()

        value = str()
        self.choix1 = ttk.Radiobutton(self, text="oui", variable=value, value=1, command=self.connexion)
        self.choix2 = ttk.Radiobutton(self, text="non", variable=value, value=2, command=self.inscription)
        self.choix1.pack()
        self.choix2.pack()
    def retour(self):
        self.destroy()
        self.__init__()
        
    def effacer(self):
        for i in self.winfo_children():
            i.destroy()
    def connexion(self):
        App.effacer(self)
        self.title("connexion")
        self.bouton=ttk.Button(self, text="retour", command=self.retour)
        self.bouton.pack()
        value = str()
        value2 = str()
        self.question1 = ttk.Label (self, text = "Rentrez votre identifiant")
        self.question1.pack()
        self.entree1 = ttk.Entry(self, textvariable=value, width=30)
        self.entree1.pack()
        self.question2 = ttk.Label (self, text = "Rentrez votre mot de passe")
        self.question2.pack()
        self.entree2 = ttk.Entry(self, textvariable=value2, width=30)
        self.entree2.pack()
        self.bouton=ttk.Button(self, text="validez", command=self.recupere)
        self.bouton.pack()
    
    def recupere(self):
        self.verif = self.entree1.get()
        self.verif2 = self.entree2.get()
        CompteBancaire.identite(self)
        if self.condition_de_boucle == False:
            showinfo(message ='La connexion a échoué, veuillez réessayer')
            App.connexion(self)
        else :
            App.compte(self)
            
    def recupere2(self):
        f = open("repertoire.txt", 'r')
        if f.mode == 'r':
            self.contenu = f.readlines()
        f.close()
        for i in range(len(self.contenu)):
            self.ligne = self.contenu[i]
            self.coupe = self.ligne.split(" ")
            motdepasse = self.coupe[1]
            if motdepasse == self.entree5.get():
                showinfo(message ='Ce mot de passe est deja utilisé')
                self.destroy()
                App.__init__(self)
        else:
            App.recupere3(self)
        
    def recupere3(self):    
        user = CompteBancaire(self.entree3.get(),self.entree4.get(),self.entree5.get())
        showinfo(message ='votre compte a bien ete créer')
        self.destroy()
        App.__init__(self)
                
    def inscription(self):
        App.effacer(self)
        self.title("inscription")
        bouton=ttk.Button(self, text="retour", command=self.retour)
        bouton.pack()
        value3 = str()
        value4 = str()
        value5 = str()
        question3 = ttk.Label (self, text = "Rentrez votre nom")
        question3.pack()
        self.entree3 = ttk.Entry(self, textvariable=value3, width=30)
        self.entree3.pack()
        question4 = ttk.Label (self, text = "Rentrez votre identifiant")
        question4.pack()
        self.entree4 = ttk.Entry(self, textvariable=value4, width=30)
        self.entree4.pack()
        question5 = ttk.Label (self, text = "Rentrez votre mot de passe")
        question5.pack()
        self.entree5 = ttk.Entry(self, textvariable=value5, width=30)
        self.entree5.pack()
        bouton=ttk.Button(self, text="validez", command=self.recupere2)
        bouton.pack()
    
    def compte(self):
        App.effacer(self)
        self.title("mon compte")
        f = open("repertoire.txt", 'r')
        if f.mode == 'r':
            self.contenu = f.readlines()
        f.close()
        for i in range(len(self.contenu)):
#on relit le fichier et on stock les nouvelles informations dans la variable (afin d'éxécuter la fonction 
#plusieurs fois sans erreur)
            f = open("repertoire.txt", 'r')
            if f.mode == 'r':
                self.contenu = f.readlines()
            f.close()
            #On utilise les données du docuement et on les transforme de manière à les exploiter
            self.ligne = self.contenu[i]
            self.coupe = self.ligne.split(" ")
            pseudo = self.coupe[0]
            motdepasse=self.coupe[1]
            nom = self.coupe[2]
            compte_courant = self.coupe[3]
#on vérifie si les mots de passe et utlisateurs sont bons, pas besoin de rentrer de nouveaux ses codes grace aux self.verif
            if pseudo == self.verif and motdepasse == self.verif2:
                if compte_courant == "None":
                    CompteBancaire.creer_compte_courant(self)
                    CompteBancaire.creer_compte_épargne(self)
                    CompteBancaire.creer_historique(self)
                    App.compte(self)
                else: 
                    compte_courant = ttk.Label (self, text = "argent sur votre compte courant :  " + self.coupe[3])
                    compte_courant.place(x=900, y=10)
                    compte_epargne = ttk.Label (self, text = "argent sur votre compte epargne :  " + self.coupe[4])
                    compte_epargne.place(x=900, y=50)
                    bouton=ttk.Button(self, text="depot", command=self.depot)
                    bouton.place(x=1100, y=150)
                    bouton=ttk.Button(self, text="retrait", command=self.retrait)
                    bouton.place(x=900, y=150)
                    bouton=ttk.Button(self, text="retour", command=self.retour)
                    bouton.place(x=0, y=0)
                    bouton=ttk.Button(self, text="evolution de votre compte", command=self.graph)
                    bouton.place(x=1500, y=850)
    
    def depot(self):
        App.effacer(self)
        value6 = int()
        value7 = str()
        question6 = ttk.Label (self, text = "choisissez un montant a deposer")
        question6.pack()
        self.entree6 = ttk.Entry(self, textvariable=value6, width=30)
        self.entree6.pack()
        question7 = ttk.Label (self, text = "choisissez un compte sur lequel deposer votre argent")
        question7.pack()
        bouton = Checkbutton(self, text="compte courant" , command=self.depot2)
        bouton.pack()
        bouton = Checkbutton(self, text="compte épargne" , command=self.depot3)
        bouton.pack()
        bouton=ttk.Button(self, text="retour", command=self.compte)
        bouton.place(x=0, y=0)
    def depot2(self):
        self.depot = self.entree6.get()
        self.condition = "1"
        CompteBancaire.depot(self)
        App.compte(self)
    def depot3(self):
        self.depot = self.entree6.get()
        self.condition = "2"
        CompteBancaire.depot(self)
        App.compte(self)
    def retrait(self):
        App.effacer(self)
        value8 = int()
        value9 = str()
        question9 = ttk.Label (self, text = "choisissez un montant a deposer")
        question9.pack()
        self.entree8 = ttk.Entry(self, textvariable=value8, width=30)
        self.entree8.pack()
        question10 = ttk.Label (self, text = "choisissez un compte sur lequel deposer votre argent")
        question10.pack()
        bouton = Checkbutton(self, text="compte courant" , command=self.retrait2)
        bouton.pack()
        bouton = Checkbutton(self, text="compte épargne" , command=self.retrait3)
        bouton.pack()
        bouton=ttk.Button(self, text="retour", command=self.compte)
        bouton.place(x=0, y=0)
    def retrait2(self):
        self.retrait = self.entree8.get()
        self.condition = "1"
        CompteBancaire.retrait(self)
        App.compte(self)
     
    def retrait3(self):
        self.retrait = self.entree8.get()
        self.condition = "2"
        CompteBancaire.retrait(self)
        
        App.compte(self)  
    def graph(self):
        CompteBancaire.graphique_courant(self)
        
if __name__ == "__main__":
    app = App()
    app.mainloop()