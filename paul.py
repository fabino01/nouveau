TP 01 Python

1.Ecrire un programe qui affiche 500 fois " je dois faire des sauvegardes régulières de mes fichiers"
for i in range(500): #500 "tours"
	print('je dois faire des sauvegardes régulières de mes fichiers')

2.Écrire un programme qui affiche tous les nombres impairs entre 0 et 1000, par ordre croissant : « 1 3 5 7 ... 995 997 999 »
a= 1
while (a < 1000):
	a
+=2

3.Écrire un programme qui affiche la table de multiplication par 13
a = 1
while a < 11:
	print(n * 13)
	compteur+= 1

4.Écrire un programme qui demande un mot à l’utilisateur et qui affiche à l’écran le nombre de lettres de ce mot.
print(len('fabino'))
6

5.Ecrire un programme qui demande un nombre entier à l’utilisateur. L’ordinateur affiche ensuite le message "Ce nombre est pair" ou "Ce nombre est impair" selon le cas.
a = int(input( "give me a number : "))
    if (a % 2 == 0):
    print("nombre pair")
    else:
    print("nombre impair")
print

6.Ecrire un programme qui demande un nombre compris entre 10 et 20, jusqu’à ce que la réponse convienne. En cas de réponse supérieure à 20, on fera apparaître un message : « Plus petit ! », et inversement, « Plus grand ! » si le nombre est inférieur à 10.
 a = int(input("give me a number between 10 et 20 :"))
    if (a > 20):
      print text ("plus petit")
    elif(a <10):
      print text ("plus grand")
print

7.Ecrire un programme qui demande un nombre de départ, et qui ensuite affiche les dix nombres suivants. Par exemple, si l'utilisateur entre le nombre 17, le programme affichera les nombres de 18 à 27.
a =1
a = input ("give me a number:")
while a < 11:
   print(a,a < 11)
    a += 1
print

8.Ecrire un programme qui demande un nombre de départ, et qui ensuite écrit la table de multiplication de ce nombre.
a = int(input("give me a number:"))
    print(a * 1)
    print(a * 2)
    print(a * 3)
    print(a * 4)
    print(a * 5)
    print(a * 6)
    print(a * 7)
    print(a * 8)
    print(a * 9)
    print(a * 10)
print


9.Ecrire un programme qui demande un nombre de départ, et qui calcule la somme des entiers jusqu’à ce nombre. Par exemple, si l’on entre 5, le programme doit calculer : 1 + 2 + 3 + 4 + 5 = 15, afficher que le résultat
a = int(input("give me a number:"))


10 Écrire un programme qui demande l’âge d’un enfant à l’utilisateur. Ensuite il l’informe de sa catégorie :

       "Poussin" de 6 à 7 ans

        "Pupille" de 8 à 9 ans

        "Minime" de 10 à 11 ans

        "Cadet" après 12 ans

a = int(input("donne l'âge?:"))
    if (a == 6 or a == 7)
          print ("poussin")
   elif(a == 8 or a == 9)
          print ("pupille")
   elif(a == 10 or a == 11)
          print ("minime")
   elif(a > 12)
          print ("cadet")
   else
          print ("too small")
print


11 Ecrivez un programme qui calcule le prix TTC d'un nombre donné d'articles de prix unitaire donné.

Avec une T.V.A. à 20%.

Les résultats devront se présenter ainsi :

nombres d'articles : 5

prix HT : 42.15 €

Prix TTC : 252.06 €

a_article = int(input("nbre d'article ?:"))
    prix _article = float(input("quel est le prix HT unitaire de l'article?:"))
    prixht = prix article * a_article
    print ("nombres d'articles : ",a_article)
    print ("prix HT : ",printht)
    tva = (prixht * 1.2)
    print ("prix TTC:", tva)
print




