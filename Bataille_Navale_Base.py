# Jean Bruté de Rémur IG3
# Programme python bataille navale version 5

print 'IL EST NECESSAIRE D AVOIR LE SHELL EN PLEIN ECRAN POUR POUVOIR JOUER A CE JEU CORRECTEMENT'
print
print

pr=raw_input('Quelle est est votre prénom? ')       #partie pas necessaire mais permet un deroulement plus ou moins interactif avec le joueur
print

ls={}                                               #creation dictionnaire pour le placement des bateaux
for i in range (21):
    for j in range (21):
        ls[i,j]=0

tab={}                                              #creation map de la bataille navale (avec un dictionnaire)
for i in range (21):
    for j in range (21):
        tab[i,j]=0
    
def affichemap():
    for i in range(21):
        print tab[0,i],'|',tab[1,i],'|',tab[2,i],'|',tab[3,i],'|',tab[4,i],'|',tab[5,i],'|',tab[6,i],'|',tab[7,i],'|',tab[8,i],'|',tab[9,i],'|',tab[10,i],'|',tab[11,i],'|',tab[12,i],'|',tab[13,i],'|',tab[14,i],'|',tab[15,i],'|',tab[16,i],'|',tab[17,i],'|',tab[18,i],'|',tab[19,i],'|',tab[20,i],'|',
        print

def aska():                                         #demande et retour de coordonnées si dans le tableau (la fonction suivante est pareille et pas forcement utile...)
    if_ok=bool(False)
    a=input('position de x?')
    while (not if_ok):
        if not a in range(21):
            print
            print 'ce n est pas dans la carte du jeu, dommage ',pr,', peut etre la prochaine fois...'
            print
            a=input('position de x?')
        else:
            if_ok=True
            return a;
def askb():     
    if_ok=bool(False)
    b=input('position de y?')
    while (not if_ok):
        if not b in range(21):
            print 'ce n est pas dans la carte du jeu, dommage ',pr,', peut etre la prochaine fois'
            print
            b=input('position de y?')
        else:
            if_ok=True
            return b;

def verifiersitouche():
    cpt=0
    if ls[10,0]==2:
        print 'bateau 1 coulé, pas trop vite ',pr,', ce n est pas le plus dur!'
        print
        cpt=cpt+1
    if ls[3,1]==2 and ls[3,2]==2:
        print 'bateau 2 coulé'
        print
        cpt=cpt+1
    if ls[1,2]==2 and ls[2,2]==2 and ls[1,2]==2:
        print 'bateau 3 coulé'
        print
        cpt=cpt+1
    if ls[11,8]==2 and ls[12,8]==2 and ls[13,8]==2:
        print 'bateau 4 coulé'
        print
        cpt=cpt+1
    if ls[19,11]==2 and ls[19,12]==2 and ls[19,13]==2 and ls[19,14]==2:
        print 'bateau 5 coulé, bravo ',pr,', c etait le plus gros'
        print
        cpt=cpt+1
    return cpt;

def verifiercasetouche():
    print
    print 'map du jeu (PS: ',pr,', ouvrir en grand écran si lecture étrange):'
    print
    print 'si un bateau est touche alors 2, si un missile a l eau 1, sinon 0'
    print
    affichemap()
    print;



def jouer():                                                #fonction principale permetttant de jouer
    while verifiersitouche()!=5:                            #tour jusqu'a ce que tout les bateaux de n'importe quelle taille soit coulé (version 5)
        touche=bool(False)
        while (not touche):                                 #tour jusqu'a ce qu'un bateau soit touché (version 2)
            a=aska()
            print
            b=askb()
            print
            tab[a,b]=1
            if ls[a,b]==1:
                print ('touché')
                touche=True
                ls[a,b]=2
                tab[a,b]==2
                verifiercasetouche()
            else:
                p=bool(False)
                for i in range (21):
                    if ls[a,i]==1:
                        p=True
                        ls[a,i]==2
                for i in range (21):
                    if ls[i,b]==1:
                        p=True
                        ls[i,b]==2
                if p:
                    print ('en vue')
                    verifiercasetouche()
                else:
                    ls[a,b]==2
                    print ('a l eau')
                    verifiercasetouche()
    print
    print 'la victoire est entre vos mains commandant ',pr,', vous avez coulé tout les bateaux adverses!!';

     
            
ls[10,0]=1                                              #position bateau 1 case

ls[3,1]=1                                               #position bateau 2 case
ls[3,2]=1

ls[1,2]=1                                               #position bateau1 3 case
ls[2,2]=1
ls[3,2]=1

ls[11,8]=1                                              #position bateau2 3 case
ls[12,8]=1
ls[13,8]=1

ls[19,11]=1                                             #position bateau 4 case
ls[19,12]=1
ls[19,13]=1
ls[19,14]=1
                                                        #j'ai juste rajouté une map pour permettre au joueur de se reperer
jouer()                                                 #en attente de le version 6 ou chaque joueur pourra placer ses bateaux et ou l'on pourra jouer a 2
