def start():
    print("Bonjour")
    p = partie()
    #while p.partie_fini:
    p.tour(p.j1)
        

class partie:
    def  __init__(self):
        print ('CrÃ©ation du joueur 1')
        self.j1 = joueur()
        print ('Entrez les bateaux du joueur 1:')
        self.j1.construire()
        print ('CrÃ©ation du joueur 2')
        self.j2 = joueur()
        print ('Entrez les bateaux du joueur 2:')
        self.j2.construire()

    def partie_fini(self):
        if self.j1.bat == 0 or self.j2.bat == 0 : return True
        else : return False

    def tour(self, joueur):
        if joueur == self.j1 : print("\n\nJoueur 1")
        else : print("\n\nJoueur 2")
        x = input("Tir en X =")
        y = input("Tir en Y =")
        joueur.tir(x, y)
        

    
        
        

class joueur:
    def __init__(self):
        self.bat = list
        self.alive = [1,1,1,1,1]
        self.bat = (bateau("Bateau de taille 4"),bateau("Bateau de taille 3"),bateau("Bateau de taille 3"),bateau("Bateau de taille 2"),bateau("Bateau de taille 1"))

    def construire(self):
        self.bat[0].placer_bateau(1)
        #self.bat[1].placer_bateau(2)
        #self.bat[2].placer_bateau(3)
        #self.bat[3].placer_bateau(3)
        #self.bat[4].placer_bateau(4)

    def detruire(self, i):
        self.bat[i] = 0
        
        

    def tir(self, a , b):
        print("Tir en X=" + a + " et en Y=" + b)
        touch = False
        i = 0
        y = 0
        while y != 5 and touch = False:
            while i != 4 and touch = False:
                if self.bat[y].liste_position[i].x == a and self.bat[y].liste_position[i].y == b :
                        touch = True
                        print("TouchÃ©")
                        #le mieux serait de faire une fonction kill position genre self.bat[y].kill[i] qui dÃ©callerait les valeurs et qui diminuerait la taille du bateau
                        self.bat[y].liste_position[i]=0
            y = y + 1
            i = i + 1

        if touch == False print("CoulÃ©")


class bateau:
    def __init__(self, name):
        self.name = name
        self.liste_position = (position(),position(),position(),position(),position())

    def placer_bateau(self, taille):
        x = int(input(self.name + " :\nX ="))
        y = int(input("Y ="))
        self.liste_position[0].creer_position(x,y)
        if taille != 1:
            d = input("Direction (H:Haut ; D:Droite ; B:Bas ; G:Gauche) = ")
            for i in range(1, taille - 1):
                if d == 'H':
                    self.liste_position[i].creer_position(x,y+i)
                if d == 'D':
                    self.liste_position[i].creer_position(x+i,y)
                if d == 'B':
                    self.liste_position[i].creer_position(x,y-i)
                if d == 'G':
                    self.liste_position[i].creer_position(x-i,y)

       
class position:
    def __init__(self):
        self.x = 0
        self.y = 0

    def creer_position(self, x, y):
        self.x = x
        self.y = y

