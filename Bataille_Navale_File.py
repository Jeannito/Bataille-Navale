#Projet final bataille navale

def start():
    print("Bonjour")
    p = partie()
    #while p.partie_fini:
    p.tour(p.j2)
    p.tour(p.j1)
        

class partie:
    def  __init__(self):
        print ('Création du joueur 1')
        self.j1 = joueur()
        print ('Entrez les bateaux du joueur 1:')
        self.j1.construire()
        print ('Création du joueur 2')
        self.j2 = joueur()
        print ('Entrez les bateaux du joueur 2:')
        self.j2.construire()

    def partie_fini(self):
        print
        
        

    def tour(self, joueur):
        if joueur == self.j1 :
            print("\n\nJoueur 2")
        else :
            print("\n\nJoueur 1")
        x = input("Tir en X =")
        y = input("Tir en Y =")
        joueur.tir(x, y)
        

    
        
        

class joueur:
    def __init__(self):
        self.grille={}                                               #creation dictionnaire pour le placement des bateaux 
        for i in range (21): 
            for j in range (21): 
                self.grille[i,j]=0 

        self.bat = list
        self.bat = (bateau(1),bateau(2),bateau(3),bateau(4),bateau(5))

    def construire(self):
        self.bat[0].placer_bateau(1, self.grille)
        self.bat[1].placer_bateau(2, self.grille)
        #self.bat[2].placer_bateau(3, grille)
        #self.bat[3].placer_bateau(3, grille)
        #self.bat[4].placer_bateau(4, grille)

        for i in range(21): 

            print self.grille[0,i],'|',self.grille[1,i],'|',self.grille[2,i],'|',self.grille[3,i],'|',self.grille[4,i],'|',self.grille[5,i],'|',self.grille[6,i],'|',self.grille[7,i],'|',self.grille[8,i],'|',self.grille[9,i],'|',self.grille[10,i],'|',self.grille[11,i],'|',self.grille[12,i],'|',self.grille[13,i],'|',self.grille[14,i],'|',self.grille[15,i],'|',self.grille[16,i],'|',self.grille[17,i],'|',self.grille[18,i],'|',self.grille[19,i],'|',self.grille[20,i],'|', 
            print


    def detruire(self, name):
        if self.name.taille == 0:
            print("Coule")
        
        

    def tir(self, a , b):
        print("Tir en X=" + str(a) + " et en Y=" + str(b))
        if self.grille[a, b] == 0 : print("A l'eau")
        i = 1
        for i in range(6):
            if self.grille[a, b] == i :
                print("Touche")
                self.grille[a, b] = 0
                self.bat[i].taille = self.bat[i].taille - 1
                if self.bat[i].taille == 0:
                    print("Coule")
                

            
        
        


class bateau:
    def __init__(self, name):
        self.name = name
        self.taille = 0

    def placer_bateau(self, taille, grille):
        self.taille = taille
        x = int(input("Bateau num" + str(self.name) + " :\nX ="))
        y = int(input("Y ="))
        grille[x, y] = self.name
        if taille != 1:
            d = input("Direction (8:Haut ; 6:Droite ; 2:Bas ; 4:Gauche) = ")
            for i in range(1, taille):
                if d == 8:
                    grille[x, y-i] = self.name
                if d == 6:
                    grille[x+i, y] = self.name
                if d == 2:
                    grille[x, y+i] = self.name
                if d == 4:
                    grille[x-i, y] = self.name


start()

