"""
Programme réalisé par Abid, Yassine, 1g8
"""
from tkinter import*
import pygame
#initialisation graphique
pygame.init()

key=1
fenetre = pygame.display.set_mode((1200, 768))
pygame.display.set_caption("jeu d'aventure")
font = pygame.font.Font('freesansbold.ttf', 30)

image12=pygame.image.load("intro.png")
image1=pygame.image.load("entrée.jpg")
image2=pygame.image.load("entréeintern.jpg")
image3=pygame.image.load("couloir.jpg")
image4=pygame.image.load("sdb.jpg")
image5=pygame.image.load("cuisine.jpg")
image6=pygame.image.load("salon.jpg")
image7=pygame.image.load("jardin.jpg")
image8=pygame.image.load("cabanon.jpg")
image9=pygame.image.load("étage.jpg")
image10=pygame.image.load("chambreparental.jpg")
image11=pygame.image.load("chambreenfant.jpg")


text1 = font.render("Vous êtes devant l'entrée", True, (0, 0, 0))
text2 = font.render("Vous êtes a l'entrée principal", True, (255, 255,255))
text3 = font.render("vous vous trouvez dans le couloir", True, (0, 0, 0))
text4 = font.render("Vous êtes dans la salle de bain", True, (255, 255,255))
text5 = font.render("Vous êtes dans la cuisine", True, (0, 0, 0))
text6 = font.render("Vous êtes dans le salon", True, (0, 0, 0))
text7 = font.render("Vous êtes dans le jardin", True, (0,0,0))
text8 = font.render("Oh tien ... Voilà", True, (255, 255, 255))
text13 = font.render("la clée de la chambre parental !!!", True, (255, 255, 255))
text9 = font.render("vous etes a l'étage", True, (255,255,255))
text10 = font.render("" , True, (255, 255, 255))
text11 = font.render(" Chut !!! Vous êtes dans la chambre de ", True, (0, 0, 0))
text12 = font.render("l'enfant, il ne faudrais pas le reviellée ", True, (0, 0, 0))

dansQuellePierceEstLePersonnage=12
def decrireLaPiece(piece):
    global key
    
    if piece==12:
        fenetre.blit(image12,(10,0))
    
    elif piece==1:
        fenetre.blit(image1,(10,0)) #afficher l'image à la prochaine actualisation
        fenetre.blit(text1,(70,100)) #afficher le texte à la prochaine actualisation
 
    elif piece==2:
        fenetre.blit(image2,(5,0))
        fenetre.blit(text2,(70,650))
 
    elif piece==3:
        fenetre.blit(image3,(10,0))
        fenetre.blit(text3,(70,600))
 
    elif piece==4:
        fenetre.blit(image4,(10,0))
        fenetre.blit(text4,(250,650))
 
    elif piece==5:
        fenetre.blit(image5,(0,0))
        fenetre.blit(text5,(70,600))
 
    elif piece==6:
        fenetre.blit(image6,(0,0))
        fenetre.blit(text6,(70,650))
 
    elif piece==7:
        fenetre.blit(image7,(0,0))
        fenetre.blit(text7,(70,650))
 
    elif piece==8:
        key=2
        fenetre.blit(image8,(0,0))
        fenetre.blit(text8,(75,600))
        fenetre.blit(text13,(75,650))
 
    elif piece==9:
        fenetre.blit(image9,(0,0))
        fenetre.blit(text9,(70,650))
 
    elif piece==10:
        fenetre.blit(image10,(0,0))
        fenetre.blit(text10,(0,300))
 
    elif piece==11:
        fenetre.blit(image11,(0,0))
        fenetre.blit(text11,(62,600))
        fenetre.blit(text12,(70,650))



def decision(direction,piece):
    print("Vous désirez allez au",direction)
    memorisePiece=piece

    if event.key==pygame.K_RETURN:
        if piece==12:
            piece=1


    #déplacement Nord
    if direction=='n':
        if piece==2:
            piece=9
        if piece==3:
            piece=4
        if piece==5:
            piece=3
        if piece==7:
            piece=6
    #déplacement Sud
    elif direction=='s':
        if piece==9:
            piece=2
        if piece==3:
            piece=5
        if piece==4:
            piece=3
        if piece==6:
            piece=7

     #déplacement Est
    elif direction=='e':
        if piece==3:
            piece=6
        if piece==2:
            piece=3
        if piece==1:
            piece=2          
        if piece==9:
            piece=11
        if piece==7:
            piece=8     
            

    #déplacement ouest
    elif direction=='o':
        if piece==2:
            piece=1
        if piece==3:
            piece=2
        if piece==6:
            piece=3
        
        if piece==9:
            if key==2:
                print("porte deverouillée")
                piece=10
            else:
                print("porte verouillée")
                piece=9

        if piece==11:        
            piece=9
        if piece==8:
            piece=7
        
    if memorisePiece==piece:
        print("Deplacement impossible")
    return piece

loop=True
while loop==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            loop = False #fermeture de la fenetre (croix rouge)
        elif event.type == pygame.KEYDOWN: #lecture du clavier
            dansQuellePierceEstLePersonnage=decision(event.unicode,dansQuellePierceEstLePersonnage)
            if event.key == pygame.K_ESCAPE or event.unicode == 'q': #touche q pour quitter
                loop = False
    decrireLaPiece(dansQuellePierceEstLePersonnage)
 # Actualisation de l'affichage
    pygame.display.flip()
pygame.quit()
